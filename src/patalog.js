import React from 'react';
import { connect } from 'react-redux';
import * as d3 from 'd3';

const allFilterTypes = ['furniture', 'fashion', 'misc', 'diy', 'fish', 'bugs', 'sea'];

class Patalog extends React.Component {
	constructor() {
		super()
		this.state = {
			searchVal: '',
			filterTypes: allFilterTypes.slice(),
			filterDone: [true, false],
			darkMode: false,
			frozenRows: [],
			frozenOnly: false,
			showStats: false,
			schemaVersion: 6
		}

		this.handleDarkMode = this.handleDarkMode.bind(this)
		
		this.handleSearch = this.handleSearch.bind(this)
		this.handleFilterType = this.handleFilterType.bind(this)
		this.handleFilterDone = this.handleFilterDone.bind(this)
		this.handleToggleFrozen = this.handleToggleFrozen.bind(this)
		this.handleToggleStats = this.handleToggleStats.bind(this)

		this.handleToggleHave = this.handleToggleHave.bind(this)
		this.handleToggleVariation = this.handleToggleVariation.bind(this)

		this.handleFreeze = this.handleFreeze.bind(this)

		this.handleLoad = this.handleLoad.bind(this)
		this.updateCatalog = this.updateCatalog.bind(this)
		this.simpleItemUpdate = this.simpleItemUpdate.bind(this)
		this.handleSave = this.handleSave.bind(this)

		this.getStats = this.getStats.bind(this)
		this.getItemList = this.getItemList.bind(this)
	}

	handleDarkMode(event) {
		this.setState({
			darkMode: true
		})
	}
		
	handleSearch(event) {
		this.setState({
			searchVal: event.target.value
		})
	}

	handleFilterType(event, type) {
		var filterTypes = this.state.filterTypes
		var idx = filterTypes.indexOf(type)
		if (idx > -1) {
			filterTypes.splice(idx, 1)
		} else {
			filterTypes.push(type)
		}
		this.setState({
			filterTypes: filterTypes
		})
	}

	handleFilterDone(event, val) {
		var filterDone = this.state.filterDone
		var idx = filterDone.indexOf(val)
		if (idx > -1) {
			filterDone.splice(idx, 1)
		} else {
			filterDone.push(val)
		}
		this.setState({
			filterDone: filterDone
		})
	}

	handleToggleFrozen(event) {
		this.setState({
			frozenOnly: !this.state.frozenOnly
		})
	}

	handleToggleStats(event) {
		this.setState({
			showStats: !this.state.showStats
		})
	}
	
	handleToggleHave(event, item) {
		item.have = !item.have
		var variations = {}
		Object.keys(item.vars).forEach(vid => {
			item.vars[vid].have = item.have
			variations[item.vars[vid].vid] = {
				variation: item.vars[vid].variation,
				have: item.vars[vid].have,
				img: item.vars[vid].img
			}
		})

		this.props.dispatch({
			type: 'UPDATE_ITEM',
			payload: {
				name: item.name,
				value: {
					type: item.type,
					have: item.have,
					vars: variations,
					get: item.get
				}
			}
		})
	}
	
	handleToggleVariation(event, item, vid) {
		item.vars[vid].have = !item.vars[vid].have
		item.have = true
		var variations = {}
		Object.keys(item.vars).forEach(vid => {
			if (!item.vars[vid].have) {
				item.have = false
			}
			variations[item.vars[vid].vid] = {
				variation: item.vars[vid].variation,
				have: item.vars[vid].have,
				img: item.vars[vid].img
			}
		})

		this.props.dispatch({
			type: 'UPDATE_ITEM',
			payload: {
				name: item.name,
				value: {
					type: item.type,
					have: item.have,
					vars: variations,
					get: item.get
				}
			}
		})
	}

	handleFreeze(event, val) {
		var frozenRows = this.state.frozenRows
		var idx = frozenRows.indexOf(val)
		if (idx > -1) {
			frozenRows.splice(idx, 1)
		} else {
			frozenRows.push(val)
		}
		this.setState({
			frozenRows: frozenRows
		})
	}
	
	handleLoad(event) {
		var load_file = event.target.files[0]
		var reader = new FileReader()
		reader.onloadend = () => {
			var load_json = JSON.parse(reader.result)

			if (load_json.version < this.state.schemaVersion) {
				load_json = this.updateCatalog(load_json)
			}
	
			this.props.dispatch({
				type: 'LOAD_FILE',
				payload: load_json.catalog
			})
	
			this.forceUpdate()
		}
		reader.readAsText(load_file)
	}

	updateCatalog(update_json) {
		var version = update_json.version
		if (version < 4) {
			var new_catalog = JSON.parse(JSON.stringify(this.props.catalog))  // Simple deep-copy
			var old_catalog = update_json.catalog

			Object.keys(new_catalog).forEach(item_name => {
				if (Array.isArray(old_catalog[item_name].vars)) {
					old_catalog[item_name].vars.forEach(ovar => {
						Object.keys(new_catalog[item_name].vars).forEach(nvid => {
							if (new_catalog[item_name].vars[nvid].variation == ovar.variation) {
								new_catalog[item_name].vars[nvid].have = ovar.have
							}
						})
					})
				} else {
					Object.keys(old_catalog[item_name].vars).forEach(ovid => {
						Object.keys(new_catalog[item_name].vars).forEach(nvid => {
							if (new_catalog[item_name].vars[nvid].variation == old_catalog[item_name].vars[ovid].variation) {
								new_catalog[item_name].vars[nvid].have = old_catalog[item_name].vars[ovid].have
							}
						})
					})
				}
				new_catalog[item_name].have = old_catalog[item_name].have
				if (new_catalog[item_name].have) {
					Object.keys(new_catalog[item_name].vars).forEach(vid => {
						new_catalog[item_name].vars[vid].have = true
					})
				}
			})

			update_json.catalog = new_catalog
			update_json.cookie = false
			update_json.version = 4
			version = 4
		}
		if (version < 5) {
			update_json = {
				catalog: update_json.catalog,
				version: 5
			}
			version = 5
		}
		if (version < 6) {
			var new_catalog = JSON.parse(JSON.stringify(this.props.catalog))  // Simple deep-copy
			var old_catalog = update_json.catalog

			new_catalog = this.simpleItemUpdate(old_catalog, new_catalog)

			update_json = {
				catalog: new_catalog,
				version: 6
			}
			version = 6
		}
		return update_json
	}

	simpleItemUpdate(old_catalog, new_catalog) {
		Object.keys(old_catalog).forEach(item_name => {
			new_catalog[item_name].have = old_catalog[item_name].have
			if (new_catalog[item_name].have) {
				Object.keys(new_catalog[item_name].vars).forEach(vid => {
					new_catalog[item_name].vars[vid].have = true
				})
			} else {
				Object.keys(old_catalog[item_name].vars).forEach(vid => {
					new_catalog[item_name].vars[vid].have = old_catalog[item_name].vars[vid].have
				})
			}
		})
		return new_catalog
	}

	getStats() {
		var item_list = this.getItemList()
		var stats = {}
		stats[''] = {
			total: item_list.length,
			complete: item_list.filter(item => item.have).length
		}
		allFilterTypes.forEach(filterType => {
			var filter_list = item_list.filter(item => item.type == filterType)
			stats[filterType] = {
				total: filter_list.length,
				complete: filter_list.filter(item => item.have).length
			}
		})
		return stats
	}

	handleSave(event) {
		var content = {
			version: this.state.schemaVersion,
			cookie: this.state.saveCookie,
			catalog: this.props.catalog
		}
		var element = document.createElement('a')
		element.href = URL.createObjectURL(new Blob([JSON.stringify(content)], {type:'application/json;charset=utf-8'}))
		element.download = 'catalog.json'
		element.style.display = 'none'
		document.body.appendChild(element)
		element.click()
		document.body.removeChild(element)
	}

	getItemList() {
		return Object.keys(this.props.catalog).map(name => (
			{
				name: name,
				type: this.props.catalog[name].type,
				have: this.props.catalog[name].have,
				vars: Object.keys(this.props.catalog[name].vars).sort().map(vid => (
					{
						vid: vid,
						variation: this.props.catalog[name].vars[vid].variation,
						have: this.props.catalog[name].vars[vid].have,
						img: this.props.catalog[name].vars[vid].img
					}
				)),
				get: this.props.catalog[name].get
			}
		))
	}
	
	render() {
		var item_list = this.getItemList()

		var filtered_items = item_list
		if (this.state.frozenOnly) {
			filtered_items = filtered_items.filter(item => this.state.frozenRows.includes(item.name))
		} else {
			filtered_items = filtered_items.filter(item => item.name.includes(this.state.searchVal) || this.state.frozenRows.includes(item.name))
			filtered_items = filtered_items.filter(item => this.state.filterTypes.includes(item.type) || this.state.frozenRows.includes(item.name))
			filtered_items = filtered_items.filter(item => this.state.filterDone.includes(item.have) || this.state.frozenRows.includes(item.name))
		}

		var sorted_items = filtered_items.sort((a, b) => {
			if (a.name < b.name) {
				return -1
			}
			if (a.name > b.name) {
				return 1
			}
			return 0
		})

		if (this.state.darkMode) {
			return (
				<div style={{backgroundColor: 'black', height: '100vh', width: '100vw'}} />
			)
		}
		return (
			<div>
				<header style={{align: 'center'}}>
					<div style={{marginTop: '15px', fontSize: '200%'}}>Patalog</div>
					<div style={{fontSize: '80%'}}>v2.3.8</div>
					<button style={{marginTop: '15px'}} onClick={this.handleDarkMode}>
						Dark Mode
					</button>

					<div style={{margin: '15px'}}>
						<span>
							Import Catalog:
							<input
								type="file"
								onChange={this.handleLoad}
								style={{marginLeft: '15px'}}
							/>
						</span>

						<span>
							<button onClick={this.handleSave}>
								Export Catalog
							</button>
						</span>
					</div>

					<div style={{margin: '15px'}}>
						<span style={{margin: '5px'}}>
							<input
								type="checkbox"
								checked={this.state.filterTypes.includes('furniture')}
								onChange={event => this.handleFilterType(event, 'furniture')}
							/>
							Furniture
						</span>

						<span style={{margin: '5px'}}>
							<input
								type="checkbox"
								checked={this.state.filterTypes.includes('fashion')}
								onChange={event => this.handleFilterType(event, 'fashion')}
							/>
							Fashion
						</span>

						<span style={{margin: '5px'}}>
							<input
								type="checkbox"
								checked={this.state.filterTypes.includes('misc')}
								onChange={event => this.handleFilterType(event, 'misc')}
							/>
							Misc
						</span>

						<span style={{margin: '5px'}}>
							<input
								type="checkbox"
								checked={this.state.filterTypes.includes('diy')}
								onChange={event => this.handleFilterType(event, 'diy')}
							/>
							DIY
						</span>

						<span style={{margin: '5px'}}>
							<input
								type="checkbox"
								checked={this.state.filterTypes.includes('fish')}
								onChange={event => this.handleFilterType(event, 'fish')}
							/>
							Fish
						</span>

						<span style={{margin: '5px'}}>
							<input
								type="checkbox"
								checked={this.state.filterTypes.includes('bugs')}
								onChange={event => this.handleFilterType(event, 'bugs')}
							/>
							Bugs
						</span>

						<span style={{margin: '5px'}}>
							<input
								type="checkbox"
								checked={this.state.filterTypes.includes('sea')}
								onChange={event => this.handleFilterType(event, 'sea')}
							/>
							Sea Creatures
						</span>
					</div>

					<div style={{margin: '15px'}}>
						<span style={{margin: '5px'}}>
							<input
								type="checkbox"
								checked={this.state.filterDone.includes(true)}
								onChange={event => this.handleFilterDone(event, true)}
							/>
							Complete
						</span>

						<span style={{margin: '5px'}}>
							<input
								type="checkbox"
								checked={this.state.filterDone.includes(false)}
								onChange={event => this.handleFilterDone(event, false)}
							/>
							Incomplete
						</span>
					</div>

					<div style={{margin: '15px'}}>
						<input
							type="checkbox"
							checked={this.state.frozenOnly}
							onChange={event => this.handleToggleFrozen(event)}
						/>
						Frozen Rows Only
					</div>

					<div style={{margin: '15px'}}>
						<input
							type="checkbox"
							checked={this.state.showStats}
							onChange={event => this.handleToggleStats(event)}
						/>
						Show Completion Stats
					</div>

					<div style={{margin: '15px'}}>
						<CompletionStats showStats={this.state.showStats} stats={this.getStats()} />
					</div>

					<div style={{margin: '15px'}}>
						<input
							type="text"
							value={this.state.searchVal}
							onChange={this.handleSearch}
						/>
					</div>

					<div style={{margin: '15px'}}>
						Displaying {sorted_items.length} entries.
					</div>
				</header>
				
				<div style={{display: 'inline-block', margin: '15px'}}>
					<table style={{width: '20%', display: 'inline'}}>
						<thead>
							<th style={{width: '30%', margin: '10px'}}>Name</th>
							<th style={{width: '10%', margin: '10px'}}>Type</th>
							<th style={{width: '10%', margin: '10px'}}>Complete</th>
							<th style={{width: '30%', margin: '10px'}}>Variations</th>
							<th style={{width: '30%', margin: '10px'}}>Availability</th>
							<th style={{width: '10%', margin: '10px'}}>Freeze Row</th>
						</thead>
						<tbody>
							{sorted_items.map(item => (
								<tr>
									<td style={{width: '30%', margin: '10px', border: 'solid'}}>{item.name}</td>
									<td style={{width: '10%', margin: '10px', border: 'solid'}}>{item.type}</td>
									<td style={{width: '10%', margin: '10px', border: 'solid'}}>
										<input
											type="checkbox"
											checked={item.have}
											onChange={event => this.handleToggleHave(event, item)}
										/>
									</td>
									<td style={{width: '30%', margin: '10px', border: 'solid'}}>
										{item.vars.map(vobj => (
											<div>
												<input
													type="checkbox"
													checked={vobj.have}
													onChange={event => this.handleToggleVariation(event, item, vobj.vid)}
												/>
												{vobj.variation}
												<ImageLink link={vobj.img} />
											</div>
										))}
									</td>
									<td style={{width: '30%', margin: '10px', border: 'solid'}}>
										{item.get.split('\n').map((item, key) => (
											<span key={key}>
												{item}
												<br />
											</span>
										))}
									</td>
									<td style={{width: '10%', margin: '10px', border: 'solid'}}>
										<input
											type="checkbox"
											checked={this.state.frozenRows.includes(item.name)}
											onChange={event => this.handleFreeze(event, item.name)}
										/>
									</td>
								</tr>
							))}
						</tbody>
					</table>
				</div>
			</div>
		)
	}
}

function ImageLink(props) {
	if (props.link === '') {
		return <span />;
	}
	return <span>
			   &nbsp;
			   <a
			       href={props.link}
				   target='_blank'>
				       [image]
			   </a>
		   </span>;
}

function CompletionStats(props) {
	if (!props.showStats) {
		return <div />;
	}

	var categoryData = []
	allFilterTypes.forEach(filterType => {
		categoryData.push({
			filterType: filterType,
			complete: props.stats[filterType].complete,
			incomplete: props.stats[filterType].total - props.stats[filterType].complete
		})
	})

	const progressWidth = window.innerWidth * 0.5
	const progressHeight = 40
	const progress = d3.select('#progress').append('svg').attr('viewBox', [0, 0, progressWidth, progressHeight])
	const progressScale = d3.scaleLinear().domain([0, props.stats[''].total]).range([0, progressWidth])
	const completeColor = d3.scaleOrdinal().domain(allFilterTypes).range(d3.schemeDark2)
	const incompleteColor = d3.scaleOrdinal().domain(allFilterTypes).range(d3.schemeSet2)

	function completePosition(filterType) {
		const end = allFilterTypes.indexOf(filterType)
		var x = 0
		for (var i = 0; i < end; i++) {
			const completeCount = props.stats[allFilterTypes[i]].complete
			x += progressScale(completeCount)
		}
		return x
	}

	function incompletePosition(filterType) {
		var x = 0
		for (var i = 0; i < allFilterTypes.length; i++) {
			const completeCount = props.stats[allFilterTypes[i]].complete
			x += progressScale(completeCount)
		}

		const end = allFilterTypes.indexOf(filterType)
		for (var i = 0; i < end; i++) {
			const incompleteCount = props.stats[allFilterTypes[i]].total - props.stats[allFilterTypes[i]].complete
			x += progressScale(incompleteCount)
		}
		return x
	}

	progress.append('g')
				.style('stroke', 'black')
			.selectAll('rect')
			.data(categoryData)
			.join('rect')
				.attr('fill', d => completeColor(d.filterType))
				.attr('x', d => completePosition(d.filterType))
				.attr('y', 0)
				.attr('height', progressHeight)
				.attr('width', d => progressScale(d.complete))
	progress.append('g')
				.style('stroke', 'black')
			.selectAll('rect')
			.data(categoryData)
			.join('rect')
				.attr('fill', d => incompleteColor(d.filterType))
				.attr('x', d => incompletePosition(d.filterType))
				.attr('y', 0)
				.attr('height', progressHeight)
				.attr('width', d => progressScale(d.incomplete))

	const ratioSide = window.innerWidth * 0.3
	const ratio = d3.select('#ratio').append('svg').attr('viewBox', [-ratioSide/2, -ratioSide/2, ratioSide, ratioSide])
	const ratioArc = d3.arc().innerRadius(0).outerRadius(ratioSide/2)
	const ratioPie = d3.pie().value(d => d.complete)(categoryData)
	const ratioColor = d3.scaleOrdinal().domain(ratioPie).range(d3.schemeDark2)

	ratio.append('g')
		 	.style('stroke', 'black')
		.selectAll('path')
		.data(ratioPie)
		.join('path')
			.attr('fill', d => ratioColor(d))
			.attr('d', ratioArc)

	return <div>
		<div style={{margin: '15px'}}>
			<div id="progress" />
			<span>{props.stats[''].complete}/{props.stats[''].total}</span>
		</div>
		<div style={{margin: '15px'}} id="ratio" />
	</div>;
}

const mapStateToProps = state => {
	return { catalog: state }
}

const mapDispatchToProps = dispatch => {
  	return {
    	dispatch
  	}
}

const Catalog = connect(
	mapStateToProps,
	mapDispatchToProps
)(Patalog)

export default Catalog;

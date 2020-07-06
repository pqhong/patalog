import React from 'react';
import { connect } from 'react-redux'

class Patalog extends React.Component {
	constructor() {
		super()
		this.state = {
			searchVal: '',
			filterTypes: ['furniture', 'fashion', 'misc', 'diy'],
			filterDone: [true, false]
		}
		
		this.handleSearch = this.handleSearch.bind(this)
		this.handleFilterType = this.handleFilterType.bind(this)
		this.handleFilterDone = this.handleFilterDone.bind(this)

		this.handleToggleHave = this.handleToggleHave.bind(this)
		this.handleToggleVariation = this.handleToggleVariation.bind(this)

		this.handleLoad = this.handleLoad.bind(this)
		this.handleSave = this.handleSave.bind(this)
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
	
	handleToggleHave(event, item) {
		item.have = !item.have
		item.vars.keys().forEach(variation => {
			item.vars[variation] = item.have
		})

		this.props.dispatch({
			type: 'UPDATE_ITEM',
			payload: {
				name: item.name,
				value: {
					type: item.type,
					have: item.have,
					vars: item.vars
				}
			}
		})
	}
	
	handleToggleVariation(event, item, variation) {
		item.vars[variation] = !item.vars[variation]
		item.have = true
		item.vars.keys().forEach(variation => {
			if (!item.vars[variation]) {
				item.have = false
			}
		})

		this.props.dispatch({
			type: 'UPDATE_ITEM',
			payload: {
				name: item.name,
				value: {
					type: item.type,
					have: item.have,
					vars: item.vars
				}
			}
		})
	}
	
	handleLoad(event) {
		var load_file = event.target.files[0]
		var reader = new FileReader()
		var load_text = reader.readAsText(load_file)
		var load_json = JSON.parse(load_text)
		
		this.props.dispatch({
			'type': 'LOAD_FILE',
			payload: load_json
		})
	}

	handleSave(event) {
		var element = document.createElement('a')
		element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(this.props.catalog))
		element.setAttribute('download', 'catalog.json')

		element.style.display = 'none'
		document.body.appendChild(element)
		element.click()
		document.body.removeChild(element)
	}
	
	render() {
		var item_list = this.props.catalog.keys().map(name => (
			{
				name: name,
				type: this.props.catalog[name].type,
				have: this.props.catalog[name].have,
				vars: this.props.catalog[name].vars
			}
		))

		var filtered_items = item_list
		filtered_items = filtered_items.filter(item => item.name.includes(this.state.searchVal))
		filtered_items = filtered_items.filter(item => this.state.filterTypes.includes(item.type))
		filtered_items = filtered_items.filter(item => this.state.filterDone.includes(item.have))

		var sorted_items = filtered_items.sort((a, b) => {
			if (a.name < b.name) {
				return -1
			}
			if (a.name > b.name) {
				return 1
			}
			return 0
		})

		return (
			<div>
				<header>
					<div>
						<input
							type="file"
							onChange={this.handleLoad}
						>
							Import Catalog
						</input>

						<button onClick={this.handleSave}>
							Export Catalog
						</button>
					</div>

					<div>
						<input
							type="checkbox"
							checked={this.state.filterTypes.includes['furniture']}
							onChange={event => this.handleFilterType(event, 'furniture')}
						>
							Furniture
						</input>

						<input
							type="checkbox"
							checked={this.state.filterTypes.includes['fashion']}
							onChange={event => this.handleFilterType(event, 'fashion')}
						>
							Fashion
						</input>

						<input
							type="checkbox"
							checked={this.state.filterTypes.includes['misc']}
							onChange={event => this.handleFilterType(event, 'misc')}
						>
							Misc
						</input>

						<input
							type="checkbox"
							checked={this.state.filterTypes.includes['diy']}
							onChange={event => this.handleFilterType(event, 'diy')}
						>
							DIY
						</input>
					</div>

					<div>
						<input
							type="checkbox"
							checked={this.state.filterDone.includes[true]}
							onChange={event => this.handleFilterDone(event, true)}
						>
							Complete
						</input>

						<input
							type="checkbox"
							checked={this.state.filterDone.includes[false]}
							onChange={event => this.handleFilterDone(event, false)}
						>
							Incomplete
						</input>
					</div>

					<div>
						<input
							type="text"
							value={this.state.searchVal}
							onChange={this.handleSearch}
						/>
					</div>
				</header>
				
				<table>
					<tbody>
						{sorted_items.map(item => (
							<tr>
								<td>{item.name}</td>
								<td>{item.type}</td>
								<td>
									<input
										type="checkbox"
										checked={item.have}
										onChange={event => this.handleToggleHave(event, item)}
									/>
								</td>
								<td>
									{item.vars.keys().map(variation => (
										<input
											type="checkbox"
											checked={item.vars[variation]}
											onChange={event => this.handleToggleVariation(event, item, variation)}
										>
											{variation}
										</input>
									))}
								</td>
							</tr>
						))}
					</tbody>
				</table>
			</div>
		)
	}
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
import { createStore } from 'redux'

const initialState = require('./catalog.json')['catalog']

const reducer = (state = initialState, action) => {
	switch(action.type) {
		case 'UPDATE_ITEM':
			return {
				...state,
				[action.payload.name]: action.payload.value
			}
		case 'LOAD_FILE':
			return action.payload
		default:
			return state
	}
}

const store = createStore(reducer)

export default store
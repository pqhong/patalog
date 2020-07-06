import React from 'react'
import ReactDOM from 'react-dom'

import { Provider } from 'react-redux'

import './index.css'
import store from './store'
import App from './App.js'

const rootElement = document.getElementById("root")
ReactDOM.render(
	<Provider store={store}>
		<App />
	</Provider>,
	rootElement
)

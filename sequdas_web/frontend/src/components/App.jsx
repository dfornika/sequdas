import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom'

import Login from './Login'
import Header from './Header'
import SequenceRunTable from './SequenceRunTable'

class App extends Component {

    auth = require('../auth')
    
    requireAuth(nextState, replace) {
	if (!this.auth.loggedIn()) {
            replace({
		pathname:'/login/',
		state: {nextPathname: '/'}
            })
	}
    }
    
    render() {
	return (
		<div className="App">
		<Header />
		<Switch>
		<Route exact path='/' component={SequenceRunTable} onEnter={this.requireAuth} />
		<Route exact path='/login/' component={Login} />
		</Switch>
	    </div>
	);
    }
}

export default App;

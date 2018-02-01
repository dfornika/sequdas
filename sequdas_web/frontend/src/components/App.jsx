import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom';

import AuthService from './AuthService';
import Login from './Login';
import Header from './Header';
import SequenceRunTable from './SequenceRunTable';

class App extends Component {

    constructor(props) {
	super(props);
	this.Auth = new AuthService();
    };
    
    requireAuth(nextState, replace) {
	if (!this.Auth.loggedIn()) {
            replace({
		pathname:'/login/',
		state: {nextPathname: '/'}
            });
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

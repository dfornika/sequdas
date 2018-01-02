import React from 'react';
import { render } from 'react-dom';
import { BrowserRouter, Route } from 'react-router-dom'

import App from './App';
import Login from './components/Login'

import registerServiceWorker from './registerServiceWorker';

import './index.css';

var auth = require('./auth')

function requireAuth(nextState, replace) {
    if (!auth.loggedIn()) {
        replace({
            pathname:'/login/',
            state: {nextPathname: '/'}
        })
    }
}

render(
	<BrowserRouter>
	<div>
	<Route exact path='/' component={App} onEnter={requireAuth} />
        <Route path='/login/' component={Login} />
	</div>
	</BrowserRouter>,
    document.getElementById('root')
);

registerServiceWorker();

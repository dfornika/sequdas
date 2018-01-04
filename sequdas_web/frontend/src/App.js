import React, { Component } from 'react';
import { InMemoryCache } from 'apollo-cache-inmemory';
import { createHttpLink } from 'apollo-link-http';
import { setContext } from 'apollo-link-context';

import SequenceRunTable from './components/SequenceRunTable.jsx'
class App extends Component {
    constructor(props) {
	super(props);	
    }
    
    render() {
	return (
		<div className="App">
		<Header />
		<BrowserRouter>
		<Route exact path='/' component={SequenceRunTable} onEnter={requireAuth} />
		<Route exact path='/login/' component={Login} />
		</BrowserRouter>
	    </div>
	);
    }
}

export default App;

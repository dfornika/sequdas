import React, { Component } from 'react';
import { Switch } from 'react-router-dom'

import Header from './components/Header.jsx';
import Nav from './components/Nav.jsx';
import SequenceRunTable from './components/SequenceRunTable.jsx';
import RunSampleChooser from './components/RunSampleChooser.jsx';

class App extends Component {
    constructor(props) {
	super(props);	
    }
    
    render() {
	return (
	    <div className="App">
	      <Header />
	      <Nav />
	      <Switch>
		<Route exact path='/' component={RunSampleChooser} />
		<Route exact path='/login/' component={Login} />
		<Route exact path='/summary/' component={SequenceRunTable} />
	      </Switch>
	    </div>
	);
    }
}

export default App;

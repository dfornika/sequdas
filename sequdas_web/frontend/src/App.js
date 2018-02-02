import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom'

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
	      <BrowserRouter>
		<Route exact path='/' component={RunSampleChooser} onEnter={requireAuth} />
		<Route exact path='/login/' component={Login} />
	      </BrowserRouter>
	    </div>
	);
    }
}

export default App;

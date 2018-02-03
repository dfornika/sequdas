import React, { Component } from 'react';

import { Accordion } from 'semantic-ui-react';

import Nav from './Nav.jsx';

import 'semantic-ui-css/semantic.min.css';
import './RunSampleChooser.css';

class RunSampleChooser extends Component {
    
    render() {

	return (
	    <div>
	      <Nav />
	      <Accordion fluid styled panels={this.props.runs} />
	    </div>
	);
    }
}

export default RunSampleChooser;

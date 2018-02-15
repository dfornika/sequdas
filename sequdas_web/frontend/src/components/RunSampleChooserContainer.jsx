import React, { Component } from 'react';

import withAuth from './withAuth';
import RunSampleChooser from './RunSampleChooser.jsx';


class RunSampleChooserContainer extends Component {
	
    
    render() {
	const data = [
	    { title: 'Run-01', content: 'Details for Run-01'},
	    { title: 'Run-02', content: 'Details for Run-02'}
	];
	
	return (
	    <div>
	      <RunSampleChooser runs={data}/>
	    </div>
	);
    }
}

export default withAuth(RunSampleChooserContainer);

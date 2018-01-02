import React, { Component } from 'react';

import Header from './Header.jsx'
import SequenceRunTable from './SequenceRunTable.jsx'

class RootComponent extends Component {
 
    render() {
	return (
	    [
	      <Header />,
	      <SequenceRunTable />
	    ]
	);
    }
}

export default RootComponent;

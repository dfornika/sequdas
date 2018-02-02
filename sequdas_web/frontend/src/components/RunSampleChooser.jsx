import React, { Component } from 'react';

import { graphql } from 'react-apollo';
import gql from 'graphql-tag';

import { Accordion } from 'semantic-ui-react';

import './RunSampleChooser.css';

class RunSampleChooser extends Component {
 
    render() {
	const allSequenceRuns = gql`{
          sequenceRuns {
            runID
          }
        }`;

	function RunSampleChooser({loading, sequenceRuns }) {
	    if (loading) {
		return <div>Loading...</div>;
	    } else {
		return (
		    <Accordion
		      />
		);
	}
	const RunSampleChooserWithData = graphql(allSequenceRuns, {
	    props: ({data: { loading, sequenceRuns }}) => ({
		loading,
		sequenceRuns
	    })
	})(RunSampleChooser);
	
	return (
	    <RunSampleChooserWithData />
	);
    }
}

export default RunSampleChooser;

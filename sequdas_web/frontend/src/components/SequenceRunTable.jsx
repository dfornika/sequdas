import React, { Component } from 'react';

import { graphql } from 'react-apollo';
import gql from 'graphql-tag';

import ReactTable from 'react-table';
import 'react-table/react-table.css';
import moment from 'moment';

import withAuth from './withAuth.jsx';
import Nav from './Nav.jsx';
import './SequenceRunTable.css';

class SequenceRunTable extends Component {

    render() {
	const allSequenceRuns = gql`{
            sequenceRuns {
              runId 
              runStartTime
              clusterDensity 
              clustersPfPercent
              samples {
                sampleName
                index1I7Seq
                readsIdentifiedPfPercent
              }
            }
          }`;

	function SequenceRunTable({ loading, sequenceRuns }) {
	    if (loading) {
		return <div>Loading</div>;
	    } else {
		return (
		    <ReactTable
		      columns={[
			  {
			      Header: 'Run ID',
			      accessor: 'runId'
			  }, {
			      id: 'runStartTime',
			      Header: 'Start Time',
			      accessor: (row) => moment(row.runStartTime).format("h:mm:ss a MMM DD, YYYY")
			  }, {
			      Header: 'Cluster Density',
			      accessor: 'clusterDensity',
			      sortable: true
			  }, {
			      Header: 'Clusters PF (%)',
			      accessor: 'clustersPfPercent'
			  }
		      ]}
		      className="-striped -highlight"
		      data={sequenceRuns}
		      defaultPageSize={10}
		      SubComponent={row => {
			  return (
			      <div style={{ padding: "20px" }}>
				<ReactTable
				  data={row.original.samples}
				  columns={[
				      {
					  Header: 'Sample Name',
					  accessor: 'sampleName'
				      }, {
					  Header: 'Index Seq',
					  accessor: 'index1I7Seq'
				      }, {
					  Header: 'Reads Identified (%)',
					  accessor: 'readsIdentifiedPfPercent',
					  sortable: true
				      }
				  ]}
				  defaultPageSize={8}
				  showPagination={true}
			      />
			      </div>
			  );
		      }}
		    />
		);
	    }
	}
	
	const SequenceRunTableWithData = graphql(allSequenceRuns, {
	    props: ({data: { loading, sequenceRuns }}) => ({
		loading,
		sequenceRuns
	    })
	})(SequenceRunTable);
	
	return (
	    <div>
	      <Nav email={this.props.user.email}/>
	      <SequenceRunTableWithData />
	    </div>
	);
    }
}

export default withAuth(SequenceRunTable);

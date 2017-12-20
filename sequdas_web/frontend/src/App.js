import React, { Component } from 'react';
import { InMemoryCache } from 'apollo-cache-inmemory';
import { createHttpLink } from 'apollo-link-http';
import { setContext } from 'apollo-link-context';
import ApolloClient from 'apollo-client';
import { ApolloProvider } from 'react-apollo'
import { graphql } from 'react-apollo';
import gql from 'graphql-tag'
import ReactTable from 'react-table'

import './App.css';
import 'react-table/react-table.css'

class App extends Component {
    constructor(props) {
	super(props);
	
	const httpLink = createHttpLink({
	    uri: 'http://localhost:8000/graphql/',
	    credentials: 'include',
	});

	const authLink = setContext((_, { headers }) => {
	    // get the authentication token from local storage if it exists
	    const token = localStorage.getItem('token');
	    // return the headers to the context so httpLink can read them
	    return {
		headers: {
		    ...headers,
		    authorization: token ? `JWT ${token}` : null,
		}
	    }
	});
	
	this.client = new ApolloClient({
	    link: authLink.concat(httpLink),
	    cache: new InMemoryCache(),
	});
    }
    
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
        }`
	
	function SequenceRunList({ loading, sequenceRuns }) {
	    console.log(sequenceRuns)
	    if (loading) {
		return <div>Loading</div>;
	    } else {
		return (
		      <ReactTable
			columns={[
			    {
				Header: 'Run ID',
				accessor: 'runId',
			    }, {
				Header: 'Start Time',
				accessor: 'runStartTime',
			    }, {
				Header: 'Cluster Density',
				accessor: 'clusterDensity',
				sortable: true,
			    }, {
				Header: 'Clusters PF (%)',
				accessor: 'clustersPfPercent',
			    }
			]}
		    className="-striped -highlight"
		    data={sequenceRuns}
		    defaultPageSize={10}
		    SubComponent={row => {
			console.log(row)
			return (
				<div style={{ padding: "20px" }}>
				<ReactTable
			    data={row.original.samples}
			    columns={[
				{
				    Header: 'Sample Name',
				    accessor: 'sampleName',
				}, {
				    Header: 'Index Seq',
				    accessor: 'index1I7Seq',
				}, {
				    Header: 'Reads Identified (%)',
				    accessor: 'readsIdentifiedPfPercent',
				    sortable: true,
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

	const SequenceRunListWithData = graphql(allSequenceRuns, {
	    props: ({data: { loading, sequenceRuns }}) => ({
		loading,
		sequenceRuns
	    }),
	})(SequenceRunList);
	
	return (
	    <div className="App">
	      <ApolloProvider client={this.client}>
		<SequenceRunListWithData />
	      </ApolloProvider>
	    </div>
	);
    }
}

export default App;

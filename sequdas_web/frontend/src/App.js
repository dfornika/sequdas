import React, { Component } from 'react';
import { InMemoryCache } from 'apollo-cache-inmemory';
import { createHttpLink } from 'apollo-link-http';
import { setContext } from 'apollo-link-context';
import ApolloClient from 'apollo-client';
import { ApolloProvider } from 'react-apollo'

import SequenceRunTable from './components/SequenceRunTable.jsx'
import Header from './components/Header.jsx'

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
	
	return (
	    <div className="App">
	      <ApolloProvider client={this.client}>
		<Header />
		<SequenceRunTable />
	      </ApolloProvider>
	    </div>
	);
    }
}

export default App;

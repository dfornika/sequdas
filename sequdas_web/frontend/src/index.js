import React from 'react';
import { render } from 'react-dom';
import { BrowserRouter } from 'react-router-dom'

import ApolloClient from 'apollo-client';
import { ApolloProvider } from 'react-apollo'
import { InMemoryCache } from 'apollo-cache-inmemory';
import { createHttpLink } from 'apollo-link-http';
import { setContext } from 'apollo-link-context';

import App from './components/App';


import registerServiceWorker from './registerServiceWorker';

import './index.css';

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
	    Authorization: token ? `JWT ${token}` : null,
	}
    }
});

const client = new ApolloClient({
    link: authLink.concat(httpLink),
    cache: new InMemoryCache(),
});

render(
	<BrowserRouter>
	<ApolloProvider client={client}>
	<App />
	</ApolloProvider>
	</BrowserRouter>
	,document.getElementById('root')
);

registerServiceWorker();

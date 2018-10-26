import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom';
import { BrowserRouter } from 'react-router-dom';

import ApolloClient from 'apollo-client';
import { ApolloProvider } from 'react-apollo';
import { InMemoryCache } from 'apollo-cache-inmemory';
import { createHttpLink } from 'apollo-link-http';
import { setContext } from 'apollo-link-context';

import Login from './LoginIRIDA';
import Header from './Header';
import SequenceRunTable from './SequenceRunTable';
import RunSampleChooserContainer from './RunSampleChooserContainer.jsx';

const httpLink = createHttpLink({
    uri: 'http://localhost:8000/graphql/',
    credentials: 'include'
});

const authLink = setContext((_, { headers }) => {
    // get the authentication token from local storage if it exists
    const token = localStorage.getItem('id_token');
    // return the headers to the context so httpLink can read them
    return {
	headers: {
	    ...headers,
	    Authorization: token ? `JWT ${token}` : null
	}
    };
});

const client = new ApolloClient({
    link: authLink.concat(httpLink),
    cache: new InMemoryCache()
});

class App extends Component {
    
    render() {
	return (
	      <BrowserRouter>
		<ApolloProvider client={client}>
		  <div>
		    <Header />
		    <Switch>
		      <Route exact path='/' component={SequenceRunTable} />
		      <Route exact path='/login/' component={Login} />
		      <Route exact path='/summary/' component={RunSampleChooserContainer} />
		    </Switch>
		  </div>
		</ApolloProvider>
	      </BrowserRouter>
	);
    }
}

export default App;

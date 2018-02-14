import React, { Component } from 'react';
import PropTypes from 'prop-types';

import AuthService from './AuthService.js';

import './Logout.css';

class Logout extends Component {
    
    constructor(props) {
	super(props);
	this.Auth = new AuthService();
	this.handleLogout = this.handleLogout.bind(this);
    };

    handleLogout = () => {
	this.Auth.logout()
	    .then(() =>
		  this.context.client.resetStore()
		 )
	    .catch(err =>
		   console.log('Logout failed.', err)
		  );
	this.context.router.history.push('/login');
    };
    
    static contextTypes = {
	client: () => PropTypes.isRequired,
	router: () => PropTypes.isRequired
    }
    
    
    
    render() {
        return (
            <button type="button" className="form-submit logout" onClick={this.handleLogout}>Logout</button>
        );
    }
}

export default Logout;

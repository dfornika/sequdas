import React, { Component } from 'react';
import PropTypes from 'prop-types';

import AuthService from './AuthService';

import './Logout.css';

class Logout extends Component {

    constructor(props) {
	super(props);
	this.Auth = new AuthService();
    };
    
    static contextTypes = {
	router: () => PropTypes.isRequired
    }
    
    handleLogout() {
	this.Auth.logout();
	this.context.router.history.push('/login');
    }
    
    render() {
        return (
            <button type="button" className="form-submit" onClick={this.handleLogout.bind(this)}>Logout</button>
        );
    }
}

export default Logout;

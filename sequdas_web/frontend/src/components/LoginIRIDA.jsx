import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Button } from 'react-bootstrap';
import AuthService from './AuthServiceIRIDA';

import './Login.css';

class Login extends Component {

    constructor(props){
	super(props);
	this.state = {
	    username: '',
	    password: ''
	};
	
	this.Auth = new AuthService();
	this.handleSubmit = this.handleSubmit.bind(this);
    }

    login() {
	this.props.auth.login();
    }

    static contextTypes = {
	router: () => PropTypes.isRequired
    }

    componentWillMount(){
	if(this.Auth.loggedIn()) {
            this.props.history.replace('/');
	}
    }
    
    handleSubmit(e) {
	e.preventDefault();
        this.Auth.login(this.state.username, this.state.password)
	    .then(response => {
		this.props.history.push(`/`);
	    })
	.catch(err =>{
                alert(err);
        });
    }
    
    render() {
        return (
	    <div className="center">
              <div className="card">
		<h1>Login</h1>
                <Button className="form-submit" type="submit" onClick={this.login.bind(this)}>Login with IRIDA</Button>
	      </div>
	    </div>
        );
    }
}

export default Login;

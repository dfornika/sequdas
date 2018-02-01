import React, { Component } from 'react';
import PropTypes from 'prop-types';

import AuthService from './AuthService';

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
              <form onSubmit={this.handleSubmit}>
		<input
		  className="form-item"
		  value={this.state.username}
		  onChange={(e) => this.setState({ username: e.target.value })}
		  type="text"
		  placeholder="username"
		/>
		<input
		  className="form-item"
		  value={this.state.password}
		  onChange={(e) => this.setState({ password: e.target.value })}
		  type="password"
		  placeholder="password"
		/>
                <button className="form-submit" type="submit">Login</button>
              </form>
	      </div>
	    </div>
        );
    }
}

export default Login;

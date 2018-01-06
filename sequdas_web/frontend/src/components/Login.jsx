import React, { Component } from 'react'
import PropTypes from 'prop-types'
import axios from 'axios'

import './Login.css'

class Login extends Component {
    constructor(props){
	super(props);
	this.state = {
	    username: '',
	    password: ''
	}
	this.handleSubmit = this.handleSubmit.bind(this);
    }

    static contextTypes = {
	router: () => PropTypes.isRequired
    }

    getToken(username, password) {
	axios({
	    method: 'post',
	    url: 'http://localhost:8000/api-token-auth/',
	    data: {
		username: username,
		password: password
	    }
	}).then(function(response) {
	    console.log(response)
            localStorage.setItem('token', response.data.token)
	});
    }
    
    handleSubmit(e) {
        e.preventDefault()
        this.getToken(this.state.username, this.state.password)
	this.props.history.push(`/`)
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
        )    
    }
}

export default Login;

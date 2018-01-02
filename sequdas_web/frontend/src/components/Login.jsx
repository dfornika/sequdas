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
    
    handleChangeUsername(event) {
	this.setState({username: event.target.value})
    }

    handleChangePassword(event) {
	this.setState({password: event.target.value})
    }
    
    handleSubmit(e) {
        e.preventDefault()
        this.getToken(this.state.username, this.state.password)
    }

    
    
    render() {
        return (
	    <div class="wrapper">
            <form onSubmit={this.handleSubmit}>
            <input type="text" placeholder="username" value={this.state.username} onChange={this.handleChangeUsername.bind(this)} />
            <input type="password" placeholder="password" value={this.state.password} onChange={this.handleChangePassword.bind(this)} />
            <button type="submit">Login</button>
            </form>
	    </div>
        )    
    }
}

export default Login;
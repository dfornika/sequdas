import React, { Component } from 'react'
import PropTypes from 'prop-types'

import './Logout.css'

class Logout extends Component {

    static contextTypes = {
	router: () => PropTypes.isRequired
    }
    
    constructor(props, context) {
	super(props, context);
    }
    
    handleLogout() {
        localStorage.removeItem("token")
	this.context.router.history.push('/login')
    }
    
    render() {
        return (
	    <div>
              <button type="button" className="form-submit" onClick={this.handleLogout.bind(this)}>Logout</button>
	    </div>
        )
    }
}

export default Logout;

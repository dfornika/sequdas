import React, { Component } from 'react';
import { Link } from 'react-router-dom'; 

import './Nav.css';

class Nav extends Component {
 
    render() {
	return (
	    <nav>
	      <ul>
		<li><Link to='/'>Home</Link></li>
		<li><Link to='/summary'>Summary</Link></li>
	      </ul>
	      <div className="username">{this.props.email}</div>	      
	    </nav>
	);
    }
}

export default Nav;

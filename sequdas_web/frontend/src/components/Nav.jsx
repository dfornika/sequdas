import React, { Component } from 'react';
import { Link } from 'react-router-dom'; 
import Logout from './Logout.jsx';

import './Nav.css';

class Nav extends Component {
 
    render() {
	return (
	    <nav>
	      <ul>
		<li><Link to='/'>Home</Link></li>
		<li><Link to='/summary'>Summary</Link></li>
		<li><Link to='/testing'>Testing</Link></li>
	      </ul>
	      <div className="username">{this.props.email}</div>
	      <Logout/>
	    </nav>
	);
    }
}

export default Nav;

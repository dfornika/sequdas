import React, { Component } from 'react';

import './Header.css';
import Logout from './Logout';

class Header extends Component {
 
    render() {
	return (
	    <header>
	      <div className="header title">
		<h1>SeqUDAS</h1>
	      </div>
	      <Logout />
	    </header>
	);
    }
}

export default Header;

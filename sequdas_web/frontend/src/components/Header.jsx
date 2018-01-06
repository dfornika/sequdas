import React, { Component } from 'react';

import './Header.css';
import Logout from './Logout'

class Header extends Component {
 
    render() {
	return (
	    <header>
	      <h1>SeqUDAS</h1>
	      <Logout />
	    </header>
	);
    }
}

export default Header;

import axios from 'axios'

export function login(username, pass) {
    this.getToken(username, pass);
}
    
export function logout() {
    delete localStorage.token
}

export function loggedIn() {
    return !!localStorage.token
}

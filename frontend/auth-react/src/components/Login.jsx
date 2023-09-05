import React from 'react'
import './Login.css'

function Login() {
  return (
    <div className="login">
        
        <form className="login-container">
            <label htmlFor='username'>UserName</label>
            <input type='text' name="username" id="username"></input>
            <label htmlFor='password'>Password</label>
            <input type='password' name="password" id="password"></input>
        </form>
        
    </div>
  )
}

export default Login
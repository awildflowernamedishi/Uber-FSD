import React from 'react'
import './NavBar.css'

function NavBar() {
  return (
    <div className="navBar">
        <div className= "navBar__left">
          <ul>Uber</ul>
          <ul>Company</ul>
          <ul>Safety</ul>
          <ul>Help</ul>
          <ul>My Trips</ul>
        </div>
        <div className="navBar__right">
          <button className="navBar__login_button">Log in</button>
          <button className="navBar__signup_button">Sign Up</button>
        </div>
    </div>
  )
}

export default NavBar
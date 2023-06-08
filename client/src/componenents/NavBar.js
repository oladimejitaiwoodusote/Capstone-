import React from 'react'
import {NavLink, useNavigate} from 'react-router-dom'
import './NavBar.css'


function NavBar() {
    const navigate = useNavigate()

    function handleClick(e){
        e.preventDefault()
        navigate('profile_page')
    }

    function handleFeed(e){
      e.preventDefault()
      navigate('/main_feed')
    }

    function handleDiscoveries(e){
      e.preventDefault()
      navigate('/discoveries')
    }

    function handleSettings(e){
      e.preventDefault()
      navigate('/settings')
    }
    
  return (
    <div className="navbar-wrapper">
        <nav className="navbar">
            <NavLink className="navbar-link" onClick={handleFeed} activeClassName="active-link">Main Feed</NavLink>
            <NavLink className="navbar-link" onClick={handleClick} activeClassName="active-link">My Profile</NavLink>
            <NavLink className="navbar-link" onClick={handleDiscoveries} activeClassName="active-link">Discover Page</NavLink>
            <NavLink className="navbar-link" onClick={handleSettings} activeClassName="active-link">Settings</NavLink>
        </nav>
    </div>
  )
}

export default NavBar
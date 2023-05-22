import React from 'react'
import {NavLink, useNavigate} from 'react-router-dom'

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
    
  return (
    <div>
        <nav>
            <NavLink onClick={handleFeed}>Main Feed</NavLink>
            <NavLink onClick={handleClick}>My Profile</NavLink>
            <NavLink>Discover Page</NavLink>
        </nav>
    </div>
  )
}

export default NavBar
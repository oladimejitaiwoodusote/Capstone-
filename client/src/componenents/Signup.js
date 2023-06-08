import React, {useEffect, useState} from 'react'
import {useNavigate} from 'react-router-dom'
import './Signup.css'

function Signup({attemptSignup, currentUser}) {
    const navigate = useNavigate()
    const [formData, setForm] = useState(
        {
            username: "",
            email: "",
            password: "",
        }
    )

    function changeHandler(e){
        setForm({...formData, [e.target.name]: e.target.value})
    }

    function submitHandler(e){
        e.preventDefault()
        attemptSignup(formData)
    }

    useEffect(()=>{
        if (currentUser){
            navigate('/profile_page')
        }
    })

    function clickHandler(){
        navigate('/')
    }

  return (
    <div className='signup-container'>
        <div className='signup-only'>
            <h1 className='signup-logo'>Collectorsgramm</h1>
            <form className='signup-form' onSubmit={submitHandler}>
                <input className='signup-input-field' name="email" placeholder='Email' onChange={changeHandler} value={formData.email}/>
                <input className='signup-input-field' name="username" placeholder='Username' onChange={changeHandler} value={formData.username}/>
                <input className='signup-input-field' name="password" placeholder='Password' onChange={changeHandler} value={formData.password}/>
                <input className='signup-submit-button' type="submit" value='Sign up'/>
            </form>
        </div>
        <div className='signup-login-only'>
            <p className='signup-login-text'>Have an account?
                <button className='signup-login-button' onClick={clickHandler}>Log in</button>
            </p>
        </div>
    </div>
  )
}

export default Signup
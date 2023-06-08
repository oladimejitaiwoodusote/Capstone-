import React, {useState, useEffect} from 'react'
import {useNavigate} from "react-router-dom"
import './Login.css'

function Login({attemptLogin, currentUser}) {
    
    const navigate = useNavigate()
    const [formData, setForm] = useState(
        {
            username: "",
            password: ""
        }
    )

    useEffect(()=> {
        if(currentUser){
            navigate('/main_feed')
    }
       
    },[currentUser])

    function changeHandler(e){
        setForm({...formData, [e.target.name]: e.target.value})
    }

    function submitHandler(e){
        e.preventDefault()
        attemptLogin(formData)
    }

    function clickHandler(e){
        navigate("/signup")
    }

    return (
    <div className='login-container'>
        <div className='login-only'>
            <h1 className='login-logo'>Collectorsgramm</h1>
            <form className='login-form' onSubmit={submitHandler}>
                <input className="login-input-field" name='username' placeholder='Username' onChange={changeHandler} value={formData.username}/>
                <input className="login-input-field" name='password' placeholder='Password' onChange={changeHandler} value={formData.password}/>
                <input className="login-submit-button" type='submit' value="Log in"/>
            </form>
        </div>
        <div className='login-signup-only'>
            <p className="login-signup-text">Don't have an account? 
                <button className="login-signup-button" onClick={clickHandler}>Signup</button>
            </p>
        </div>
    </div>
  )
}

export default Login
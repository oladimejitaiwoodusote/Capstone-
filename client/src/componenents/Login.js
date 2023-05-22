import React, {useState, useEffect} from 'react'
import {useNavigate} from "react-router-dom"

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
            navigate('/profile_page')
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
    <div>
        <h1>Login</h1>
        <form onSubmit={submitHandler}>
            <input name='username' placeholder='Enter username' onChange={changeHandler} value={formData.username}/>
            <input name='password' placeholder='Enter password' onChange={changeHandler} value={formData.password}/>
            <input type='submit'/>
        </form>
        <h1>Don't have an account? Signup</h1>
        <button onClick={clickHandler}>Signup</button>
    </div>
  )
}

export default Login
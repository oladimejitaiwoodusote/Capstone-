import React, {useEffect, useState} from 'react'
import {useNavigate} from 'react-router-dom'

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

    console.log(currentUser)

  return (
    <div>
        <h1>Create Account</h1>
        <form onSubmit={submitHandler}>
            <input name="username" placeholder='Enter username' onChange={changeHandler} value={formData.username}/>
            <input name="email" placeholder='Enter email' onChange={changeHandler} value={formData.email}/>
            <input name="password" placeholder='Enter password' onChange={changeHandler} value={formData.password}/>
            <input type="submit"/>
        </form>
    </div>
  )
}

export default Signup
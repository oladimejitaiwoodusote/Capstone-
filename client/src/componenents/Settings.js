import React, {useState} from 'react'
import { useNavigate } from 'react-router-dom'
import './Settings.css'

function Settings({attemptUpdate}) {
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
        console.log(formData)
        attemptUpdate(formData)
        navigate('/profile_page')
    }
  return (
    <div className='settings-container'>
        Update Information     
        <form  className='settings-form' onSubmit={submitHandler}>
            <input className='settings-input-field' onChange={changeHandler} name="email" placeholder='Email'></input>
            <input className='settings-input-field' onChange={changeHandler} name="username" placeholder='Username'></input>
            <input className='settings-input-field' onChange={changeHandler} name="password" placeholder='Password'></input>
            <input className='settings-submit-button' type="submit" value='Update Info'></input>
        </form>
    </div>
  )
}

export default Settings
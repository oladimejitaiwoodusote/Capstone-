import React, {useState, useEffect} from 'react'

function Login({attemptLogin}) {

    const [formData, setForm] = useState(
        {
            username: "",
            password: ""
        }
    )

    function changeHandler(e){
        setForm({...formData, [e.target.name]: e.target.value})
    }

    function submitHandler(e){
        e.preventDefault()
        attemptLogin(formData)
    }

    return (
    <div>
        <h1>Login</h1>
        <form onSubmit={submitHandler}>
            <input name='username' placeholder='Enter username' onChange={changeHandler} value={formData.username}/>
            <input name='password' placeholder='Enter password' onChange={changeHandler} value={formData.password}/>
            <input type='submit'/>
        </form>
    </div>
  )
}

export default Login
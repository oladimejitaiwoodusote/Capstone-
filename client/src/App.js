import './App.css';
import {Routes, Route} from "react-router-dom"
import Login from './componenents/Login';
import {useState} from "react"
import Signup from './componenents/Signup';


function App() {
  const [currentUser, setUser] = useState(null)

  function handleLogin(userdata){
    fetch('/login',{
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        'Accepts': 'application/json'
      },
      body: JSON.stringify(userdata)
    })
    .then(response => {
      if(response.ok){
        response.json()
        .then(data => setUser(data))
      }
      else {
        response.json()
        .then(data => alert(data.message))
      }
    })
  }

  function handleSignup(userdata){
    fetch('/signup',{
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accepts': 'application/json'
      },
      body: JSON.stringify(userdata)
    })
    .then(response => response.json())
    .then(data => setUser(data))
  }

  return (
    <>
      <Routes>
        <Route path = "login" element ={<Login attemptLogin={handleLogin}/>}/>
        <Route path = "signup" element ={<Signup attemptSignup={handleSignup}/>} />
      </Routes>
    </>
  );
}

export default App;

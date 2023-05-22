import './App.css';
import {Routes, Route} from "react-router-dom"
import Login from './componenents/Login';
import {useState, useEffect} from "react"
import Signup from './componenents/Signup';
import ProfilePage from './componenents/ProfilePage';
import AboutPage from './componenents/AboutPage';
import NavBar from './componenents/NavBar';
import MainFeed from './componenents/MainFeed';

function App() {
  const [currentUser, setUser] = useState(null)

  useEffect(()=>{
    fetch('/check_session')
    .then(response => {
      if(response.ok){
        response.json()
        .then(data => setUser(data))
      }
    })
  },[])

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

  function handleLogout(){
    setUser(null)
    fetch('/logout',{
      method: "DELETE"
    })
  }


  return (
    <>
      <NavBar/>
      <Routes>
        <Route path = "/" element ={<Login attemptLogin={handleLogin} currentUser={currentUser}/>}/>
        <Route path ="main_feed" element={<MainFeed/>} currentUser={currentUser}/>     
        <Route path = "signup" element ={<Signup attemptSignup={handleSignup} currentUser={currentUser}/>}/>
        <Route path = "profile_page" element={<ProfilePage logout={handleLogout} currentUser={currentUser}/>} />
        <Route path ="aboutpage" element={<AboutPage/>}/>
      </Routes>
    </>
  );
}

export default App;

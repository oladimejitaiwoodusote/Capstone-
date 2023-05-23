import React, {useState, useEffect} from 'react'
import Collection from './Collection' 
import {useNavigate} from 'react-router-dom'

function ProfilePage({currentUser, logout}) {
    const [records, setRecords] = useState([])
    const navigate = useNavigate()
    const [followers, setFollowers] = useState([])
    const [followings, setFollowings] = useState([])

    useEffect(()=>{
        if (currentUser){
        fetch(`users_records/${currentUser.id}`)
        .then(response => response.json())
        .then(data => setRecords(data))
        }
        else{
            navigate('/')
        }
    },[currentUser])

    useEffect(()=>{
        if(currentUser){
            fetch(`users/${currentUser.id}`)
            .then(response => response.json())
            .then(data => {
                setFollowers(data["followers"])
                setFollowings(data["followings"])
            })
        }
    },[currentUser])
    
    const [showForm, setShow] = useState(false) 
    const [recordForm, setRecord] = useState({
        title: "",
        artist: "",
        year: "",
        genre: "",
        cover_art: ""
    })
    
    function handleForm(){
        setShow(!showForm)
    }
    
    function changeHandler(e){
        setRecord({...recordForm,[e.target.name]:e.target.value})
    }
    
    function submitHandler(e){
        e.preventDefault()
        console.log(recordForm)
        console.log(currentUser.id)
        fetch('/record',{
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Accepts': 'application/json'
            },
            body: JSON.stringify(recordForm)    
        })
        .then(response => response.json())
        .then(data => setRecords([...records,data]))
        setRecord({
            title: "",
            artist: "",
            year: "",
            genre: "",
            cover_art: ""
        })
    }

    function handleDelete(id){
        const latestRecords = records.filter(record => record.id !== id )
        setRecords(latestRecords)
    }

    function handleEdit(editedRecord){
        console.log(editedRecord)
        const latestRecords = records.map(record => {
            if(record.id === editedRecord.id){
                return editedRecord
            }
            else{
                return record
            }
        })
        setRecords(latestRecords)
    }
    
    if(currentUser){
        
        return (
            <div>
        <button onClick={logout}>Logout</button>
        <button onClick={handleForm}>Add New Record</button>
        <h1>Welcome {currentUser.username} </h1>   
        <div>
            <h1>{followers.length} Followers</h1>
            <h1>{followings.length} Following</h1>
        </div> 
        {showForm? 
                    <div>
                        <h3>Enter record details</h3>
                        <form onSubmit={submitHandler}>
                            <input value={recordForm.title} onChange={changeHandler} name= "title" placeholder='Enter title'/>
                            <input value={recordForm.artist} onChange={changeHandler} name= "artist" placeholder='Enter artist'/>
                            <input value={recordForm.year} onChange={changeHandler} name= "year" placeholder='Enter year'/>
                            <input value={recordForm.genre} onChange={changeHandler} name= "genre" placeholder='Enter genre'/>
                            <input value={recordForm.cover_art} onChange={changeHandler} name= "cover_art" placeholder='Enter cover art'/>
                            <input type='submit'/>
                        </form>
                   </div>
        :null}
        <Collection onEdit={handleEdit} handleDelete={handleDelete} records ={records} currentUser={currentUser}/>
    </div>
    )}

    else{
        return "LOADING..."
    }
}

export default ProfilePage
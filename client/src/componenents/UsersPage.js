import React, {useEffect, useState} from 'react'
import {useParams} from 'react-router-dom'
import Record from './Record'
import {Avatar} from '@mui/material'
import './UsersPage.css'


function UsersPage({currentUser}) {
    const params = useParams()
    const [usersRecords, setUsersRecords] = useState([])
    const [userDetails, setDetails] = useState(null)
    const [usersFollowers, setUsersFollowers] = useState([])
    const [usersFollowings, setUsersFollowings] = useState([])
   
    useEffect(()=>{
        fetch(`/users_records/${params.id}`)
        .then(response => response.json())
        .then(data => setUsersRecords(data))
    },[])

    useEffect(()=> {
      fetch(`/users_details/${params.id}`)
      .then(response=>response.json())
      .then(data => setDetails(data))
    },[])

    useEffect(()=>{
      fetch(`/users/${params.id}`)
      .then(response=>response.json())
      .then(data => {
        setUsersFollowers(data["followers"])
        setUsersFollowings(data["followings"])
      })
    },[])

    const profilesRecords = usersRecords.map(record => {
        return <Record key={record.id} record={record} user={currentUser} />
    })

    const followersIDs = usersFollowers.map(follower => {
      return follower.id
    })

    function handleUnfollow(){
      fetch(`/users_unfollow/${params.id}`)
      .then(response => response.json())
      .then(data => {
        const currentFollowers = usersFollowers.filter(follower => follower.id != data.id)
        setUsersFollowers(currentFollowers)
      })
    }

    function handleFollow(){
      fetch(`/users_follow/${params.id}`)
      .then(response => response.json())
      .then(data => {
        setUsersFollowers([...usersFollowers, data])
      })
    }

    if(userDetails && currentUser){
  return (
    <div>
        <div className="users-page-info">
        <Avatar
                className="record_avatar"
                alt = "Avatar"
                src = {userDetails.avatar}
                />   
          <h1>{userDetails.username}</h1>
          <h1>{usersFollowers.length} Followers</h1>
          <h1>{usersFollowings.length} Following</h1>
          {followersIDs.includes(currentUser.id)? <button className="users-page-button" onClick={handleUnfollow}>Unfollow</button>: <button className="users-page-button" onClick={handleFollow}>Follow</button>}
        </div>
        {profilesRecords}
    </div>
  )}
  else {
    return "LOADING...."
  }
}

export default UsersPage
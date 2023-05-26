import React, {useEffect, useState} from 'react'
import {useParams} from 'react-router-dom'
import Record from './Record'
import {Avatar} from '@mui/material'

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

    console.log(usersRecords)
    const profilesRecords = usersRecords.map(record => {
        return <Record record={record} user={currentUser} />
    })
    console.log(profilesRecords)

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

    console.log(followersIDs)

    if(userDetails && currentUser){
  return (
    <div>
        <div>
        <Avatar
                className="record_avatar"
                alt = "Avatar"
                src = {userDetails.avatar}
                />   
          <h1>{userDetails.username}</h1>
          <h1>{usersFollowers.length} Followers</h1>
          <h1>{usersFollowings.length} Following</h1>
          {followersIDs.includes(currentUser.id)? <button onClick={handleUnfollow}>Unfollow</button>: <button onClick={handleFollow}>Follow</button>}
        </div>
        {profilesRecords}
    </div>
  )}
  else {
    return "LOADING...."
  }
}

export default UsersPage
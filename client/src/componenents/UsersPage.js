import React, {useEffect, useState} from 'react'
import {useParams} from 'react-router-dom'
import Record from './Record'

function UsersPage({currentUser}) {
    const params = useParams()
    const [usersRecords, setUsersRecords] = useState([])
    console.log(params)
    const empty = []

    useEffect(()=>{
        fetch(`/users_records/${params.id}`)
        .then(response => response.json())
        .then(data => setUsersRecords(data))
    },[])

    console.log(usersRecords)
    const profilesRecords = usersRecords.map(record => {
        return <Record record={record} user={currentUser} />
    })
    console.log(profilesRecords)
    
  return (
    <div>UsersPage
        {profilesRecords}
    </div>
  )
}

export default UsersPage
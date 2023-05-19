import React from 'react'
import Collection from './Collection'

function ProfilePage({currentUser}) {

    if(currentUser){

    return (
    <div>
        <h1>Welcome {currentUser.username} </h1>    
        <Collection currentUser={currentUser}/>

    </div>
    )
    }

    else{
        return "LOADING..."
    }

}

export default ProfilePage
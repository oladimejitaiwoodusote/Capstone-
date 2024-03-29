import React, {useState, useEffect} from 'react'
import Record from './Record'

function MainFeed({currentUser}) {
  const [feed, setFeed] = useState([])
  
  useEffect(()=>{
    if (currentUser){
    fetch(`/feed/${currentUser.id}`)
    .then(response => response.json())
    .then(data => setFeed(data))
    }
  },[currentUser])

  const Feed = feed.map(record => {
    return <Record key={record.id} user = {currentUser} record={record}/>
  })

  return (
    <div>
        {Feed}
    </div>
  )
}

export default MainFeed
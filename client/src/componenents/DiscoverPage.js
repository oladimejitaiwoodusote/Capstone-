import React, { useEffect, useState } from 'react'
import Record from './Record'

function DiscoverPage({currentUser}) {
    const [discoveries, setDiscoveries] = useState([])

    useEffect(()=>{
        if(currentUser){
        fetch(`/discoveries/${currentUser.id}`)
        .then(response => response.json())
        .then(data => setDiscoveries(data))
        }
    },[currentUser])

    const Discoveries = discoveries.map(discovery => {
        return <Record key={discovery.id} user={currentUser} record={discovery}/>
    })
    console.log(Discoveries)

  return (
    <div>
        {Discoveries}
    </div>
  )
}

export default DiscoverPage
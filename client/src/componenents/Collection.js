import React, { useEffect, useState } from 'react'
import Record from './Record'

function Collection({currentUser}) {
    const [records, setRecords] = useState([])
 
    useEffect(()=>{
        fetch(`users_records/${currentUser.id}`)
        .then(response => response.json())
        .then(data => setRecords(data))
    },[])

    const collection = records.map(record => {
        return <Record key = {record.id} record={record} user={currentUser}/>
    })

  return (
    <div>
        {collection}
    </div>
  )
}

export default Collection
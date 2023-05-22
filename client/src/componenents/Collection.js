import React from 'react'
import Record from './Record'

function Collection({currentUser, records, handleDelete, onEdit}) {

    const collection = records.map(record => {
        return <Record key = {record.id} record={record} user={currentUser} handleDelete={handleDelete} onEdit={onEdit}/>
    })

  return (
    <div>
        {collection}
    </div>
  )
}

export default Collection
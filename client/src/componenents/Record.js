import React, {useEffect, useState} from 'react'
import { Avatar } from '@mui/material';

function Record({record, user, handleDelete, onEdit}) {
    const [comments, setComments] = useState([])
    const [newComment, setNewComment] = useState("")
    const [showEditForm, setShow] = useState(false)
    const [editForm, setEdit] = useState({
        title: "",
        artist: "",
        year: "",
        genre: "",
        cover_art: ""
    })

    
    useEffect(()=>{
        fetch(`/comments/${record.id}`)
        .then(response => response.json())
        .then(data => setComments(data))
    },[])

    const commentSection = comments.map(comment => {
        return <h3 key = {comment.id}> {comment.user} {comment.text}</h3>
    })

    function submitHandler(e){
        e.preventDefault()
        const data = {
            "text": newComment,
            "user_id": user.id,
            "record_id": record.id,
        }

        fetch(`comment`,{
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Accepts': 'application/json'
              },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => setComments([...comments, data]))
        setNewComment("")
    }

    function changeHandler(e){
        setNewComment(e.target.value)
    }
    function handleClick(e){
        fetch(`/users_record/${record.id}`,{
            method: "DELETE"
        })
        .then(response => response.json())
        .then(data => handleDelete(data))
    }

    function handleEdit(e){
        setShow(!showEditForm)
    }

    function editHandler(e){
        setEdit({...editForm, [e.target.name]: e.target.value})
    }
    
    function editSubmitHandler(e){
        e.preventDefault()
        fetch(`/record/${record.id}`,{
            method: "PATCH",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(editForm)
        })
        .then(response => response.json())
        .then(data => onEdit(data))
    }

  return (
    <div className="record">
        <div className="record_header">
            <Avatar
                className="record_avatar"
                alt = "Avatar"
                src = "https://cdn.britannica.com/91/197591-050-E90418AF/Bob-Dylan-Bringing-It-All-Back-Home-1965.jpg"
                />                
        </div>
        <img className="record_img" src = {record.cover_art}/>
        <button>Like Button</button>
        <button onClick={handleEdit}>Edit Details</button>
        <button onClick={handleClick}>Delete Record</button>
        {showEditForm? 
        <form onSubmit={editSubmitHandler}>
            <input value={editForm.title} onChange={editHandler} placeholder='Enter title' name='title'/>
            <input value={editForm.artist} onChange={editHandler} placeholder='Enter artist' name='artist'/>
            <input value={editForm.year} onChange={editHandler} placeholder='Enter year of release' name='year'/>
            <input value={editForm.genre} onChange={editHandler} placeholder='Enter genre' name='genre'/>
            <input value={editForm.cover_art} onChange={editHandler}placeholder='Enter cover_art' name='cover_art'/>
            <input type='submit'/>
        </form>
        :null}
        <div className="records_comment_section">
            {commentSection}
        </div>
        <form onSubmit={submitHandler}>
            <input placeholder="Enter comment..." name="comment" value={newComment} onChange={changeHandler}/>
        </form>
    </div>
  )
}

export default Record
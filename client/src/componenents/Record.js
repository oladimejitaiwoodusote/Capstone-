import React, {useEffect, useState} from 'react'
import { Avatar } from '@mui/material';
import { faHeart, faBookmark } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

function Record({record, user}) {
    const [comments, setComments] = useState([])
    const [newComment, setNewComment] = useState("")
    
    useEffect(()=>{
        fetch(`/comments/${record.id}`)
        .then(response => response.json())
        .then(data => setComments(data))
    },[])

    const commentSection = comments.map(comment => {
        return <h3>{comment.user} {comment.text}</h3>
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
    }

    function changeHandler(e){
        setNewComment(e.target.value)
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
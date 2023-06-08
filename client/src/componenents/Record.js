import React, {useEffect, useState} from 'react'
import { Avatar } from '@mui/material';
import {Link} from 'react-router-dom'
import './Record.css'
import FavoriteIcon from '@mui/icons-material/Favorite';

function Record({record, user, handleDelete, onEdit}) {
    const [comments, setComments] = useState([])
    const [newComment, setNewComment] = useState("")
    const [showEditForm, setShow] = useState(false)
    const [showInfo, setShowInfo] = useState(true)
    const [editForm, setEdit] = useState({
        title: "",
        artist: "",
        year: "",
        genre: "",
        cover_art: ""
    })
    const [likeCount, setLikeCount] = useState(0);
    const [liked, setLiked] = useState(false);

    useEffect(()=>{
        fetch(`/comments/${record.id}`)
        .then(response => response.json())
        .then(data => setComments(data))
    },[])

    useEffect(()=> {
        fetch(`/likes/${record.id}`)
        .then(response => response.json())
        .then(data => setLikeCount(data.length))
    },[])

   

    const commentSection = comments.map(comment => {
        return <h4 className="record_comment" key = {comment.id}>
                    <strong> {comment.user}</strong>: {comment.text}   
                </h4>
    })

    function submitHandler(e){
        e.preventDefault()
        const data = {
            "text": newComment,
            "user_id": user.id,
            "record_id": record.id,
        }

        fetch(`/comment`,{
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

    function handleLike(){
        if(liked){
            setLikeCount(likeCount - 1)
        } else {
            setLikeCount(likeCount + 1)            

        }
        setLiked(!liked)
    }

    function handleInfo(){
        setShowInfo(!showInfo)
    }
    
  return (
    <div className="record">
        <div className="record_header">
            <Avatar
                className="record_avatar"
                alt = "Avatar"
                src = {record.avatar}
                />   
            <Link to={`/users/${record.user_id}`}>{record.username}</Link>
        </div>
        {showInfo? <img onClick={handleInfo} className="record_img" src = {record.cover_art}/>:
        <div className="record_info" onClick={handleInfo}>
            <p>{record.title}</p>
            <p>{record.artist}</p>
            <p>{record.year}</p>
            <p>{record.genre}</p>
        </div>
        }
        <button className='record_like_button' onClick={handleLike}>
            <FavoriteIcon color={liked? 'secondary': 'action'}/>
        </button>
        <span className='record_like_count'>{likeCount} Likes</span>
        {user.id === record.user_id?<button className="record_edit_button" onClick={handleEdit}>Edit Details</button>: null}
        {user.id === record.user_id? <button className="record_delete_button"onClick={handleClick}>Delete Record</button>: null}
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
        <div className="record_comment_section">
            {commentSection}
        </div>
        <form onSubmit={submitHandler}>
            <input placeholder="Enter comment..." name="comment" value={newComment} onChange={changeHandler}/>
        </form>
    </div>
  )
}

export default Record
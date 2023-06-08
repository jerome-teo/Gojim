import React from 'react'
import "./profile.css"
import { useNavigate } from "react-router-dom";
//if not logged in, should redirect to login page

import Button from 'react-bootstrap/Button';

import { Link } from 'react-router-dom';
import { useState } from 'react';
import { useEffect } from 'react';

const Profile = () => {
  const navigate = useNavigate();
  
  function signOut(){
    //Should have signout logic here
    localStorage.clear();
    navigate("/login");
  }

  const [username, setUsername] = useState("default")
  useEffect(() => {
    setUsername(localStorage.getItem("username").substring(1,localStorage.getItem("username").length-1))
  });

  return (
    <div className="profile">
      <div /*onClick={prompt for file}*/ className="rounded-circle">
        <img src="default.png"></img>
      </div>
      <div className="profileGraphic">{username.substring(0,1)}</div>
      <div className="profileText">
        <p>{username}</p>
        <div className="lesserText">
          <p>XX Workouts Created</p>
        </div>
      </div>
      <div className="buttons">
        <p><Link to="/workouts">My Workouts</Link> </p>
        <p><Button className="signOut" variant="danger" onClick={signOut} >Log Out</Button></p>
      </div>
    </div>
  )
}

export default Profile
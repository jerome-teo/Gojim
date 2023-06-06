import React from 'react'
import "./profile.css"
import { useNavigate } from "react-router-dom";

//if not logged in, should redirect to login page

import Button from 'react-bootstrap/Button';

import { Link } from 'react-router-dom';

const Profile = () => {
  const navigate = useNavigate();
  function signOut(){
    //Should have signout logic here
    localStorage.clear();
    navigate("/login");
  }

  return (
    <div className="profile">
      <Button variant="link" /*onClick={prompt for file}*/ className="rounded-circle">
        <img src="default.png"></img>
      </Button>
      <div className="profileText">
        <p>John Smith</p>
        <div className="lesserText">
          <p>XX Workouts Created</p>
        </div>
      </div>
      <div className="buttons">
        <p><Link to="/workouts">My Workouts</Link> </p>
        <p><Button className="signOut" variant="danger" onClick={signOut} >Sign Out</Button></p>
      </div>
    </div>
  )
}

export default Profile
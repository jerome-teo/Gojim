import React, { useState } from 'react';
import "./navigation.css";
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';

import { Outlet } from 'react-router-dom';
import { useNavigate } from "react-router-dom";
import { useEffect } from 'react';

const Navigation = () => {

  const navigate = useNavigate();
  const toProfile = () => {
    if(localStorage.getItem("username") === null){
      navigate("/login")
    } else{
      navigate("/profile");
    }
  }
  const handleCreateClick = () => {
    if(localStorage.getItem("username") === null){
      navigate("/login");
    } else {
      navigate("/create")
    }
  }
  const handleWorkoutsClick = () => {
    if(localStorage.getItem("username") === null){
      navigate("/login");
    } else {
      navigate("/workouts")
    }
  }
  const handleSettingsClick = () => {
    if(localStorage.getItem("username") === null){
      navigate("/login");
    } else {
      navigate("/settings")
    }
  }
  const handleLoginClick = () => {
    navigate("/login")
  }

  const handleSignupClick = () => {
    navigate("/signup")
  }

  const handleHomeClick = () => {
    navigate("/")
  }

  const [loggedIn, setLoggedIn] = useState(false)
  useEffect(() => {
    if(localStorage.getItem("username") === null){
      setLoggedIn(false)
    } else {
      setLoggedIn(true)
    }
  });

  return (
    <div>
      <div className="navbar">
        <div className="navtabs">
            <p className="logo">GoJim!</p>
            <Button variant="link"><p onClick={handleHomeClick}>Home</p></Button>
            <Button variant="link"><p onClick={handleCreateClick}>Create Workout</p></Button>
            <Button variant="link"><p onClick={handleWorkoutsClick}>My Workouts</p></Button>
            <Button variant="link"><p onClick={handleSettingsClick}>Settings</p></Button>
            {!loggedIn && (
              <Button variant="link"><p onClick={handleLoginClick}>Login</p></Button>
            )} 
            {!loggedIn && (
              <Button variant="link"><p onClick={handleSignupClick}>Sign Up</p></Button>
            )} 
            <Button variant="link" onClick={toProfile} className="rounded-circle">
              <img src="default.png"></img>
            </Button>
        </div>
      </div>
      <Outlet />
    </div>
  )
}

export default Navigation
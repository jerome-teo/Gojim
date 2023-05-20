import React from 'react';
import "./navigation.css";
import 'bootstrap/dist/css/bootstrap.min.css';


const Navigation = () => {
  return (
    <div className="navbar">
        <div className="navtabs">
            <p><a href="#home">Home</a> </p>
            <p><a href="#workouts">My Workouts</a> </p>
            <p><a href="#settings">Settings</a> </p>
            <p><a href="#login">Login</a> </p>
            <i></i>
        </div>
    </div>
  )
}

export default Navigation
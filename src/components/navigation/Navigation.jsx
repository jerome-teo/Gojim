import React from 'react';
import "./navigation.css";
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';

const Navigation = () => {
  return (
    <div className="navbar">
        <div className="navtabs">
            <p><a href="#home">Home</a> </p>
            <p><a href="#workouts">My Workouts</a> </p>
            <p><a href="#settings">Settings</a> </p>
            <p><a href="#login">Login</a> </p>
            <Button variant="link" href="#profile" className="rounded-circle">
              <img src="test.webp"></img>
            </Button>
        </div>
    </div>
  )
}

export default Navigation
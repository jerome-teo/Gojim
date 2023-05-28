import React from 'react';
import "./navigation.css";
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';

import { Outlet } from 'react-router-dom';
import { Link } from 'react-router-dom';
import { useNavigate } from "react-router-dom";

const Navigation = () => {

  const navigate = useNavigate();
  const toProfile = () => navigate("/profile");

  return (
    <div>
      <div className="navbar">
        <div className="navtabs">
            <p><Link to="/">Home</Link> </p>
            <p><Link to="/workouts">My Workouts</Link> </p>
            <p><Link to="/settings">Settings</Link> </p>
            <p><Link to="/login">Login</Link> </p>
            <Button variant="link" onClick={toProfile} className="rounded-circle">
              <img src="test.webp"></img>
            </Button>
        </div>
      </div>
      <Outlet />
    </div>
  )
}

export default Navigation
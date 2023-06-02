import React from 'react'
import "./profile.css"

//if not logged in, should redirect to login page

import Button from 'react-bootstrap/Button';

import { Link } from 'react-router-dom';

const Profile = () => {

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
      <div className="bio">
        About Me: Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Morbi ac nulla velit. Interdum et malesuada fames ac ante ipsum primis in faucibus.
      </div>
      <div className="buttons">
        <p><Link to="/workouts">My Workouts</Link> </p>
      </div>
    </div>
  )
}

export default Profile
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
  
  const owner = localStorage.getItem("username");
  const num_workouts = 0;
  const [workoutNum, setWorkoutNum] = useState(num_workouts);
  useEffect( () => {
    //add a like
    console.log("workout num")
      const handleWorkoutNum = async (e) => {
      console.log("workout num in async!")
      //handle backend logic here
      const data = {
        owner,
      };
      try {
        const response = await fetch ('http://127.0.0.1:5000/get-num-workouts', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data),
        })
        console.log(JSON.stringify(data))

        if (response.ok){
          const jsonData = await response.json();
          console.log(jsonData)
          let numArray = Array.from(jsonData)
          console.log("hereh!")
          console.log(Array.from(jsonData))
          console.log(numArray)
          console.log("lets go")
          console.log(numArray[0].num_workouts)
          setWorkoutNum(numArray[0].num_workouts);
        } else {
          console.error('Error');
        }
      } catch (error){
        console.error('Error:', error);
      };
    }
    handleWorkoutNum();
  })


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
      <Button variant="link" /*onClick={prompt for file}*/ className="rounded-circle">
        <img src="default.png"></img>
      </Button>
      <div className="profileText">
        <p>{username}</p>
        <div className="lesserText">
          <p>{workoutNum} Workouts Created</p>
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
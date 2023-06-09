import React from 'react'
import "./workouts.css"
import Button from 'react-bootstrap/Button';
import { useState } from 'react';
import Popup from 'reactjs-popup';
import { json } from 'react-router-dom';

const myWorkouts = [
  {
    id: 0,
    name: "Test Workout 1",
    workoutString: "Pushups:  Reps: 5 Sets: 5\nPullups:  Reps: 4 Sets: 5",
    likes: 0
  },
  {
    id: 1,
    name: "Test Workout 2",
    workoutString: "Curls:  Reps: 5 Sets: 5",
    likes: 0
  },
  {
    id: 2,
    name: "Test Workout 3",
    workoutString: "Crunches:  Reps: 5 Sets: 5",
    likes: 0
  }
];

const savedWorkouts = [
  {
    name: "Saved Workout 1",
    workoutString: "Pushups:  Reps: 5 Sets: 5\nPullups:  Reps: 4 Sets: 5"
  },
  {
    name: "Saved Workout 2",
    workoutString: "Pushups:  Reps: 5 Sets: 5\nPullups:  Reps: 4 Sets: 5"
  },
  {
    name: "Saved Workout 3",
    workoutString: "Pushups:  Reps: 5 Sets: 5\nPullups:  Reps: 4 Sets: 5"
  }
];


const Workouts = () => {
  const [myWorkout, setMyWorkout] = useState(myWorkouts)

  const handleMyDelete = (workoutId) => {
    console.log("here is handle my delete")
    const handleDelete = async (e) => {
      console.log(workoutId)
      console.log("here is handle delete!!!")
    // e.preventDefault();
    //handle backend logic here
    const data = {
      workoutId,
    };
    try{
      const response = await fetch ('http://127.0.0.1:5000/delete-workout', {
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
        // indow.location.href = "/workouts"
        handleMine();
      } else {
        console.error('Error');
      }
    } catch (error){
      console.error('Error:', error);
    };
  }
    handleDelete();
  }
  
  const handleSaveRemove = () => {
    //handle deleting saved workout here
  }

  const [likeCount, setLikeCount] = useState(0);
  const handleLike = (/*can pass in something referring to the workout if necessary*/) => {
    //add a like

  }

  const owner = localStorage.getItem("username")
  const handleSave = (workoutId) => (/*can pass in something referring to the workout if necessary*/) =>{
    //save to workouts
    console.log("here is handle save")
    const handleMySave = async (e) => {
      console.log(workoutId)
      console.log("here is handle my save!!!")
    // e.preventDefault();
    //handle backend logic here
    const data = {
      workoutId,
      owner,
    };
    try{
      const response = await fetch ('http://127.0.0.1:5000/save-workout', {
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
        window.location.href = "/workouts"
      } else {
        console.error('Error');
      }
    } catch (error){
      console.error('Error:', error);
    };
  }
    handleMySave();

  }

  const myWorkoutResults = myWorkout.map(workoutName =>
    <li key={workoutName.name} className="list">
      <Popup className="workoutPopup" trigger={<Button className="ownWorkout" variant="link">{workoutName.name}</Button>} modal nested>
        {closed => (
          <div>
            <div className="popupTitle">
              {workoutName.name}
            </div>
            <div className="popupString">
              {workoutName.workoutString}
            </div>
            <p className="likeCounter">{likeCount} Likes</p>
            <Button className="likeButton" variant="dark" onClick={handleLike}>Like</Button>
            <Button className="saveButton" variant="dark" onClick={ () => handleSave(workoutName.id)}>Save</Button>
          </div>
        )}
      </Popup>
      <Button className="deleteButton" variant="danger" onClick={ () => handleMyDelete(workoutName.id)}>
        Delete
      </Button>
    </li>
  );

  const savedWorkoutResults = savedWorkouts.map(workoutName =>
    <li key={workoutName.name} className="list">
      <Popup className="workoutPopup" trigger={<Button className="ownWorkout" variant="link">{workoutName.name}</Button>} modal nested>
        {closed => (
          <div>
            <div className="popupTitle">
              {workoutName.name}
            </div>
            <div className="popupString">
              {workoutName.workoutString}
            </div>
            <p className="likeCounter">{likeCount} Likes</p>
            <Button className="likeButton" variant="dark" onClick={handleLike}>Like</Button>
            <Button className="saveButton" variant="dark" onClick={handleSave}>Save</Button>
          </div>
        )}
      </Popup>
      <Button className="deleteButton" variant="danger" onClick={handleSaveRemove}>
        Remove
      </Button>
    </li>
  );

  const [showMine, setShowMine] = useState(false);
  const [showSaved, setShowSaved] = useState(false);

  const handleMine = () => {
    setShowMine(true);
    setShowSaved(false);
    const finalize = async (e) => {
      // e.preventDefault();
      const data = {
        owner,
      }

      try {
        console.log("here is workouts.jsx")
        console.log(localStorage.getItem("username"),)
        const response = await fetch('http://127.0.0.1:5000/get-my-workouts', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data),
        })
        console.log(response)
        if (response.ok) {
          const jsonData = await response.json();
          console.log(jsonData)
          console.log("here!")
          setMyWorkout(Array.from(jsonData))
          console.log(jsonData)
        } else {
          console.log('Error: ');
        }
      }
      catch (error) {
        console.log("error:", error);
      }
    }
    finalize()
  }
  const handleSaved = () => {
    setShowMine(false);
    setShowSaved(true);
  }

  return (
    <div>
      <div>
        <p className="ownWorkoutTitle">Workouts</p>
        <div className="shownWorkouts">
          {showMine && (
            <ul>
              <p>Created Workouts</p>
              {myWorkoutResults}
            </ul>
          )}
          {showSaved && (
            <ul>
              <p>Saved Workouts</p>
              {savedWorkoutResults}
            </ul>
          )}
        </div>
        <Button className="mineButton" variant="secondary" onClick={handleMine}>Show My Workouts</Button>
        <Button className="savedButton" variant="secondary" onClick={handleSaved}>Show Saved Workouts</Button>
      </div>
    </div>
  )
}

export default Workouts
import React from 'react'
import "./workouts.css"
import Button from 'react-bootstrap/Button';
import { useState } from 'react';
import Popup from 'reactjs-popup';

const myWorkouts = [
  {
    name: "Test Workout 1",
    workoutString: "Pushups:  Reps: 5 Sets: 5\nPullups:  Reps: 4 Sets: 5"
  },
  {
    name: "Test Workout 2",
    workoutString: "Curls:  Reps: 5 Sets: 5"
  },
  {
    name: "Test Workout 3",
    workoutString: "Crunches:  Reps: 5 Sets: 5"
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

  const handleMyDelete = () => {
    //handle deleting my workout here
  }
  
  const handleSaveRemove = () => {
    //handle deleting saved workout here
  }

  const handleLike = (/*can pass in something referring to the workout if necessary*/) => {
    //add a like
  }

  const handleSave = (/*can pass in something referring to the workout if necessary*/) =>{
    //save to workouts
  }

  const [workoutName, setWorkoutName] = useState({
    listOfNames: [],
  });

  const myWorkoutResults = myWorkouts.map(workoutName =>
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
            <Button className="likeButton" variant="dark" onClick={handleLike}>Like</Button>
            <Button className="saveButton" variant="dark" onClick={handleSave}>Save</Button>
          </div>
        )}
      </Popup>
      <Button className="deleteButton" variant="danger" onClick={handleMyDelete}>
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

  const owner = localStorage.getItem("username")

  const handleMine = () => {
    setShowMine(true);
    setShowSaved(false);
    const finalize = async (e) => {
      e.preventDefault();
      const data = {
        owner,
      }

      // try {
      //   console.log("here is workouts.jsx")
      //   console.log(localStorage.getItem("username"))
      //   const response = await fetch('http://127.0.0.1:5000/get-my-workouts-names', {
      //     method: 'GET',
      //     header: {
      //       'Content-Type': 'application/json',
      //     },
      //     body: JSON.stringify(data),
      //   })
      //   if (response) {
      //     const jsonData = await response.json();
      //     console.log(jsonData)
      //   } else {
      //     console.error('Error: ');
      //   }
      // }
      // catch (error) {
      //   console.error('Error:', error);
      // }
      try {
        console.log("here is workouts.jsx")
        console.log(localStorage.getItem("username"))
        fetch("http://127.0.0.1:5000/get-my-workouts-names").then(
          response => response.json()
        ).then(

        )
      }
    }
  }
  const handleSaved = () => {
    setShowMine(false);
    setShowSaved(true);
  }

  return (
    <div>
      <div>
        <p className="ownWorkoutTitle">Workouts</p>
        <p className="shownWorkouts">
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
        </p>
        <Button className="mineButton" variant="secondary" onClick={handleMine}>Show My Workouts</Button>
        <Button className="savedButton" variant="secondary" onClick={handleSaved}>Show Saved Workouts</Button>
      </div>
    </div>
  )
}

export default Workouts
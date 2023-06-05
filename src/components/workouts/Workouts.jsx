import React from 'react'
import "./workouts.css"
import Button from 'react-bootstrap/Button';
import { useState } from 'react';

const myWorkouts = [
  {
    name: "Test Workout 1"
  },
  {
    name: "Test Workout 2"
  },
  {
    name: "Test Workout 3"
  }
];

const savedWorkouts = [
  {
    name: "Saved Workout 1"
  },
  {
    name: "Saved Workout 2"
  },
  {
    name: "Saved Workout 3"
  }
];

const handleMyDelete = () => {
  //handle deleting my workout here
}

const handleSaveRemove = () => {
  //handle deleting saved workout here
}

const Workouts = () => {

  const myWorkoutResults = myWorkouts.map(workoutName =>
    <li key={workoutName.name} className="list">
      <Button className = "ownWorkout" variant="link">{workoutName.name}</Button>
      <Button className="deleteButton" variant="danger" onClick={handleMyDelete}>
        Delete
      </Button>
    </li>
  );

  const savedWorkoutResults = savedWorkouts.map(workoutName =>
    <li key={workoutName.name} className="list">
      <Button className = "ownWorkout" variant="link">{workoutName.name}</Button>
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
import React from 'react'
import "./workouts.css"
import Button from 'react-bootstrap/Button';

const workouts = [
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

const Workouts = () => {

  const workoutResults = workouts.map(workoutName =>
    <li key={workoutName.name} className="list">
      <Button variant="link">{workoutName.name}</Button>
    </li>
  );

  return (
    <div>
      <div className>
        <p className="ownWorkoutTitle">Your Workouts</p>
        <p className="ownWorkouts">
          <ul>
            {workoutResults}
          </ul>
        </p>
      </div>
    </div>
  )
}

export default Workouts
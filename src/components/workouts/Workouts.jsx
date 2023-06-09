import React, { useReducer } from 'react'
import "./workouts.css"
import Button from 'react-bootstrap/Button';
import { useState } from 'react';
import Popup from 'reactjs-popup';
import { json } from 'react-router-dom';
import { useEffect } from 'react';

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


const Workouts = () => {
  const [myWorkout, setMyWorkout] = useState(myWorkouts)
  const [mySavedWorkouts, setSavedWorkouts] = useState(savedWorkouts)
  const owner = localStorage.getItem("username")

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
  
  const handleSaveRemove = (workoutId) => {
    //handle deleting saved workout here
    console.log("here is handle save remove")
    const handleRemoveSave = async (e) => {
      console.log(workoutId)
      console.log("here is handle remove!!")
    // e.preventDefault();
    //handle backend logic here
    const data = {
      workoutId,
      owner
    };
    try{
      const response = await fetch ('http://127.0.0.1:5000/unsave-workout', {
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
        this.forceUpdate()
        // window.location.href = "/workouts"
        handleSaved();
      } else {
        console.error('Error');
      }
    } catch (error){
      console.error('Error:', error);
    };
  }
    handleRemoveSave();
  }

  const [likeCount, setLikeCount] = useState(0);
  const handleLike = (workoutId) => {
    // add a like
    //save to workouts
    console.log("here is handle like")
    const handleMyLike= async (e) => {
      console.log(workoutId)
      console.log("here is handle my like!!!")
    // e.preventDefault();
    //handle backend logic here
    const data = {
      workoutId,
      owner,
    };
    try{
      const response = await fetch ('http://127.0.0.1:5000/like-or-unlike-workout', {
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

        let likeArray = Array.from(jsonData)
        console.log("hereh!")
        console.log(Array.from(jsonData))
        console.log(likeArray)
        console.log("lets go")
        console.log(likeArray[0].num_likes)
        setLikeCount(likeArray[0].num_likes);
        
      } else {
        console.error('Error');
      }
    } catch (error){
      console.error('Error:', error);
    };
  }
    handleMyLike();

  }

  useEffect(() => {
    setLikeCount(likeCount);
  }, [likeCount]);

  const handleDisplay = (workoutId) => {
    console.log("here is handle display")
    const handleMyDisplay= async (e) => {
      console.log(workoutId)
      console.log("here is handle my display!!!")
      // e.preventDefault();
      //handle backend logic here
      const data = {
        workoutId,
      };
      try{
        const response = await fetch ('http://127.0.0.1:5000/get-num-likes', {
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

          let likeArray = Array.from(jsonData)
          console.log("hereh!")
          console.log(Array.from(jsonData))
          console.log(likeArray)
          console.log("lets go")
          console.log(likeArray[0].num_likes)
          setLikeCount(likeArray[0].num_likes);
          
        } else {
          console.error('Error');
        }
      } catch (error){
        console.error('Error:', error);
      };
    }
    handleMyDisplay();
  }

  const myWorkoutResults = myWorkout.map(workoutName =>
    <li key={workoutName.id} className="list">
      <Popup className="workoutPopup" trigger={<Button onClick={() => handleDisplay(workoutName.id)} className="ownWorkout" variant="link">{workoutName.name}</Button>} modal nested>
        {closed => (
          <div>
            <div className="popupTitle">
              {workoutName.name}
            </div>
            <div className="popupString">
              {workoutName.workoutString}
            </div>
            <p className="likeCounter">{workoutName.likes} Likes</p>
            <Button className="likeButton" variant="dark" onClick={() => handleLike(workoutName.id)}>Like</Button>
          </div>
        )}
      </Popup>
      <Button className="deleteButton" variant="danger" onClick={ () => handleMyDelete(workoutName.id)}>
        Delete
      </Button>
    </li>
  );

  const savedWorkoutResults = mySavedWorkouts.map(workoutName =>
    <li key={workoutName.id} className="list">
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
            <Button className="likeButton" variant="dark" onClick={() => handleLike(workoutName.id)}>Like</Button>
          </div>
        )}
      </Popup>
      <Button className="deleteButton" variant="danger" onClick={ () => handleSaveRemove(workoutName.id)}>
        Remove
      </Button>
    </li>
  );

  const [showMine, setShowMine] = useState(false);
  const [showSaved, setShowSaved] = useState(false);

  // HANDLE GET WORKOUTS
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

  // HANDLE GET SAVED WORKOUTS
  const handleSaved = () => {
    setShowMine(false);
    setShowSaved(true);
    const finalize = async (e) => {
      // e.preventDefault();
      const data = {
        owner,
      }

      try {
        console.log("here is workouts saved.jsx")
        console.log(localStorage.getItem("username"),)
        const response = await fetch('http://127.0.0.1:5000/get-saved-workouts', {
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
          setSavedWorkouts(Array.from(jsonData))
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
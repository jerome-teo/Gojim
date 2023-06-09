import React, { useEffect } from 'react'
import "./home.css"
import { ReactSearchAutocomplete } from 'react-search-autocomplete'
import { useState } from 'react';
import Popup from 'reactjs-popup';

import Button from 'react-bootstrap/Button';
import { useNavigate } from "react-router-dom";

let Workouts = [
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
const tags = [
  {
    id: 0,
    name: "Upper-body"
  },{
    id: 1,
    name: "Lower-body"
  },{
    id: 2,
    name: "Beginner"
  },{
    id: 3,
    name: "Intermediate"
  },{
    id: 4,
    name: "Advanced"
  },{
    id: 5,
    name: "Short"
  },{
    id: 6,
    name: "Long"
  },{
    id: 7,
    name: "Full-body"
  },{
    id: 8,
    name: "No Equipment"
  },{
    id: 9,
    name: "Dumbbells Only"
  },{
    id: 10,
    name: "Back"
  },{
    id: 11,
    name: "Chest"
  },{
    id: 12,
    name: "Legs"
  },{
    id: 13,
    name: "Arms"
  },{
    id: 14,
    name: "Shoulders"
  }
]
const Home = () => {
  
  const navigate = useNavigate();

  const [displayedWorkouts, setWorkouts] = useState(Workouts)
  useEffect( () => {
    const finalize = async (e) => {
      // e.preventDefault();

      try {
        console.log("here is home.jsx")
        console.log(localStorage.getItem("username"),)
        const response = await fetch('http://127.0.0.1:5000/get-public-workouts')
        console.log(response)
        if (response.ok) {
          const jsonData = await response.json();
          console.log(jsonData)
          console.log("here!")
          setWorkouts(Array.from(jsonData))
          console.log("helloworld")
          console.log(Array.from(jsonData))
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
  }, []);

  const workoutResults = displayedWorkouts.map(workoutName =>
    <li key={workoutName.id} className="searchList">
      <Popup className="workoutPopup" trigger={<Button variant="link">{workoutName.name}</Button>} modal nested>
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
            <Button className="saveButton" variant="dark" onClick={() => handleSave(workoutName.id)}>Save</Button>
          </div>
        )}
      </Popup>
    </li>
  );


  const [likeCount, setLikeCount] = useState(0); //Maybe best to handle another way, depending on backend
  const handleLike = (/*can pass in something referring to the workout if necessary*/) => {
    if(localStorage.getItem("username") === null){
      navigate("/login")
    }
    //add a like
  }

  const owner = localStorage.getItem("username")
  const handleSave = (workoutId) => {
    if(localStorage.getItem("username") === null){
      navigate("/login")
      return;
    }
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

  const handleSelect = (tags) => {
    if(!tagString.includes(tags.name)){
      setTagString(tagString + tags.name + "\n");
    }
    //Depending on back-end implementation of search, can add tags.name to a data structure here
  }

  

  const [showResults, setShowResults] = useState(true);
  const handleSearch = async (e) => {
    setTagString("");
    setShowResults(true);
    //Handle logic for finding appropriate workouts
    const data = {
      tagString,
    };

    try{
      const response = await fetch ('http://127.0.0.1:5000/search', {
        method: 'POST',
        headers:{
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })
      console.log(JSON.stringify(data))

      if (response.ok){
        const jsonData = await response.json();
        //Set workouts to the array returned
        setWorkouts(Array.from(jsonData))
      } else {
        //Set workouts to empty array
        setWorkouts([])
      }
    } catch (error){
      console.error('Error', error);
    }

  }

  const [tagString, setTagString] = useState("");

  return (
    <div>
      <div className="homeTitle">
        Find Your Workout!
      </div>
      <div className="tagBox">
        <p>Tags</p>
        <textarea readOnly={true} value={tagString}/>
      </div>

      {/*results class must be before class search so that search results appear above the below text*/}
      <div className="results">
        {showResults && (
          <div>
            <p className="searchTitle">Search Results</p>
            <ul>
              {workoutResults}
            </ul>
          </div>
        )}
      </div>
      <div className='search'>
        <ReactSearchAutocomplete 
          styling={{border: "1px solid #000000" }}
          items={tags}
          onSelect={handleSelect}
          placeholder="Enter Tags Here"
        />
      </div>
      <div className="searchButton">
        <Button variant="secondary" onClick={handleSearch}>
          Search!
        </Button>
      </div>
      
    </div>
  );
}

export default Home
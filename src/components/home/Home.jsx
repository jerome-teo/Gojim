import React from 'react'
import "./home.css"
import { ReactSearchAutocomplete } from 'react-search-autocomplete'
import { useState } from 'react';
import Popup from 'reactjs-popup';

import Button from 'react-bootstrap/Button';


const workouts = [
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

  const workoutResults = workouts.map(workoutName =>
    <li key={workoutName.name} className="searchList">
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
            <Button className="saveButton" variant="dark" onClick={handleSave}>Save</Button>
          </div>
        )}
      </Popup>
    </li>
  );


  const [likeCount, setLikeCount] = useState(0); //Maybe best to handle another way, depending on backend
  const handleLike = (/*can pass in something referring to the workout if necessary*/) => {
    //add a like
  }

  const handleSave = (/*can pass in something referring to the workout if necessary*/) =>{
    //save to workouts
  }

  const handleSelect = (tags) => {
    if(!tagString.includes(tags.name)){
      setTagString(tagString + tags.name + "\n");
    }
    //Depending on back-end implementation of search, can add tags.name to a data structure here
  }

  const [showResults, setShowResults] = useState(false);
  const handleSearch = () => {
    setTagString("");
    setShowResults(true);
    //Handle logic for finding appropriate workouts
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
import React from 'react'
import "./home.css"
import { ReactSearchAutocomplete } from 'react-search-autocomplete'
import { useState } from 'react';

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

const Home = () => {

  const tags = [
    {
      id: 0,
      name: "Upper-body"
    },
    {
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
    },
  ]

  const workoutResults = workouts.map(workoutName =>
    <li key={workoutName.name} className="searchList">
      <Button variant="link">{workoutName.name}</Button>
    </li>
  );

  const handleSelect = (tags) => {
    setTagString(tagString + tags.name + "\n");
    //Depending on back-end implementation of search, can add tags.name to a data structure here
  }

  const clearTags = () => {
    setTagString("");
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
      <div className='search'>
        <ReactSearchAutocomplete 
          styling={{border: "1px solid #000000" }}
          items={tags}
          onSelect={handleSelect}
          placeholder="Enter Tags Here"
        />
      </div>
      <div className="searchButton">
        <Button variant="secondary" onClick={clearTags}>
          {/*Should update results section*/}
          Search!
        </Button>
      </div>
      <div className="results">
        <p>Search Results</p>
        <ul>
          {workoutResults}
        </ul>
      </div>
    </div>
  );
}

export default Home
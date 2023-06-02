import React from 'react'
import { useState } from 'react';
import { ReactSearchAutocomplete } from 'react-search-autocomplete'
import "./create.css"

import Button from 'react-bootstrap/Button';

const Create = () => {

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
      <div className="createTitle">
        Make Your Workout!
      </div>
      
      <div className="createTagBox">
        <div className='createSearch'>
          <ReactSearchAutocomplete 
            styling={{border: "1px solid #000000" }}
            items={tags}
            onSelect={handleSelect}
            placeholder="Add tags"
          />
        </div>
        <textarea readOnly={true} value={tagString}/>
      </div>
      <div className="clearButton">
        <Button variant="danger" onClick={clearTags}>
          Clear Tags
        </Button>
      </div>

      <div className="exercise">
        <p>Exercise:</p>
        <textarea className="exerciseName"/>
        <p>Reps:</p>
        <textarea className="exerciseReps"/>
        <p>Sets:</p>
        <textarea className="exerciseSets"/>
      </div>
      <Button className="exerciseButton" variant="secondary" onClick={clearTags}>
        Submit Exercise
      </Button>
    </div>
  )
}

export default Create
import React from 'react'
import { useEffect, useState } from 'react';
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
    
      const [exerciseName, setExerciseName] = useState("");
      const handleExerciseName = box => {
        setExerciseName(box.target.value);
      }
      const [exerciseReps, setExerciseReps] = useState("");
      const handleExerciseReps = box => {
        setExerciseReps(box.target.value);
      }
      const [exerciseSets, setExerciseSets] = useState("");
      const handleExerciseSets = box => {
        setExerciseSets(box.target.value);
      }

      const [exerciseString, setExercise] = useState("");

      const [savedWorkoutString, setPrevWorkout] = useState("");
      const [workoutString, setWorkout] = useState("");
      useEffect(() => {
        setPrevWorkout(workoutString);
        setWorkout(workoutString + exerciseString + "\n");
      }, [exerciseString]);

      const handleExerciseButton = () => {
        if(exerciseName === "" || exerciseReps === "" || exerciseSets === ""){
          return;
        } else {
          //Opportunity to store strings in a temporary database (or main string) here
          setExercise(exerciseName + ":  Reps: " + exerciseReps + " Sets: " + exerciseSets);
        }
        setExerciseName("");
        setExerciseReps("");
        setExerciseSets("");
      }

      const finalize = () => {
        //Should send the strings in the temporary database to a main database
        //Should do the same for the tags in tagString
        setWorkout("");
      }

      const handleUndo = () => {
        setWorkout(savedWorkoutString);
      }

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
        <textarea className="exerciseName" value={exerciseName} onChange={handleExerciseName}/>
        <p>Reps:</p>
        <textarea className="exerciseReps" value={exerciseReps} onChange={handleExerciseReps}/>
        <p>Sets:</p>
        <textarea className="exerciseSets" value={exerciseSets} onChange={handleExerciseSets}/>
      </div>
      <Button className="exerciseButton" variant="secondary" onClick={handleExerciseButton}>
        Add Exercise
      </Button>
      <Button className="undoButton" variant="danger" onClick={handleUndo}>
        Undo
      </Button>

      <div className="workoutPreview">
        <p>Current Workout</p>
        <textarea readOnly={true} value={workoutString}/>
      </div>
      <Button className="workoutButton" variant="secondary" onClick={finalize}>
        Submit Workout
      </Button>

    </div>
  )
}

export default Create
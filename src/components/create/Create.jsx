import React from 'react'
import { useEffect, useState } from 'react';
import { ReactSearchAutocomplete } from 'react-search-autocomplete'
import "./create.css"
import { useNavigate } from "react-router-dom";

import Button from 'react-bootstrap/Button';

const Create = () => {

    //Possible tags
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
    
      //Handles what tags to associate with exercise
      const handleSelect = (tags) => {
        setTagString(tagString + tags.name + "\n");
        //Depending on back-end implementation of search, can add tags.name to a data structure here
      }
    
      //Clears tags
      const clearTags = () => {
        //Should also handle clearing the tags for the search
        setTagString("");
      }
      const [tagString, setTagString] = useState("");
    
      //Contains name of exercise
      const [exerciseName, setExerciseName] = useState("");
      const handleExerciseName = box => {
        setExerciseName(box.target.value);
      }

      //Contains reps
      const [exerciseReps, setExerciseReps] = useState("");
      const handleExerciseReps = box => {
        setExerciseReps(box.target.value);
      }

      //Contains sets
      const [exerciseSets, setExerciseSets] = useState("");
      const handleExerciseSets = box => {
        setExerciseSets(box.target.value);
      }

      //Contains name of workout
      const [workoutName, setWorkoutName] = useState("");
      const handleNameChange = box => {
        setWorkoutName(box.target.value);
      }
      const [exerciseString, setExercise] = useState("");

      //Necessary for state to update in one click
      const [savedWorkoutString, setPrevWorkout] = useState("");
      const [workoutString, setWorkout] = useState("");
      useEffect(() => {
        setPrevWorkout(workoutString);
        if(exerciseString !== ""){
          setWorkout(workoutString + exerciseString + "\n");
        }
      }, [exerciseString]);

      //Handles submitting exercise to the workoutString
      const handleExerciseButton = () => {
        if(exerciseName === "" || exerciseReps === "" || exerciseSets === ""){
          return;
        } else {
          setExercise(exerciseName + ":  Reps: " + exerciseReps + " Sets: " + exerciseSets);
        }
        setExerciseName("");
        setExerciseReps("");
        setExerciseSets("");
      }

      //Handles submitting the actual workout *********
      const navigate = useNavigate();

      const finalize = async (e) => {
        e.preventDefault();
        const data = {
          workoutName,
          workoutString,
          tagString,
        };

        if(workoutString !== "" && workoutName !== ""){
          
          try {
            const response = await fetch('http://localhost:5000/create-new-workout', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify(data),
            })
            if (response.ok) {
            const jsonData = await response.json();
            console.log(jsonData)
          } else {
            console.error('Error: ');
          }
          //Should send the workout string to the database
          //Should do the same for the tags in tagString
          //Should do the same for the workout name
          setWorkout("");
          setWorkoutName("");
          navigate("/workouts");
        } catch (error){
          console.error('Error:', error);
        }
        //if bracket
        }
        //function bracket
      };

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
        <p>Name: <textarea onChange={handleNameChange} value={workoutName} className="nameInput"></textarea></p>
        <textarea className="workoutPreviewBox" readOnly={true} value={workoutString}/>
      </div>
      <Button className="workoutButton" variant="secondary" onClick={finalize}>
        Submit Workout
      </Button>

    </div>
  )
}

export default Create
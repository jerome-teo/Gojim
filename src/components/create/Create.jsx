import React from 'react'
import { useEffect, useState } from 'react';
import { ReactSearchAutocomplete } from 'react-search-autocomplete'
import "./create.css"
import { useNavigate } from "react-router-dom";

import Button from 'react-bootstrap/Button';
//Possible tags
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

const Create = () => {

      //Handles what tags to associate with exercise
      const handleSelect = (tags) => {
        if(!tagString.includes(tags.name)){
          setTagString(tagString + tags.name + "\n");
        }
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
      // const [owner, setOwner] = useState("");
      const owner = localStorage.getItem("username")
      //Handles submitting the actual workout *********
      const navigate = useNavigate();

      const finalize = async (e) => {
        e.preventDefault();
        const data = {
          workoutName,
          workoutString,
          tagString,
          owner,
        };

        if(workoutString !== "" && workoutName !== ""){

          try {
            // setOwner(localStorage.getItem("username"))
            console.log("here is Create.jsx")
            // console.log(owner)
            console.log(localStorage.getItem("username"))
            console.log("localStorage:", localStorage)
            console.log("data:", data)
            const response = await fetch('http://127.0.0.1:5000/create-new-workout', {
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
        <div className="nameAndBox">
          <p><div className="name">Name:</div><textarea onChange={handleNameChange} value={workoutName} className="nameInput"></textarea></p>
        </div>
        <textarea className="workoutPreviewBox" readOnly={true} value={workoutString}/>
      </div>
      <Button className="workoutButton" variant="secondary" onClick={finalize}>
        Submit Workout
      </Button>

    </div>
  )
}

export default Create

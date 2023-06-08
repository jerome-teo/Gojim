import Navigation from "./components/navigation/Navigation"
import Login from "./components/login/Login";
import Workouts from "./components/workouts/Workouts"
import Create from "./components/create/Create";
import Settings from "./components/settings/Settings"
import SignUp from "./components/signup/SignUp"
import Home from "./components/home/Home";
import "./App.css"

import { Route } from 'react-router-dom';
import { Routes } from 'react-router-dom';
import Profile from "./components/profile/Profile";
import { useEffect } from "react";

function App() {

    useEffect(() => {
        // addDefault workouts taken from create.jsx logic
        const addDefaultWorkouts = async () => {
            try {
                console.log("creating default workouts")
                const response = await fetch('http://127.0.0.1:5000/create-default-workout', {
                  method: 'POST',
                  mode:"no-cors",
                  headers: {
                    'Access-Control-Allow-Origin':'*',
                    'Access-Control-Allow-Methods':'POST,PATCH,OPTIONS'
                  },
                })
                if (response.ok) {
                const jsonData = await response.json();
                console.log("Error")
              } else {
                console.error('Error: ');
              }
            } catch (error){
              console.error('Error:', error);
            }
        }
        addDefaultWorkouts();
    }, []);

    return (
        <div>
            <Routes>
                <Route path="/" element={<Navigation />}>
                    <Route path="/" element={<Home />}/>
                    <Route path="/profile" element={<Profile />}/>
                    <Route path="/create" element={<Create />}/>
                    <Route path="/workouts" element={<Workouts />}/>
                    <Route path="/settings" element={<Settings />}/>
                    <Route path="/login" element={<Login />}/>
                    <Route path="/signup" element={<SignUp />}/>
                </Route>
            </Routes>
        </div>
    );
}

export default App;
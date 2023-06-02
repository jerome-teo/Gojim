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

function App() {
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
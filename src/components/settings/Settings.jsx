import React from 'react'
import "./settings.css"
import Switch from "react-switch";
import { useState } from 'react';
import { useRef } from 'react';
import Popup from 'reactjs-popup';
import 'reactjs-popup/dist/index.css';
import Button from 'react-bootstrap/Button';

const Settings = () => {

  //Used for toggling public/private workout
  const [on, toggleOn] = useState(false);
  
  const ref = useRef();

  //Handles toggling workouts as private or public
  const handleToggle = () => {
    toggleOn(!on);
    //handle backend logic here
  }

  //Handles changing username
  const handleUsername = () => {
    ref.current.close();
    //handle backend logic here
  }

  //Handles changing email
  const handleEmail = () => {
    ref.current.close();
    //handle backend logic here
  }

  //Handles changing password
  const handlePassword = () => {
    ref.current.close();
    //handle backend logic here
  }

  //Handles deleting account
  const handleDelete = () => {
    //handle backend logic here
  }

  //Contains newly typed username
  const [username, setUsername] = useState("");
  const handleNameChange = box => {
    setUsername(box.target.value);
  }

  //Contains newly typed email
  const [email, setEmail] = useState("");
  const handleEmailChange = box => {
    setEmail(box.target.value);
  }

  //Contains string for old password
  const [oldPassword, setOldPassword] = useState("");
  const handleOldPassword = box => {
    setOldPassword(box.target.value);
  }
  //Contains string for new password
  const [password, setPassword] = useState("");
  const handlePasswordChange = box => {
    setPassword(box.target.value);
  }

  return (
    <div>
      <div className="settingTitle">
        Settings
      </div>

      {/*Toggle private/public workouts*/}
      <div className="options">
        <p>
          Workouts Public?
          <Switch onChange={handleToggle} checked={on} className="toggle"/>
        </p>

        {/*Change Name*/}
        <p>
          <Popup ref={ref} position="right center" trigger={<Button variant="link" className="button">Change Username</Button>}>
            {close =>(
              <div>
                <p className="settingsPopupTitle">New Username</p>
                <p><input type="text" className="input" onChange={handleNameChange}/></p>
                <p>
                  <Button variant="link" onClick = {handleUsername} className="button">Confirm</Button>
                  <Button variant="link" onClick = {close} className="button">Cancel</Button>
                </p>
              </div>
            )}
          </Popup>
        </p>

        {/*Change email*/}
        <p>
          <Popup ref={ref} position="right center" trigger={<Button variant="link" className="button">Change Email</Button>}>
            {close =>(
              <div>
                <p className="settingsPopupTitle">New Email</p>
                <p><input type="text" className="input" onChange={handleEmailChange}/></p>
                <p>
                  <Button variant="link" onClick = {handleEmail} className="button">Confirm</Button>
                  <Button variant="link" onClick = {close} className="button">Cancel</Button>
                </p>
              </div>
            )}
          </Popup>
        </p>

        {/*Change password; asks for both old password and new pasword*/}
        <p>
          <Popup ref={ref} position="right center" trigger={<Button variant="link" className="button">Change Password</Button>}>
            {close =>(
              <div>
                <p className="settingsPopupTitle">Old Password</p>
                <p><input type="text" className="input" onChange={handleOldPassword}/></p>
                <p className="settingsPopupTitle">New Password</p>
                <p><input type="text" className="input" onChange={handlePasswordChange}/></p>
                <p>
                  <Button variant="link" onClick = {handlePassword} className="button">Confirm</Button>
                  <Button variant="link" onClick = {close} className="button">Cancel</Button>
                </p>
              </div>
            )}
          </Popup>
        </p>

        {/*Delete Account*/}
        <p><Button variant="link" onClick = {handleDelete} className="button">Delete Account</Button></p>
      
      </div>
    </div>
  )
}

export default Settings
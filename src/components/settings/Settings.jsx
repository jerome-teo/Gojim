import React from 'react'
import "./settings.css"
import Switch from "react-switch";
import { useState } from 'react';
import Popup from 'reactjs-popup';
import 'reactjs-popup/dist/index.css';
import Button from 'react-bootstrap/Button';

const Settings = () => {

  //Used for toggling public/private workout
  const [on, toggleOn] = useState(false);

  return (
    <div>
      <div className="settingTitle">
        Settings
      </div>

      {/*Toggle private/public workouts*/}
      <div className="options">
        <p>
          Workouts Public?
          <Switch onChange={toggleOn} checked={on} className="toggle"/>
        </p>

        {/*Change Name*/}
        <p>
          <Popup position="right center" trigger={<Button variant="link" className="button">Change Username</Button>}>
            {close =>(
              <div>
                <p className="popupTitle">New Username</p>
                <p><input type="text" className="input"/></p>
                <p>
                  <Button variant="link" onClick = {close} className="button">Confirm</Button>
                  <Button variant="link" onClick = {close} className="button">Cancel</Button>
                </p>
              </div>
            )}
          </Popup>
        </p>

        {/*Change email*/}
        <p>
          <Popup position="right center" trigger={<Button variant="link" className="button">Change Email</Button>}>
            {close =>(
              <div>
                <p className="popupTitle">New Email</p>
                <p><input type="text" className="input"/></p>
                <p>
                  <Button variant="link" onClick = {close} className="button">Confirm</Button>
                  <Button variant="link" onClick = {close} className="button">Cancel</Button>
                </p>
              </div>
            )}
          </Popup>
        </p>

        {/*Change password; asks for both old password and new pasword*/}
        <p>
          <Popup position="right center" trigger={<Button variant="link" className="button">Change Password</Button>}>
            {close =>(
              <div>
                <p className="popupTitle">Old Password</p>
                <p><input type="text" className="input"/></p>
                <p className="popupTitle">New Password</p>
                <p><input type="text" className="input"/></p>
                <p>
                  <Button variant="link" onClick = {close} className="button">Confirm</Button>
                  <Button variant="link" onClick = {close} className="button">Cancel</Button>
                </p>
              </div>
            )}
          </Popup>
        </p>

        {/*Delete Account*/}
        <p><Button variant="link" className="button">Delete Account</Button></p>
      
      </div>
    </div>
  )
}

export default Settings
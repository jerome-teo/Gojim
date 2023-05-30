import React from 'react'
import "./login.css"
import Button from 'react-bootstrap/Button';

const Login = () => {
  return (
    <div>
      <div className = "loginTitle">
        Sign In
      </div>

      {/*Sign-in Credentials*/}
      <div className = "signInCreds">
        <p>
        {/* <form action = "/action_page.php"> */}
        <label for = "username">
          Username:
          </label>
        <input type = "text" id = "username" name = "username" />
        {/* </form> */}
        </p>
        
        <p>
        {/* <form action = "/action_page.php"> */}
        <label for = "password">
          Password:
          </label>
        <input type = "text" id = "password" name = "password" />
        {/* </form> */}
        </p>
      </div>
    </div>
  )
}

export default Login
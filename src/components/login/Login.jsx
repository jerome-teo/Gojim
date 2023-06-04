import React from 'react'
import "./login.css"

const Login = () => {
  return (
    <div>
      <div className = "loginTitle">
        Sign In
      </div>

      {/*Sign-in Credentials*/}
      <form action="/profile">
        <div className = "signInCreds">
          <p>
          {/* <form action = "/action_page.php"> */}
          <label for = "username">
            Username:
            </label>
          <input className="usernameField" type = "text" id = "username" name = "username" />
          {/* </form> */}
          </p>
          
          <p>
          {/* <form action = "/action_page.php"> */}
          <label for = "password">
            Password:
            </label>
          <input className="psswdField" type = "text" id = "password" name = "password" />
          {/* </form> */}
          </p>
        </div>

        {/*Submit Button*/}
        <div className = "submitButton">
          <input type="submit" value="Submit" />
        </div>
      </form>

      {/*Signup button*/}
      <form action = "/signup">
        <div className = "signupButton">
          <input type="submit" value="No Account? Sign up Here!" />
        </div>
      </form>
    </div>
  )
}

export default Login
import React from 'react'
import "./login.css"

const Login = () => {
  return (
    <div>
      <div className = "title">
        Sign In
      </div>

      <form action="/profile">
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

        {/*Submit Button*/}
        <div className = "submitButton">
          <input type="submit" value="Submit" />
        </div>
      </form>
    </div>
  )
}

export default Login
import React, {useState} from 'react'
import "./login.css"


const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errorFlag, setErrorFlag] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent the form from submitting normally

    // Create a data object with the user's input
    const data = {
      username,
      password,
    };

    try {
      // Send a POST request to the backend endpoint '/sign-up'
      
      const response = await fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })
      console.log(JSON.stringify(data))
      //console.log("HERE")
      if (response.ok) {
        // Success response from the backend
        const jsonData = await response.json();
        console.log(jsonData)
        localStorage.setItem("username", JSON.stringify(username))
        // Do something with the response data if needed
        console.log("here is Login.jsx")
        console.log(localStorage.getItem("username"))
        setErrorFlag("0");
        window.location.href = '/';  

      } else {
        // Error response from the backend
        setErrorFlag("1");
        console.error('Error:');
        // Handle the error case accordingly
      }
      // setUsername("");
      // setPassword("");
    } catch (error) {
      console.error('Error:', error);
      // Handle any network or other errors
    }
    // window.location.href = '/';  
  };

  return (
    <div>
      <div className = "loginTitle">
        Log In
      </div>

      {/*Sign-in Credentials*/}
      <form action="/profile">
        <div className = "signInCreds">
          <p>
          {/* <form action = "/action_page.php"> */}
          <label for = "username">
            Username:
            </label>
          <input className="usernameField" type = "text" id = "username" name = "username" 
          value = {username}
          onChange={(e) => setUsername(e.target.value)}
          />
          {/* </form> */}
          </p>
          
          <p>
          {/* <form action = "/action_page.php"> */}
          <label for = "password">
            Password:
            </label>
          <input className="psswdField" type = "password" id = "password" name = "password" 
          value = {password}
          onChange={(e) => setPassword(e.target.value)}
          />
          {/* </form> */}
          </p>
        </div>

        {/*Submit Button*/}
        <div className = "submitButton" onClick={handleSubmit}>
          <input type="submit" value="Submit" />
          <p></p>
          {errorFlag === "1"? <div style={{color: "red"}}> Invalid Username or Password </div> : <div> </div>}
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
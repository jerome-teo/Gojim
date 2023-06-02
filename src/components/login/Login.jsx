import React, {useState, useEffect} from 'react'
import "./login.css"

const Login = () => {
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  // useEffect(() => {
  //   // Function to fetch data from the backend API
  //   const fetchData = async () => {
  //     try {
  //       const response = await fetch('/login'); // Replace with your API endpoint URL
  //       const jsonData = await response.json();
  //       setData(jsonData); // Update state with the fetched data
  //     } catch (error) {
  //       console.error('Error fetching data:', error);
  //     }
  //   };

  //   fetchData(); // Call the fetch data function
  // }, []);

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
          <input 
            type = "text" 
            id = "username" 
            name = "username" 
          />
          {/* </form> */}
          </p>
          
          <p>
          {/* <form action = "/action_page.php"> */}
          <label for = "password">
            Password:
            </label>
          <input 
            type = "text" 
            id = "password" 
            name = "password" 
          />
          {/* </form> */}
          </p>
        </div>

        {/*Submit Button*/}
        <div className = "submitButton">
          <input 
            type="submit" 
            value="Submit" 
          />
        </div>
      </form>

      {/*Signup button*/}
      <form action = "/signup">
        <div className = "signupButton">
          <input 
            type="submit" 
            value="No Account? Sign up Here!" 
          />
        </div>
      </form>
    </div>
  )
}

export default Login
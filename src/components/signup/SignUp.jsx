import React, {useState} from 'react'
import "./signup.css"

const SignUp = () => {
    const [email, setEmail] = useState("");
    const [username, setUsername] = useState("");
    const [password1, setPassword1] = useState("");
    const [password2, setPassword2] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault(); // Prevent the form from submitting normally
    
        // Create a data object with the user's input
        const data = {
          email,
          username,
          password1,
          password2,
        };
    
        try {
          // Send a POST request to the backend endpoint '/sign-up'
          const response = await fetch('http://localhost:5000/sign-up', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
          })
          if (response.ok) {
            // Success response from the backend
            const jsonData = await response.json();
            console.log(jsonData)
            // Do something with the response data if needed
            setEmail("RIGHT");
          } else {
            // Error response from the backend
            setEmail("WRONG");
            console.error('Error:');
            // Handle the error case accordingly
          }
        
          //setEmail("");
          setUsername("");
          setPassword1("");
          setPassword2("");
        } catch (error) {
          console.error('Error:', error);
          // Handle any network or other errors
        }
          
      };
    return (
        <div>
            <div className = "signUpTitle">
                Begin your workout by signing up today!
            </div>

            {/*Sign-in Credentials*/}
            <form action="/login">
                <div className = "signUpCreds">
                    <p>
                    <label for = "signUpUsername">
                        Choose a Username (8-16 characters long):
                    </label>
                    <input className="signUpUsernameField" type = "text" id = "signUpUsername" name = "signUpUsername"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    />
                    </p>
                
                    <p>
                    <label for = "signUpEmail">
                        Enter your email:
                    </label>
                    <input 
                      type = "text" 
                      id = "signUpEmail" 
                      name = "signUpEmail" 
                      value = {email}
                      onChange={(e) => setEmail(e.target.value)}
                    />
                    </p>

                    <p>
                    <label for = "signUpPassword">
                        Choose a Password (8-16 characters long):
                    </label>
                    <input className="signUpPsswdField" type = "password" id = "signUpPassword" name = "signUpPassword" 
                    value = {password1}
                    onChange={(e) => setPassword1(e.target.value)}
                    />
                    </p>

                    <p>
                    <label for = "signUpPassword2">
                        Confirm Password:
                    </label>
                    <input 
                    type = "password" 
                    id = "signUpPassword2" 
                    name = "signUpPassword2" 
                    value = {password2}
                    onChange={(e) => setPassword2(e.target.value)}
                    />
                    </p>
                </div>

                {/*Submit Button*/}
                <div className = "submitSignUp" onClick={handleSubmit}>
                    <input type="submit" value="Sign Up Now!" />
                </div>
            </form>
        </div>
    )
}

export default SignUp
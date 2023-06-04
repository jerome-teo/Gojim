import React from 'react'
import "./signup.css"

const SignUp = () => {
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
                    <input className="signUpUsernameField" type = "text" id = "signUpUsername" name = "signUpUsername" />
                    </p>
                
                    <p>
                    <label for = "signUpPassword">
                        Choose a Password (8-16 characters long):
                    </label>
                    <input className="signUpPsswdField" type = "text" id = "signUpPassword" name = "signUpPassword" />
                    </p>
                </div>

                {/*Submit Button*/}
                <div className = "submitSignUp">
                    <input type="submit" value="Sign Up Now!" />
                </div>
            </form>
        </div>
    )
}

export default SignUp
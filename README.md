# gojim
GoJim is an interactive webapp that allows users to share their preferred workout sequences and view others' created workouts as well. Given the overwhelming abundance of knowledge about health and fitness online, some of which may be contradictory or conflicting due to disagreements, we wanted to provide a centralized platform that encourages user sharing and interaction for exchange of ideas, which has the potential for more complex/meaningful interfaction. 

GoJim functions on a React.js-based front-end technology and a Flask backend application. The React interface is responsible for the user interface, providing a simple, easy-to-understand medium for query-making and display of data from the backend. The Flask application is necessary to implement API endpoints for data processing, storage, verification, and filtering using the implementation of logic to declare suitable SQLAlchemy databases. The Flask app connects and facilitates communication between the frontend and the database. For signup, the inputs are sent from the React app to the Flask app to check for existing accounts with identical credentials. For the login, the React app stores and retrieves the user’s authentication information in/from LocalStorage, which is important to give access to other functionalities like Create Workout/Saved/My Workouts that are user-specific because this will be used to query for information tagged with the unique username in the backend/database. As such, logging out/deleting the account clears the LocalStorage and removes access to said functionalities. 

**Key Features**
- Users can create accounts on the signup page and authenticate using the login page to access their account information.
- Users can search for workouts of specific tags.
- Users can create lists of their favorite sequence of exercises under a single workout and upload it to their profile
- Users can interact with others' posts in the form of likes and saves.
- Users can customize their privacy settings, change their username, email and password on the settings page.
- Users and non-users can view a home page where workout routines shared by all public accounts are visible on a feed.

**Running the Web App:**

    git clone https://github.com/Jeromeoui/gojim
    cd gojim
    cd backend
    cd src

**Set up the backend server:**

    python __init__.py
  
The flask app will be accessible at http://localhost:5000 so you can view it in the browser.

To ensure that the necessary libraries can be accessed, you would need to install:
- flask
- flask_login
- sqlalchemy
- sqlalchemy.orm
- flask_cors
- flask_jwt_extended

  pip install {library}

**Run the frontend application:**

Open another terminal
  
    cd src
  
    npm install
    
    (optional) npm install --legacy-peer-deps # if there are dependencies in your package that you need to bypass
  
    npm start
 

The React app will be accessible at http://localhost:3000 so you can view it in the browser.

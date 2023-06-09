# gojim
GoJim is an interactive webapp that allows users to share their preferred workout sequences and view others' created workouts as well.

**Key Features**
- Users can create accounts on the signup page and authenticate using the login page to access their account information.
- Users can search for workouts of specific tags.
- Users can create lists of their favorite sequence of exercises under a single workout and upload it to their profile
- Users can interact with others' posts in the form of likes.
- Users can customize their privacy settings, change their username and password on the settings page.
- Users and non-users can view a home page where relevant articles shared by others are visible on a feed.

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

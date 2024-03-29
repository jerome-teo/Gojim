import requests
import json

def test_login():
    response = requests.post('http://127.0.0.1:5000/login', data={'username':'shivani', 'password':'hello1234'})
    print(response)
    if response.status_code == 200:
        print("hello")
    elif response.status_code == 401:
        print('Unsuccessful login')


def test_signup():
    response = requests.post('http://127.0.0.1:5000/sign-up', headers = {'Content-Type': 'application/json'}, data={'email':'tims@gmail.com', 'username':'timsmith', 'password1':'hello12345', 'password2':'hello12345'})
    # print(response.text)
    if response.status_code == 200:
        print('successful account created')
    elif response.status_code == 401:
        print('account not created')

def test_new_workout():
    response = requests.post('http://127.0.0.1:5000/create-new-workout', headers = {"Content-Type": "application/json"}, 
                             data={"workoutName":"Train Upper", "workoutString":"lats, reps: 8, sets: 10", "tagString":"upper\nchest", "owner":"hello123"})
    # print(response.content)
    # print(response.text)
    data = response.text
    try:
        data_json = json.loads(data)
        print(data_json)
    except json.JSONDecodeError:
        print("Empty response")
    # print(json.loads(response.content).decode("utf-8"))
    if response.status_code == 200:
        print('workout list created')
    elif response.status_code == 500:
        print('workout list not created')

def test_get_my_workouts():
    response = requests.get('http://127.0.0.1:5000/get-my-workouts')
    # print(response.text)
    if response.status_code == 200:
        print('workout retrieved')
    elif response.status_code == 500:
        print('workout not retrieved')

if __name__=='__main__':
    # test_login()
    # test_signup()
    test_new_workout()
    # test_get_my_workouts()
    pass
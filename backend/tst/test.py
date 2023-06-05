import requests

def test_login():
    response = requests.post('http://127.0.0.1:5000/login', data={'username':'shivani', 'password':'hello1234'})
    if response.status_code == 200:
        print("hello")
    elif response.status_code == 401:
        print('Unsuccessful login')


def test_logout():
    response = requests.post('http://127.0.0.1:5000/sign-up', headers = {'Content-Type': 'application/json'}, data={'email':'tims@gmail.com', 'username':'timsmith', 'password1':'hello12345', 'password2':'hello12345'})
    if response.status_code == 200:
        print('successful account created')
    elif response.status_code == 401:
        print('account not created')

def test_new_workout():
    response = requests.post('http://127.0.0.1:5000/create-new-workout', data={'name':'train upper', 'info':'lats, reps: 8, sets: 10', 'tags':'upper,chest'})
    print(response.json())
    if response.status_code == 200:
        print('workout list created')
    elif response.status_code == 500:
        print('workout list not created')

def test_get_my_workouts():
    response = requests.get('http://127.0.0.1:5000/get-my-workouts')
    # print(response.json())
    if response.status_code == 200:
        print('workout retrieved')
    elif response.status_code == 500:
        print('workout not retrieved')

if __name__=='__main__':
    #test_login()
    test_logout()
    #test_new_workout()
    #test_get_my_workouts()
    pass
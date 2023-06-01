import requests


def test_login():
    response = requests.post('http://127.0.0.1:5000/login', data={'username':'shivani', 'password':'hello1234'})
    if response.status_code == 200:
        print(response.json())
    elif response.status_code == 401:
        print('Unsuccessful login')


def test_logout():
    pass

if __name__=='__main__':
    test_login()
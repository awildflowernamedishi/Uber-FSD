from fastapi import FastAPI
import random
from datetime import datetime

app = FastAPI()

user_coll = [{
    "id": 1,
    "name": 'Ateen',
    "email":"ateen@psit.ac.in",
    "password": "ateen123",
    "created_at": "31-07-2023 18:19:00"

},{
    "id": 2,
    "name": 'Aditi',
    "email":"aditi@psit.ac.in",
    "password": "aditi456",
    "created_at": "31-07-2023 18:20:00"
}
]

@app.get('/')
def greet():
    return 'this is using fast api'

@app.post('/api/v1/signup')
def signup(user_obj: dict):
    for user in user_coll:
        if user_obj['email'] == user['email']:
            return {"status": "failure", "message": "error! user already signed up..","data":{}}
    user_dict = {}
    user_dict['id'] = random.randint(1, 9999999)
    user_dict['name'] = user_obj['name']
    user_dict['email'] = user_obj['email']
    user_dict['password'] = user_obj['password']
    user_dict['created_at'] = datetime.utcnow()

    user_coll.append(user_dict)

    return {"status": "success", "message": "OK", "data":user_dict}


@app.get('/api/v1/greet_me/{firstname}/{lastname}')
def greet_me(firstname: str,lastname: str):
    return {"status": "success", "message": f'hello {firstname} {lastname}'}



@app.post('/api/v1/signin')
def signin(user_req: dict):
    for user in user_coll:
        if user_req['email'] == user['email']:
            if user_req['password'] == user['password']:
                return {"status": "success", "message": "OK", "access_token":user['id'], "expiry":60}

    return {"status": "failure", "message": "invalid credentials", "access_token":None, "expiry":0}
# /nearby/drivers'

@app.post('/api/v1/search/nearby_drivers')
def nearby_drivers(access_token: str):
    pass

@app.get('/api/v1/users')
def get_all_users():
    return user_coll

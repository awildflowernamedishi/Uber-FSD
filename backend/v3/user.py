from fastapi import APIRouter,Response
import utils,random,models,database_manager
from datetime import datetime
from typing import List

router = APIRouter()

@router.post('/api/v2/signup')
async def signup(user_obj: models.UserCreateRequest):
    db = database_manager.get_db()
    user_coll = db.user_coll
    user_obj = user_obj.dict()
    result = await user_coll.find_one({"email": user_obj['email']})
    if result:
        return {"status": "failure", "message": "error! user already signed up..","data":{}}
    user_dict = {}
    user_dict['id'] = random.randint(1, 9999999)
    user_dict['name'] = user_obj['name']
    user_dict['email'] = user_obj['email']
    # hashing the password 
    hashed_password = utils.hash(user_obj['password'])
    user_dict['password'] = hashed_password
    user_dict['created_at'] = datetime.utcnow()

    user_coll.insert_one(user_dict)

    return user_dict

@router.post('/api/v2/signin')
async def signin(user_req: dict,response: Response):
    db = database_manager.get_db()
    user_coll = db.user_coll
    user_doc = await user_coll.find_one({"email": user_req['email']})
    if user_doc:
        if utils.hash(user_req['password']) == user_doc['password']:
            # set cookie
            response.set_cookie("access_token",user_doc['id'])    
            return {"status": "success", "message": "OK", "access_token":user_doc['id'], "expiry":60}

    return {"status": "failure", "message": "invalid credentials", "access_token":None, "expiry":0}

@router.get('/api/v2/users',response_model=List[models.UserCreateResponse])
async def get_all_users():
    db = database_manager.get_db()
    user_coll = db.user_coll
    documents = user_coll.find({})
    result = []
    async for document in documents:
        result.append(models.UserCreateResponse(**document))
    return result

@router.post('/api/v2/signout')
async def signin(response: Response):
    response.delete_cookie("access_token")    
    return {"status": "success", "message": "signed out!", "access_token":None, "expiry":0}
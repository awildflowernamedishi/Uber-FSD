from fastapi import APIRouter
import models,database_manager


router = APIRouter()
db = database_manager.get_db()
user_coll = db.user_coll


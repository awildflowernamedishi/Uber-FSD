from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v2/greet_me/{firstname}/{lastname}')
def greet_me(firstname: str,lastname: str):
    return {"status": "success", "message": f'hello {firstname} {lastname}'}
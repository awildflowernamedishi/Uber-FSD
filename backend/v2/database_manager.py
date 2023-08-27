from motor.motor_asyncio import AsyncIOMotorClient

uri = 'mongodb://localhost:27017/'
client = AsyncIOMotorClient(uri)

database = client.auth_db

def get_db():
    return database

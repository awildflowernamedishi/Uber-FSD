from fastapi import FastAPI
import user,driver,greet

app = FastAPI()

@app.get('/')
def root():
    return 'this is using fast api'

app.include_router(user.router)
app.include_router(driver.router)
app.include_router(greet.router)
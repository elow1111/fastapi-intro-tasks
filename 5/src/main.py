from fastapi import FastAPI, Body
from typing import Optional

app = FastAPI()

# BEGIN (write your solution here)
@app.post("/users", status_code=200)
async def create_task(username:str = Body(...), email:str = Body(...), age:Optional[int] = Body(None)):
    new_user = {
        "username": username,
        "email": email,
        "age": age
    }
    new_user["status"] = "User created"
    return new_user
# END

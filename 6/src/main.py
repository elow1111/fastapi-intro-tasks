from fastapi import FastAPI, Form

app = FastAPI()

# BEGIN (write your solution here)
@app.post("/login", status_code=200)
async def create_task(username:str = Form(...), password:str = Form(...)):
    new_user = {
        "username": username,
        "password": password,
    }
    new_user["status"] = "Login successful"
    return new_user
# END

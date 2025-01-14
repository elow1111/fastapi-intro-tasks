from fastapi import FastAPI, Path

app = FastAPI()

# BEGIN (write your solution here)
from fastapi import HTTPException
@app.get("/users/{user_id}")
async def get_user_id(user_id):
    user_id = int(user_id)
    if user_id<=0:
        raise HTTPException(status_code=422, detail="Недопустимое значение числа")
    return {"user_id": user_id}
# END

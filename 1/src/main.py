from fastapi import FastAPI

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/reverse/{text}")
async def get_all_tasks(text):
    return {"reversed": text[::-1]}
# END

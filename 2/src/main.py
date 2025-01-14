from fastapi import FastAPI, Query
app = FastAPI()

# BEGIN (write your solution here)
from fastapi import HTTPException
@app.get("/filter")
async def get_min_and_max(min=0, max=100):
    min, max = [int(min), int(max)]
    if min < 0 or max > 100:
        raise HTTPException(status_code=422, detail="Недопустимое значение минимального или мачимального числа")
    return {"min": min, "max": max}
# END

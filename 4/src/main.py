from fastapi import FastAPI, Cookie

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/language")
async def get_language(language = Cookie(default=None)):
    if language:
        return {"language": language}
    return {'message': "Language not set"}
# END

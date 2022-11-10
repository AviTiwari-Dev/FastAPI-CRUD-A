from fastapi import FastAPI

person_api = FastAPI()


@person_api.get("/home")
async def home():
    return "Welcome Home"

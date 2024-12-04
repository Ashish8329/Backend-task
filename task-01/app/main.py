from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import database
from app.crud import create_user, get_users
from app.schemas import UserCreate, UserRead

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    await database.connect()
    yield
    # Shutdown actions
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

@app.post("/users/", response_model=UserRead)
async def add_user(user: UserCreate):
    user_data = await create_user(user.name, user.email)
    return user_data

@app.get("/users/", response_model=list[UserRead])
async def list_users():
    return await get_users()

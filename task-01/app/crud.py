from sqlalchemy import insert, select
from app.models import User
from app.database import database

async def create_user(name: str, email: str):
    query = insert(User).values(name=name, email=email).returning(User.id, User.name, User.email)
    result = await database.fetch_one(query)
    return {"id": result["id"], "name": result["name"], "email": result["email"]}

async def get_users():
    query = select(User)
    return await database.fetch_all(query)

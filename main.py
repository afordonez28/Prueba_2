from fastapi import FastAPI, HTTPException, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from data.models import User, Pet
from data.connection_db import init_db, get_session
from data import operations_db

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

# --- Usuarios ---
@app.get("/users")
async def list_users(session: AsyncSession = Depends(get_session)):
    return await operations_db.get_users(session)

@app.get("/users/{user_id}")
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await operations_db.get_user_by_id(user_id, session)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@app.post("/users")
async def create_user(user: User, session: AsyncSession = Depends(get_session)):
    return await operations_db.create_user(user, session)

# --- Mascotas ---
@app.get("/pets")
async def list_pets(session: AsyncSession = Depends(get_session)):
    return await operations_db.get_all_pets(session)

@app.post("/pets")
async def create_pet(pet: Pet, session: AsyncSession = Depends(get_session)):
    return await operations_db.create_pet(pet, session)
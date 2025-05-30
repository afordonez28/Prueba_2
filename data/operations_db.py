from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from data.models import User, Pet

# --- Usuarios ---
async def create_user(user: User, session: AsyncSession):
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

async def get_users(session: AsyncSession):
    result = await session.exec(select(User))
    return result.all()

async def get_user_by_id(user_id: int, session: AsyncSession):
    return await session.get(User, user_id)

# --- Mascotas ---
async def create_pet(pet: Pet, session: AsyncSession):
    session.add(pet)
    await session.commit()
    await session.refresh(pet)
    return pet

async def get_all_pets(session: AsyncSession):
    result = await session.exec(select(Pet))
    return result.all()

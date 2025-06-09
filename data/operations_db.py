from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from data.models import Cliente, Vehiculo, ZonaParqueo, RegistroParqueo, Tarifa

# --- Clientes ---
async def create_cliente(cliente: Cliente, session: AsyncSession):
    session.add(cliente)
    await session.commit()
    await session.refresh(cliente)
    return cliente

async def get_clientes(session: AsyncSession):
    result = await session.exec(select(Cliente))
    return result.all()


# --- Vehículos ---
async def create_vehiculo(vehiculo: Vehiculo, session: AsyncSession):
    session.add(vehiculo)
    await session.commit()
    await session.refresh(vehiculo)
    return vehiculo

async def get_vehiculos(session: AsyncSession):
    result = await session.exec(select(Vehiculo))
    return result.all()


# --- Zonas ---
async def get_zonas_disponibles(session: AsyncSession):
    result = await session.exec(select(ZonaParqueo).where(ZonaParqueo.disponible == True))
    return result.all()


# --- Registro de Parqueo ---
async def registrar_entrada(registro: RegistroParqueo, session: AsyncSession):
    session.add(registro)
    await session.commit()
    await session.refresh(registro)
    return registro

from fastapi import FastAPI, HTTPException, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from data.models import Cliente, Vehiculo, ZonaParqueo, RegistroParqueo
from data.connection_db import init_db, get_session
from data.operations_db import (
    create_cliente, get_clientes,
    create_vehiculo, get_vehiculos,
    get_zonas_disponibles, registrar_entrada
)

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

# --- Clientes ---
@app.post("/clientes")
async def add_cliente(cliente: Cliente, session: AsyncSession = Depends(get_session)):
    return await create_cliente(cliente, session)

@app.get("/clientes")
async def list_clientes(session: AsyncSession = Depends(get_session)):
    return await get_clientes(session)

# --- Vehículos ---
@app.post("/vehiculos")
async def add_vehiculo(vehiculo: Vehiculo, session: AsyncSession = Depends(get_session)):
    return await create_vehiculo(vehiculo, session)

@app.get("/vehiculos")
async def list_vehiculos(session: AsyncSession = Depends(get_session)):
    return await get_vehiculos(session)

# --- Zonas disponibles ---
@app.get("/zonas/disponibles")
async def zonas_disponibles(session: AsyncSession = Depends(get_session)):
    return await get_zonas_disponibles(session)

# --- Registro de entrada ---
@app.post("/registro/entrada")
async def registrar_vehiculo(registro: RegistroParqueo, session: AsyncSession = Depends(get_session)):
    return await registrar_entrada(registro, session)
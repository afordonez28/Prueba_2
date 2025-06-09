from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship


class Cliente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    telefono: str
    frecuente: bool = False


class Vehiculo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    placa: str
    tipo: str  # Ej: "carro", "moto"
    color: Optional[str]
    cliente_id: int = Field(foreign_key="cliente.id")


class ZonaParqueo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str  # Ej: "derecha", "centro"
    tipo: str    # "cubierta", "descubierta", "premium"
    disponible: bool = True


class Tarifa(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tipo_zona: str
    tipo_vehiculo: str
    valor: float


class RegistroParqueo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    vehiculo_id: int = Field(foreign_key="vehiculo.id")
    zona_id: int = Field(foreign_key="zonaparqueo.id")
    fecha_entrada: datetime
    fecha_salida: Optional[datetime]
    ticket_generado: bool = False

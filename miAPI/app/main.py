#Importaciones
from fastapi import FastAPI
from app.routers import usuarios,varios

# Instacia del servidor
app = FastAPI(
    title='MI primer API',
    description='Ivan Isay Guerra',
    version='1.0.0'
    )

app.include_router(usuarios.router)
app.include_router(varios.router)




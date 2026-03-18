
#Endpoints usuarios

from fastapi import status,HTTPException, Depends, APIRouter
from app.models.usuario import usuario_create
from app.data.database import usuarios
from app.security.auth import verificar_Peticion

router = APIRouter(
    prefix= "/v1/usuarios", tags=["CRUD HTTP"]
)

@router.get("/")
async def leer_usuarios( ):
    return{
        "status":"200",
        "total": len(usuarios),
        "usuarios":usuarios
    }
    
@router.post("/",status_code=status.HTTP_201_CREATED)
async def crear_usuario(usuario:usuario_create):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(
                status_code=400,
                detail="El id ya existe"
            )
    usuarios.append(usuario)
    return{
        "mensaje":"Usuario Agregado",
        "Usuario":usuario
    }
    

@router.put("/{id}", status_code=status.HTTP_200_OK)
async def actualizar_usuario(id: int, usuario_actualizado: dict):

    for index, usr in enumerate(usuarios):
        if usr["id"] == id:

            # Reemplazamos completamente el usuario
            usuarios[index] = usuario_actualizado

            return {
                "message": "Usuario actualizado completamente",
                "data": usuario_actualizado
            }

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )
    
@router.patch("/{id}",status_code=status.HTTP_200_OK)
async def actualizar_parcial(id: int, datos: dict):

    for usr in usuarios:
        if usr["id"] == id:

            # Actualización parcial
            usr.update(datos)

            return {
                "message": "Usuario actualizado parcialmente",
                "data": usr
            }

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )
    
@router.delete("/{id}",status_code=status.HTTP_200_OK)
async def eliminar_usuario(id: int, userAuth:str= Depends(verificar_Peticion)):

    for index, usr in enumerate(usuarios):
        if usr["id"] == id:

            usuarios.pop(index)

            return {
                "message": f"Usuario eliminado por: {userAuth}"
            }

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


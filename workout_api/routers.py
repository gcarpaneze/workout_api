from fastapi import APIRouter

from workout_api.atleta.controller import router as atleta
from workout_api.categorias.controller import router as categoria
from workout_api.centro_treinamento.controller import router as centro_treinamento

api_router = APIRouter()

api_router.include_router(router=atleta, prefix="/atletas", tags=["atletas"])
api_router.include_router(router=categoria, prefix="/categorias", tags=["categorias"])
api_router.include_router(
    router=centro_treinamento, prefix="/centro_treinamento", tags=["centro_treinamento"]
)

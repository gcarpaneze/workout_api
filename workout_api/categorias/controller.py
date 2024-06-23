from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException, status
from sqlalchemy.future import select

from workout_api.categorias.models import CategoriaModel
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut
from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter()


@router.post(
    "/",
    summary="Criar nova categoria",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut,
)
async def post(
    db_session: DatabaseDependency, categoriaIn: CategoriaIn = Body(...)
) -> CategoriaOut:
    categoria_out = CategoriaOut(id=uuid4(), **categoriaIn.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())

    db_session.add(categoria_model)
    await db_session.commit()

    return categoria_out


@router.get(
    "/",
    summary="Buscar todas as categorias",
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaOut],
)
async def query(db_session: DatabaseDependency) -> list[CategoriaOut]:
    categorias = (await db_session.execute(select(CategoriaModel))).scalars().all()

    return categorias


@router.get(
    "/{id}",
    summary="Buscar uma categoria pelo ID",
    status_code=status.HTTP_200_OK,
    response_model=CategoriaOut,
)
async def query(id, db_session: DatabaseDependency) -> CategoriaOut:
    categoria = (
        (await db_session.execute(select(CategoriaModel).filter_by(id=id)))
        .scalars()
        .first()
    )

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com o {id} não encontrada",
        )

    return categoria

from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException, status
from sqlalchemy.future import select

from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.centro_treinamento.schemas import (
    CentroTreinamentoIn,
    CentroTreinamentoOut,
)
from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter()


@router.post(
    "/",
    summary="Criar um novo centro de treinamento",
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut,
)
async def post(
    db_session: DatabaseDependency, centroTreinamentoIn: CentroTreinamentoIn = Body(...)
) -> CentroTreinamentoOut:
    centro_treinamento_out = CentroTreinamentoOut(
        id=uuid4(), **centroTreinamentoIn.model_dump()
    )
    categoria_model = CentroTreinamentoModel(**centro_treinamento_out.model_dump())

    db_session.add(categoria_model)
    await db_session.commit()

    return centro_treinamento_out


@router.get(
    "/",
    summary="Buscar todos os centros de treinamento",
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoOut],
)
async def query(db_session: DatabaseDependency) -> list[CentroTreinamentoOut]:
    centros_de_treinamento = (
        (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()
    )

    return centros_de_treinamento


@router.get(
    "/{id}",
    summary="Buscar um centro de treinamento pelo ID",
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoOut,
)
async def query(id, db_session: DatabaseDependency) -> CentroTreinamentoOut:
    centro_treinamento = (
        (await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id)))
        .scalars()
        .first()
    )

    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Centro de treinamento com o {id} não encontrado",
        )

    return centro_treinamento

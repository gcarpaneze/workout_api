from typing import Annotated, Literal, Optional

from pydantic import ConfigDict, Field, PositiveFloat
from typing_extensions import Unpack

from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta
from workout_api.contrib.schemas import BaseSchema, OutMixin


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta")]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta")]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta")]
    sexo: Annotated[
        Literal["M", "F"], Field(description="Sexo do atleta", max_length=1)
    ]

    categoria: Annotated[CategoriaIn, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[
        CentroTreinamentoAtleta, Field(description="Centro de treinamento do atleta")
    ]


class AtletaIn(Atleta):
    pass


class AtletaOut(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta", max_length=50)]
    categoria: Annotated[CategoriaIn, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[
        CentroTreinamentoAtleta, Field(description="Centro de treinamento do atleta")
    ]


class AtletaUpdate(BaseSchema):
    nome: Annotated[
        Optional[str], Field(None, description="Nome do atleta", max_length=50)
    ]
    idade: Annotated[Optional[int], Field(None, description="Idade do atleta")]

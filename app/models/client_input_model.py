
from dataclasses import Field
from typing import Annotated
from pydantic import BaseModel, Field


class ClientInput(BaseModel):
    days: Annotated[int | None, Field(
        ge=0,
        le=10000,
    )]
    is_month_to_month: Annotated[int | None, Field(
        ge=0,
        le=1,
    )]
    is_fiber_optic: Annotated[int | None, Field(
        ge=0,
        le=1,
    )]
    is_electronic_check: Annotated[int | None, Field(
        ge=0,
        le=1,
    )]
    internet: Annotated[int | None, Field(
        ge=0,
        le=1,
    )]

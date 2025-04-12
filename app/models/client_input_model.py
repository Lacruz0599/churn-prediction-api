
from dataclasses import Field
from typing import Annotated
from pydantic import BaseModel, Field


class ClientInput(BaseModel):
    days: Annotated[int | None, Field()]
    is_month_to_month: Annotated[int | None, Field()]
    is_optical_fiber: Annotated[int | None, Field()]
    internet: Annotated[int | None, Field()]

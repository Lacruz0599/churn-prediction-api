
from dataclasses import Field
from typing import Annotated
from pydantic import BaseModel, Field


class Client(BaseModel):
    days: Annotated[int | None, Field()]
    internet_service: bool
    phone_service: bool

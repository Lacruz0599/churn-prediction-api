# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


# # Parametros de query
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#     user_id: int, item_id: str, q: str | None = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item
# #http://127.0.0.1:8000/users/3456/items/foo?short=1&q=cftctyvg


# Request body
# from fastapi import FastAPI
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# app = FastAPI()

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.model_dump()}
#     if q:
#         result.update({"q": q})
#     return result


# Validation data string
# from typing import Annotated
# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         str | None,
#         Query(  # Query es la verificacion para los parametros query, tambien hay path, body, etc
#             title="Query string",
#             description="Query string for the items to search in the database that have a good match",
#             min_length=3,
#         ),
#     ] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# path an number validation
# from typing import Annotated
# from fastapi import FastAPI, Path, Query

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
#     q: str,
#     size: Annotated[float, Query(gt=0, lt=10.5)],
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if size:
#         results.update({"size": size})
#     return results


# Modelos para parametros y prohibir parametros extra
# from typing import Annotated, Literal
# from fastapi import FastAPI, Query
# from pydantic import BaseModel, Field

# app = FastAPI()

# class FilterParams(BaseModel):
#     model_config = {"extra": "forbid"}

#     limit: int = Field(100, gt=0, le=100)
#     offset: int = Field(0, ge=0)
#     order_by: Literal["created_at", "updated_at"] = "created_at"
#     tags: list[str] = []

# @app.get("/items/")
# async def read_items(filter_query: Annotated[FilterParams, Query()]):
#     return filter_query


# Multiples parametros del body
# from typing import Annotated
# from fastapi import Body, FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# class User(BaseModel):
#     username: str
#     full_name: str | None = None

# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int,
#     item: Item,
#     user: User,
#     # embed=True es un parametro especial, investigalo
#     importance: Annotated[int, Body(gt=0)],
#     q: str | None = None,
# ):
#     results = {"item_id": item_id, "item": item,
#                "user": user, "importance": importance}
#     if q:
#         results.update({"q": q})
#     return results


# fiel para validar parametros body
# from typing import Annotated
# from fastapi import Body, FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = Field(
#         default=None, title="The description of the item", max_length=300
#     )
#     price: float = Field(gt=0, description="The price must be greater than zero")
#     tax: float | None = None

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
#     results = {"item_id": item_id, "item": item}
#     return results


# Ejemplo de respuesta con reducción de datos en la salida
# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()

# class BaseUser(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None

# class UserIn(BaseUser):
#     password: str

# @app.post("/user/")
# async def create_user(user: UserIn) -> BaseUser:
#     return user


# Handling errors
# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse

# class UnicornException(Exception):
#     def __init__(self, name: str):
#         self.name = name

# app = FastAPI()

# @app.exception_handler(UnicornException)
# async def unicorn_exception_handler(request: Request, exc: UnicornException):
#     return JSONResponse(
#         status_code=418,
#         content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
#     )

# @app.get("/unicorns/{name}")
# async def read_unicorn(name: str):
#     if name == "yolo":
#         raise UnicornException(name=name)
#     return {"unicorn_name": name}


from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

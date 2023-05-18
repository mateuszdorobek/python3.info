.. testsetup::

    # doctest: +SKIP_FILE


FastAPI Dependencies
====================
* CDI - Content Dependency Injection
* Used when you have functions which takes the same thing (for example parameters)
* If one of your dependencies is declared multiple times for the same path operation, for example, multiple dependencies have a common sub-dependency, FastAPI will know to call that sub-dependency only once per request.
* And it will save the returned value in a "cache" and pass it to all the "dependants" that need it in that specific request, instead of calling the dependency multiple times for the same request.


Function
--------
>>> from fastapi import Depends, FastAPI
>>>
>>> app = FastAPI()
>>>
>>>
>>> async def common_parameters(q: str | None = None,
...                             skip: int = 0,
...                             limit: int = 100) -> dict:
...     return {"q": q, "skip": skip, "limit": limit}
>>>
>>>
>>> @app.get("/items/")
... async def read_items(commons: dict = Depends(common_parameters)):
...     return commons
>>>
>>>
>>> @app.get("/users/")
... async def read_users(commons: dict = Depends(common_parameters)):
...     return commons


Class
-----
>>> from fastapi import Depends, FastAPI
>>>
>>> app = FastAPI()
>>>
>>>
>>> fake_items_db = [
...     {"item_name": "Foo"},
...     {"item_name": "Bar"},
...     {"item_name": "Baz"},
... ]
>>>
>>>
>>> class CommonQueryParams:
...     def __init__(self, q: str | None = None,
...                  skip: int = 0,
...                  limit: int = 100):
...         self.q = q
...         self.skip = skip
...         self.limit = limit
>>>
>>>
>>> @app.get("/items/")
... async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
...     response = {}
...     if commons.q:
...         response.update({"q": commons.q})
...     items = fake_items_db[commons.skip : commons.skip + commons.limit]
...     response.update({"items": items})
...     return response


Shortcut
--------
* FastAPI provides a shortcut injecting classes
* ``commons: CommonQueryParams = Depends()``

Instead of writing:

>>> commons: CommonQueryParams = Depends(CommonQueryParams)

you write:

>>> commons: CommonQueryParams = Depends()


Dependencies in path operation decorators
-----------------------------------------
* In some cases you don't really need the return value of a dependency inside your path operation function.
* Or the dependency doesn't return a value.
* But you still need it to be executed/solved.
* For those cases, instead of declaring a path operation function parameter with Depends, you can add a list of dependencies to the path operation decorator.

>>> from fastapi import Depends, FastAPI, Header, HTTPException
>>>
>>> app = FastAPI()
>>>
>>>
>>> async def verify_token(x_token: str = Header(...)):
...     if x_token != "fake-super-secret-token":
...         raise HTTPException(status_code=400, detail="X-Token header invalid")
>>>
>>>
>>> async def verify_key(x_key: str = Header(...)):
...     if x_key != "fake-super-secret-key":
...         raise HTTPException(status_code=400, detail="X-Key header invalid")
...     return x_key
>>>
>>>
>>> @app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
... async def read_items():
...     return [
...         {"item": "Foo"},
...         {"item": "Bar"},
...     ]


Global Dependencies
-------------------
* For some types of applications you might want to add dependencies to the whole application.

>>> from fastapi import Depends, FastAPI, Header, HTTPException
>>>
>>>
>>> async def verify_token(x_token: str = Header(...)):
...     if x_token != "fake-super-secret-token":
...         raise HTTPException(status_code=400, detail="X-Token header invalid")
>>>
>>>
>>> async def verify_key(x_key: str = Header(...)):
...     if x_key != "fake-super-secret-key":
...         raise HTTPException(status_code=400, detail="X-Key header invalid")
...     return x_key
>>>
>>>
>>> app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])
>>>
>>>
>>> @app.get("/items/")
... async def read_items():
...     return [
...         {"item": "Portal Gun"},
...         {"item": "Plumbus"},
...     ]
>>>
>>>
>>> @app.get("/users/")
... async def read_users():
...     return [
...         {"username": "Rick"},
...         {"username": "Morty"},
...     ]


Router Based Dependencies
-------------------------
>>> from fastapi import APIRouter, Depends, HTTPException
>>> from ..dependencies import get_token_header
>>>
>>> router = APIRouter(
...     prefix="/items",
...     tags=["items"],
...     dependencies=[Depends(get_token_header)],
...     responses={404: {"description": "Not found"}},
... )
>>>
>>>
>>> fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}
>>>
>>>
>>> @router.get("/")
... async def read_items():
...     return fake_items_db
>>>
>>>
>>> @router.get("/{item_id}")
... async def read_item(item_id: str):
...     if item_id not in fake_items_db:
...         raise HTTPException(status_code=404, detail="Item not found")
...     return {"name": fake_items_db[item_id]["name"], "item_id": item_id}
>>>
>>>
>>> @router.put(
...     "/{item_id}",
...     tags=["custom"],
...     responses={403: {"description": "Operation forbidden"}},
... )
... async def update_item(item_id: str):
...     if item_id != "plumbus":
...         raise HTTPException(
...             status_code=403, detail="You can only update the item: plumbus"
...         )
...     return {"item_id": item_id, "name": "The great Plumbus"}

>>> from fastapi import Depends, FastAPI
>>> from .dependencies import get_query_token, get_token_header
>>> from .internal import admin
>>> from .routers import items, users
>>>
>>> app = FastAPI(dependencies=[Depends(get_query_token)])
>>>
>>>
>>> app.include_router(users.router)
>>> app.include_router(items.router)
>>> app.include_router(
...     admin.router,
...     prefix="/admin",
...     tags=["admin"],
...     dependencies=[Depends(get_token_header)],
...     responses={418: {"description": "I'm a teapot"}},
... )
>>>
>>>
>>> @app.get("/")
... async def root():
...     return {"message": "Hello Bigger Applications!"}


Dependencies with yield
-----------------------
* FastAPI supports dependencies that do some extra steps after finishing.*
* To do this, use yield instead of return, and write the extra steps after.
* It might be tempting to raise an HTTPException or similar in the exit code, after the yield. But it won't work.
* The exit code in dependencies with yield is executed after the response is sent
* Only one response will be sent to the client.
* After one of those responses is sent, no other response can be sent.

>>> async def get_db():
...     db = DBSession()
...     try:
...         yield db
...     finally:
...         db.close()


>>> class MyDatabase:
...     def __init__(self):
...         self.db = DBSession()
...
...     def __enter__(self):
...         return self.db
...
...     def __exit__(self, exc_type, exc_value, traceback):
...         self.db.close()
>>>
>>>
>>> async def get_db():
...     with MyDatabase() as db:
...         yield db

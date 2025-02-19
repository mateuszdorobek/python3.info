FastAPI Test Sync
=================
* ``pytest``
* ``unittest``
* PyCharm PRO HTTP Runner
* https://www.jetbrains.com/help/pycharm/http-response-handling-examples.html


Sync
----
>>> from fastapi import FastAPI
>>> from fastapi.testclient import TestClient
>>>
>>> app = FastAPI()
>>> client = TestClient(app)
>>>
>>>
>>> @app.get("/")
... async def read_main():
...     return {"msg": "Hello World"}
>>>
>>>
>>> def test_read_main():
...     response = client.get("/")
...     assert response.status_code == 200
...     assert response.json() == {"msg": "Hello World"}


Use Case
--------
>>> from fastapi import FastAPI
>>> from fastapi.testclient import TestClient
>>>
>>> app = FastAPI()
>>> client = TestClient(app)
>>>
>>>
>>> @app.get("/")
... async def read_main():
...     return {"msg": "Hello World"}
>>>
>>>
>>> def test_read_item():
...     response = client.get("/items/foo", headers={"X-Token": "coneofsilence"})
...     assert response.status_code == 200
...     assert response.json() == {
...         "id": "foo",
...         "title": "Foo",
...         "description": "There goes my hero",
...     }
>>>
>>>
>>> def test_read_item_bad_token():
...     response = client.get("/items/foo", headers={"X-Token": "hailhydra"})
...     assert response.status_code == 400
...     assert response.json() == {"detail": "Invalid X-Token header"}
>>>
>>>
>>> def test_read_inexistent_item():
...     response = client.get("/items/baz", headers={"X-Token": "coneofsilence"})
...     assert response.status_code == 404
...     assert response.json() == {"detail": "Item not found"}
>>>
>>>
>>> def test_create_item():
...     response = client.post(
...         "/items/",
...         headers={"X-Token": "coneofsilence"},
...         json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
...     )
...     assert response.status_code == 200
...     assert response.json() == {
...         "id": "foobar",
...         "title": "Foo Bar",
...         "description": "The Foo Barters",
...     }
>>>
>>>
>>> def test_create_item_bad_token():
...     response = client.post(
...         "/items/",
...         headers={"X-Token": "hailhydra"},
...         json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
...     )
...     assert response.status_code == 400
...     assert response.json() == {"detail": "Invalid X-Token header"}
>>>
>>>
>>> def test_create_existing_item():
...     response = client.post(
...         "/items/",
...         headers={"X-Token": "coneofsilence"},
...         json={
...             "id": "foo",
...             "title": "The Foo ID Stealers",
...             "description": "There goes my stealer",
...         },
...     )
...     assert response.status_code == 400
...     assert response.json() == {"detail": "Item already exists"}


Async
-----
* https://fastapi.tiangolo.com/advanced/async-tests/

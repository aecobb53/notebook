# FastAPI

https://fastapi.tiangolo.com/features/

Compatable modules:
- Enum
- typing(Optional)
- pydantic

The format above is `module(class)` -> `from module import class`

---

Operations
- POST
- GET
- PUT
- DELETE

more exotic ones
- OPTIONS
- HEAD
- PATCH
- TRACE

Core operations
`POST`: to create data
`GET`: to read data
`PUT`: to update data
`DELETE`: to delete data

You can return a dict, list, singular values as str, int, etc. 
You can also return Pydantic models.

Pydantic is used for data validation. 
It comes with fastapi. 

Order of path operations matters. 
Hard links need to come first

```python
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
```

Im not sure what `Enum` the module is used for but it works with fastapi

## Query parameters

When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

```python
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
```
The query is the set of key-value pairs that go after the ? in a URL, separated by & characters.

For example, in the URL:

```url
http://127.0.0.1:8000/items/?skip=0&limit=10
```

...the query parameters are:

- `skip`: with a value of `0`
- `limit`: with a value of `10`

As they are part of the URL, they are "naturally" strings.

But when you declare them with Python types (in the example above, as int), they are converted to that type and validated against it.

In the example above they have default values of `skip=0` and `limit=10`.

You can also use the `Optional` module
Using Optional you can interprit these as True: [`true`, `True`, `1`, `on`, `yes`] or any other case combos. 

If you want to make a parameter optional set the Optional type to `None`. 

You can set key-value pairs like this
```python
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
```

```url
http://127.0.0.1:8000/items/foo-item?needy=sooooneedy
```

All together

```python
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
```

In this case, there are 3 query parameters:

- `needy`, a required `str`.
- `skip`, an `int` with a default value of `0`.
- `limit`, an optional `int`.

---

You can set min and max lengh using Optional. 
You can then also use regex

```python
@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

You can set default values much like `None`:
```python
@app.get("/items/")
async def read_items(q: str = Query("fixedquery", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```
Here the `fixedquery` is a default `q` value. 

You can mix and match requirements 
```python
q: str
# will require str much like
q: Optional[str] = None

# if you need Query
q: Optional[str] = Query(None, min_length=3)
```

If you have multiple `q`'s
```python
@app.get("/items/")
async def read_items(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items
```

```url
http://localhost:8000/items/?q=foo&q=bar
```

they will be interperatid like this
```json
{
  "q": [
    "foo",
    "bar"
  ]
}
```

You can set a list of default `q`'s
```python
@app.get("/items/")
async def read_items(q: List[str] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items
```

you can use `list` directly instead of `List[str]`
```python
async def read_items(q: list = Query([])):
```

You can add titles and descriptions
```python
@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

You can declare aliases if the url has to be one type but the variable is something else in python. 
```python
async def read_items(q: Optional[str] = Query(None, alias="item-query")):
```

You can depreciate old parameters with `deprecated=True`
```python
async def read_items(
    q: Optional[str] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
```

### Path Parameters and Numeric Validations

To use kwargs have the first element as a `*`
```python
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get"), q: str
):
```

Here, with `ge=1`, item_id will need to be an integer number "greater than or equal" to `1`.
```python
# int
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get", ge=1), q: str
):

# float
async def read_items(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(..., gt=0, lt=10.5)
):
```

|Abreviation|Action|
|---:|:---|
|`e` |Equal to              |
|`gt`|Greater than          |
|`lt`|Less than             |
|`ge`|Greater than or equal |
|`le`|Less than or equal    |

## Body

Body may be a very important thing in the long run but it wasnt making a lot of sence because I 
still have no concept of what the requests should look like. 


# Recaps


- Import FastAPI.
- Create an app instance.
- Write a path operation decorator (like @app.get("/")).
- Write a path operation function (like def root(): ... above).
- Run the development server (like uvicorn main:app --reload).

---

With FastAPI, by using short, intuitive and standard Python type declarations, you get:

- Editor support: error checks, autocompletion, etc.
- Data "parsing"
- Data validation
- API annotation and automatic documentation

And you only have to declare them once.

That's probably the main visible advantage of FastAPI compared to alternative frameworks 

---

You can declare additional validations and metadata for your parameters.

Generic validations and metadata:

- alias
- title
- description
- deprecated

Validations specific for strings:

- min_length
- max_length
- regex

---

With Query, Path (and others you haven't seen yet) you can declare metadata and string validations in the same ways as with Query Parameters and String Validations.

And you can also declare numeric validations:

- gt: greater than
- ge: greater than or equal
- lt: less than
- le: less than or equal

---

You can add multiple body parameters to your path operation function, even though a request can only have a single body.

But FastAPI will handle it, give you the correct data in your function, and validate and document the correct schema in the path operation.

You can also declare singular values to be received as part of the body.

And you can instruct FastAPI to embed the body in a key even when there is only a single parameter declared.

---

You can use Pydantic's Field to declare extra validations and metadata for model attributes.

You can also use the extra keyword arguments to pass additional JSON Schema metadata.

---

With FastAPI you have the maximum flexibility provided by Pydantic models, while keeping your code simple, short and elegant.

But with all the benefits:

- Editor support (completion everywhere!)
- Data conversion (a.k.a. parsing / serialization)
- Data validation
- Schema documentation
- Automatic docs

---



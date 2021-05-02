import os
import uvicorn
from fastapi import FastAPI, Path, File, Query, Cookie, Header, Request, Response
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from typing import Optional
from datetime import datetime

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

app = FastAPI()
app.mount("/static", StaticFiles(directory="./dist/", html=True))

@app.get("/")
async def root(request: Request):
    return FileResponse("./dist/index.html", media_type='text/html')

@app.get("/header/")
async def read_items(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}

@app.get("/cookie/")
async def read_items(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}

@app.get("/response/")
async def read_items():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/items/{item_id}")
async def read_items(
        item_id: int = Path(..., title="The ID of the item to get"),
        q: Optional[str] = Query(None, alias="item-query"),
    ):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/date/")
async def get_date():
    now = datetime.now()    
    return {"date" : date}

@app.get("/lover/")
async def get_lover():
    now = datetime.now()
    my_lover = "mangokim"
    return {"my_lover" : my_lover, "now" : now}

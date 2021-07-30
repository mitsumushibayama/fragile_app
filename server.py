from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import db

app = FastAPI()

@app.get("/")
def read_root():
    return FileResponse('reference.html')

@app.get("/scripts")
def read_js():
    return FileResponse('reference.js')

@app.get("/get/user")
async def get_all():
    json_data = jsonable_encoder(db.get_all())
    return JSONResponse(content = json_data)

@app.get("/get/user/{id}")
async def get_user(id: int):
    json_data = jsonable_encoder(db.get_id_user(id))
    return JSONResponse(content = json_data)

@app.get("/get/user/{id}/pass")
async def get_user(id: int):
    json_data = jsonable_encoder(db.get_id_user_pass(id))
    return JSONResponse(content = json_data)



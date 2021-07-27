from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
import db

file_path = 'reference.html'
app = FastAPI()

@app.get("/", response_class = HTMLResponse)
def read_root():
    return FileResponse(file_path, media_type='text/html')

@app.get("/get/users")
async def get_all():
    json_data = jsonable_encoder(db.get_all())
    return JSONResponse(content = json_data)

@app.get("/get/users/{id}")
async def get_user(id: int):
    json_data = jsonable_encoder(db.get_id_user(id))
    return JSONResponse(content = json_data)


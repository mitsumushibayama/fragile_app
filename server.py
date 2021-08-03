from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import db
import user

app = FastAPI()
app.mount("/scripts/reference", StaticFiles(directory="scripts"), name="scripts")
app.mount("/scripts/register", StaticFiles(directory="scripts"), name="scripts")

@app.get("/")
def get_index():
    return FileResponse('index.html')

@app.get("/reference")
def get_reference():
    return FileResponse('reference.html')

@app.get("/register")
def get_register():
    return FileResponse('register.html')

@app.get("/scripts/reference")
def get_reference_js():
    return FileResponse('scripts/reference.js')

@app.get("/scripts/register")
def get_register_js():
    return FileResponse('scripts/register.js')

@app.get("/get/user/{id}")
async def get_user(id: int):
    json_data = jsonable_encoder(db.get_id_user(id))
    return JSONResponse(content = json_data)

@app.get("/get/user/{id}/pass")
async def get_user(id: int):
    json_data = jsonable_encoder(db.get_id_user_pass(id))
    return JSONResponse(content = json_data)

@app.post("/post/user")
async def post_user(user: user.User):
    json_data = jsonable_encoder(db.post_user(user))
    return JSONResponse(content = json_data)




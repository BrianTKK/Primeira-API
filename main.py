from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class usuario(BaseModel):
    id: int
    name: str

usuarios = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/usuarios")
def listar_usuarios():
    return usuarios

@app.post("/usuarios", status_code=201)
def add_usuario(usuario: usuario):
    next_id = (0 if len(usuarios) == 0 else max([usuario.id for usuario in usuarios])) + 1

    usuario.id = next_id
    usuarios.append(usuario)

    return usuario

@app.delete("/usuarios/{id_usuario}", status_code=204)
def delete_usuario(id_usuario: int):
    global usuarios
    
    usuarios_encontrados = [usuario for usuario in usuarios if usuario.id == id_usuario]

    if len(usuarios_encontrados) == 0:
        raise HTTPException(status_code=404, detail="usuario nao encontrado")
    
    usuarios =  [usuario for usuario in usuarios if usuario.id != id_usuario]
    return 
from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    nome_usuario : str
    senha : str
    admin : bool
    

class LoginSchema(BaseModel):
    nome_usuario : str
    senha : str
    
    class Config:
        from_attributes = True 
from fastapi import APIRouter, Depends, HTTPException
from backend.models import Usuario
from backend.dependecies import pegar_sessao, verificar_token
from sqlalchemy.orm import Session
from backend.config import bcrypt_context, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY
from backend.autenticacao.schemas import UsuarioSchema, LoginSchema
from jose import jwt, JWTError
from datetime import datetime, timezone, timedelta
from fastapi.security import OAuth2PasswordRequestForm

auth_router = APIRouter(prefix="/auth", tags=["auth"])

def criar_token(id_usuario,duracao_token =timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) ):
    data_expiracao = datetime.now(timezone.utc) + duracao_token
    dict_info = {"sub": str(id_usuario), "exp":data_expiracao}
    encoded_jwt = jwt.encode(dict_info, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def autenticar_usuario(nome_usuario, senha, session):
    usuario = session.query(Usuario).filter(Usuario.nome_usuario == nome_usuario).first()
    
    if not usuario:
        return False
    
    elif not bcrypt_context.verify(senha, usuario.senha):
        return False
    
    else:
        return usuario
    
@auth_router.post("/cadastro")
async def cadastro_usuario(usuario_schema: UsuarioSchema, session:Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    #buscando usuario:
    usuario = session.query(Usuario).filter(Usuario.nome_usuario==usuario_schema.nome_usuario).first()
    
    if usuario:
        raise HTTPException(status_code=400, detail="Usuario já cadastrado!")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome_usuario, senha_criptografada)
        session.add(novo_usuario)
        session.commit()    
        return {"mensagem":"Usuario cadastrado com sucesso"}
    
@auth_router.post("/login")
async def login(login_schema:LoginSchema, session:Session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(login_schema.nome_usuario, login_schema.senha, session)
    
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuario não encontrado!")
    else:
        access_token = criar_token(usuario.id)
        refresh_token = criar_token(usuario.id, timedelta(days=7))
        return{"acess_token":access_token,
               "refresh_token":refresh_token,
               "type_token":"Bearer"}

#rota criada apenas para teste de autenticação com fastAPI        
@auth_router.post("/login-form")
async def login_form(form_data: OAuth2PasswordRequestForm = Depends(),
                     session: Session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(form_data.username, form_data.password, session)
    
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuario não encontrado!")
    else:
        access_token = criar_token(usuario.id)
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

        
        
@auth_router.get("/refresh")
async def use_refresh_token(usuario: Usuario = Depends(verificar_token)):
    access_token = criar_token(usuario.id)
    return{"acess_token":access_token,
               "type_token":"Bearer"}
        
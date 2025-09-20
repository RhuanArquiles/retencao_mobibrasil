from fastapi import Depends, HTTPException
from backend.models import db
from sqlalchemy.orm import sessionmaker, Session
from backend.models import Usuario
from jose import jwt, JWTError
from backend.config import SECRET_KEY, ALGORITHM, oauth2_schemas

def pegar_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()
        
def verificar_token(token:str = Depends(oauth2_schemas), session:Session=Depends(pegar_sessao)):
    try:
        dic_info = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id_usuario = int(dic_info.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Acesso negado, verifique a validade do token")
    
    usuario = session.query(Usuario).filter(Usuario.id==id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Acesso inválido")
    else:
        return usuario
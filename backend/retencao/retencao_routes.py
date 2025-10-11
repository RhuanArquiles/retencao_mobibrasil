from fastapi import APIRouter, Depends, HTTPException
from backend.retencao.schemas import RetencaoSchema, RetencaoResponseSchema, RetencaoUpdateSchema
from backend.models import Retencao
from backend.dependecies import pegar_sessao, verificar_token
from sqlalchemy.orm import Session
from datetime import datetime, date
from typing import List

retencao_router = APIRouter(prefix="/retencao", tags= ["retencao"], dependencies=[Depends(verificar_token)])

@retencao_router.post("/cadastro")
async def cadastro_retido(retencao_schema: RetencaoSchema, session:Session = Depends(pegar_sessao)):
    dias_retido = (retencao_schema.data_retencao - retencao_schema.data_inicial).days
    
    novo_retido = Retencao(
    descricao=retencao_schema.descricao,
    data_inicial=retencao_schema.data_inicial,
    data_retencao=retencao_schema.data_retencao,
    dias_retido=dias_retido, 
    garagem=retencao_schema.garagem,
    prefixo=retencao_schema.prefixo
)


    session.add(novo_retido)
    session.commit()
    return {"mensagem": "informação cadastrada com sucesso!"}

@retencao_router.get("/retido", response_model=List[RetencaoResponseSchema])
async def acessar_retido(data:date, session : Session = Depends(pegar_sessao)):
    retencao = session.query(Retencao).filter(Retencao.data_retencao==data).all()
    
    if retencao:
        return retencao
    else:
        raise HTTPException(status_code=400, detail="Não há informações de retenção na data informada")
    
@retencao_router.put("/retido/{retencao_id}")
async def atualizar_retido(retencao_id:int, retencao_update_schema:RetencaoUpdateSchema, session:Session = Depends(pegar_sessao)):
    retencao_update = session.query(Retencao).filter(Retencao.id == retencao_id).first()
    
    if not retencao_update:
        raise HTTPException(status_code=400, detail="Retenção não encontrada.")
    else:
        dias_retido = (retencao_update_schema.data_retencao - retencao_update_schema.data_inicial).days
        
        retencao_update.descricao = retencao_update_schema.descricao
        retencao_update.data_inicial = retencao_update_schema.data_inicial
        retencao_update.data_retencao = retencao_update_schema.data_retencao
        retencao_update.dias_retido = dias_retido
        retencao_update.garagem = retencao_update_schema.garagem
        retencao_update.prefixo = retencao_update_schema.prefixo
        
        session.commit()
        session.refresh(retencao_update)
        
        return{"mensagem": "retenção atualizada com sucesso"}
    
@retencao_router.delete("/retido/{retencao_id}")
async def deletar_retido(retencao_id : int, session:Session = Depends(pegar_sessao)):
    retencao_delete = session.query(Retencao).filter(Retencao.id == retencao_id).first()
    if not retencao_delete:
        raise HTTPException(status_code=400, detail="Retencao não encontrada")   
    else:
        session.delete(retencao_delete)
        session.commit()
        
        return {"mensagem":"retenção deletada com sucesso"}
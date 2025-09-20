from fastapi import APIRouter, Depends, HTTPException
from backend.dependecies import pegar_sessao
from sqlalchemy.orm import Session
from backend.models import Veiculo
from backend.veiculo.schemas import VeiculoSchema

veiculo_router = APIRouter(prefix="/veiculo", tags=["veiculo"])

@veiculo_router.post("/veiculo")
async def cadastro_veiculo(veiculo_schema:VeiculoSchema, session:Session = Depends(pegar_sessao)):
    veiculo = session.query(Veiculo).filter(Veiculo.prefixo == veiculo_schema.prefixo).first()
    
    if veiculo:
        raise HTTPException(status_code=400, detail = "Veículo já cadastrado")
        
    else:
        veiculo = Veiculo(
            prefixo=veiculo_schema.prefixo,
            tipo=veiculo_schema.tipo,
            modelo=veiculo_schema.modelo
        )
        
        session.add(veiculo)
        session.commit()
        
        return {"mensagem":"Veiculo cadastrado com sucesso"}
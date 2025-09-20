from pydantic import BaseModel
from datetime import date

class RetencaoSchema(BaseModel):
    descricao : str
    data_inicial : date
    data_retencao : date
    garagem : str
    prefixo : int
    
    class Config:
        from_attributes = True
        
class RetencaoResponseSchema(BaseModel):
    id: int
    descricao: str
    data_inicial: date
    data_retencao: date
    dias_retido: int
    garagem: str
    prefixo: int

    class Config:
        from_attributes = True
        
class RetencaoUpdateSchema(BaseModel):
    descricao : str
    data_inicial : date
    data_retencao : date
    garagem : str
    prefixo : int
    
    class Config:
        from_attributes = True
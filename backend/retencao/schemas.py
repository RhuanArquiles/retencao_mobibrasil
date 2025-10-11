from pydantic import BaseModel, field_validator
from datetime import date, datetime

class RetencaoSchema(BaseModel):
    descricao : str
    data_inicial : date
    data_retencao : date
    garagem : str
    prefixo : int
    
    #converte a entrada do usuário para um objeto do tipo date
    @field_validator("data_inicial", "data_retencao", mode="before")
    def parse_date(cls, v):
        if isinstance(v, str):
            for fmt in ("%d/%m/%Y", "%d-%m-%Y"):
                try:
                    return datetime.strptime(v, fmt).date()
                except ValueError:
                    continue
            raise ValueError("Data deve estar no formato DD/MM/YYYY ou DD-MM-YYYY")
        return v
    
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
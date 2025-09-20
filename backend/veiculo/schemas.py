from pydantic import BaseModel

class VeiculoSchema(BaseModel):
    prefixo : int
    tipo : str
    modelo : str
    
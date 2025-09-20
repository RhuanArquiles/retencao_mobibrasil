from fastapi import FastAPI

app = FastAPI()

from backend.retencao.retencao_routes import retencao_router
from backend.autenticacao.auth_routes import auth_router
from backend.veiculo.veiculo_routes import veiculo_router

app.include_router(retencao_router)
app.include_router(auth_router)
app.include_router(veiculo_router)

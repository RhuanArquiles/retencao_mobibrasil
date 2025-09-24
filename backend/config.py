from passlib.context import CryptContext #rotas de autenticação
from dotenv import load_dotenv
import os
from fastapi.security import OAuth2PasswordBearer

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM =os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


bcrypt_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")
oauth2_schemas = OAuth2PasswordBearer("/auth/login")

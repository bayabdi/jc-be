from distutils.command.config import config
from starlette.config import Config

config = Config(".env")
DATABASE_URL = "postgresql://postges:string@localhost:5432/jc"
ACCES_TOKEN_EXPIRE_MINUTES = 24 * 60
ALGORITHM = "HS256"
SECRET_KEY = config("SECRET_KEY", cast=str, default="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7")
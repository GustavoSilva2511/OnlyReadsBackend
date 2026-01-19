from dotenv import load_dotenv
from os import getenv

load_dotenv()

class Settings:
    DATABASE_URL = getenv("DATABASE_URL")
    # DATABASE_URL = "sqlite:///database.db"
    DATABASE_MEMORY_URL = getenv("DATABASE_MEMORY_URL")
    SECRET_KEY = getenv("SECRET_KEY")
    ALGORITHM = getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

settings = Settings()

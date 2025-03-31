import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
import secrets
# def generate_secret_key():
#     return secrets.token.hex(32)
# env_path = Path(__file__).parent.parent / ".env"
# if not env_path.exists():
#     with open(env_path, "a") as f:
#         f.write(f'\nSECRET_KEY={generate_secret_key}')


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: int
    SECRET_KEY: str
    ALGORITHM: str
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", '.env')
    )

settings = Settings()

def get_db_url():
    return (f'postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@'
            f'{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}')
from functools import lru_cache
from pydantic import BaseSettings, SecretStr


class Setting(BaseSettings):
    DB_USERNAME: str
    DB_PASSWORD: SecretStr
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    TELEGRAM_BOT_TOKEN: SecretStr

    class Config:
        env_file = ".env"
        env_file_encding = "uft-8"


@lru_cache
def get_setting():
    return Setting()


settings = get_setting()

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str
    description: str
    app_version: str
    database_url: str
    secret: str
    first_superuser_email: str
    first_superuser_password: str

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


settings = Settings()

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """
    統一管理應用程式環境設定。
    """

    debug: bool = False
    database_url: str

    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_")

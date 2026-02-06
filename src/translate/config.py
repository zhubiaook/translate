from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # env OPENAI_API_KEY
    openai_api_key: str
    # env OPENAI_BASE_URL
    openai_base_url: str = "https://api.deepseek.com"
    # env OPENAI_MODEL
    openai_model: str = "deepseek/deepseek-chat"


settings = Settings()

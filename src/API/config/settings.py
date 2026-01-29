import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    
    # API
    APP_NAME: str = os.getenv("APP_NAME")
    APP_VERSION: str = os.getenv("APP_VERSION")
    
    # Server
    HOST: str = os.getenv("HOST")
    PORT: int = int(os.getenv("PORT"))
    
    # Whisper
    SST_MODEL_PATH: str = os.getenv("SST_MODEL_PATH")
    
    # Audio
    AUDIO_SAMPLE_RATE: int = int(os.getenv("AUDIO_SAMPLE_RATE"))
    AUDIO_MONO: bool = os.getenv("AUDIO_MONO").lower() == "true"
    AUDIO_FP16: bool = os.getenv("AUDIO_FP16").lower() == "true"
    AUDIO_LANGUAGE: str = os.getenv("AUDIO_LANGUAGE")
    FILES_EXTENSIONS: list[str] = os.getenv("FILES_EXTENSIONS").split(",")
    
    # LLM
    LLM_MODEL_PATH: str = os.getenv("LLM_MODEL_PATH", "")


settings = Settings()

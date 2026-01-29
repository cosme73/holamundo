import whisper
from src.API.config.settings import settings

class STTModel:
    _instance = None
    _model = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._inicializar_modelo()
        return cls._instance
    
    def _inicializar_modelo(self):
        if self._model is None:
            self._model = whisper.load_model(settings.SST_MODEL_PATH)
    
    def get_model(self):
        return self._model

# Instancia singleton
stt_model = STTModel()

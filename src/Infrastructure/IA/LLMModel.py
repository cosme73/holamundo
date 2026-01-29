from llama_cpp import Llama
from src.API.config.settings import settings

class LLMModel:
    _instance = None
    _model = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._inicializar_modelo()
        return cls._instance
    
    def _inicializar_modelo(self):
        if self._model is None:
            self._model = Llama(model_path=settings.LLM_MODEL_PATH)
    
    def get_model(self):
        return self._model

# Instancia singleton
llm_model = LLMModel()

import time
from src.API.config.settings import settings
from src.Infrastructure.IA.LLMModel import llm_model



class PromptProcessingService:
    
    def __init__(self):
        self.model = llm_model.get_model()
    
    def _formatear_tiempo(self, segundos: float) -> str:
  
        return f"{int(segundos // 60):02d}:{int(segundos % 60):02d}"
    
    def PromptProcessing(self, prompt) -> tuple[str, str]:
        
        inicio = time.time()
        
        messages = [
        {"role": "system", "content": "Eres un asistente que extrae información y genera JSON válido."},
        {"role": "user", "content": prompt}
    ]
        respuesta = self.create_chat_completion(
	    messages = messages)

        duracion = time.time() - inicio
        tiempo = self._formatear_tiempo(duracion)
        
        return respuesta['choices'][0]['message']['content'], tiempo
    


prompt_processing_service = PromptProcessingService()

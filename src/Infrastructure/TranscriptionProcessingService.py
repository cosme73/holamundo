
import os
import time
import tempfile
import librosa
import numpy as np
from src.API.config.settings import settings
from src.Infrastructure.IA.STTModel import stt_model

class TranscripcionProcessingService:
    
    def __init__(self):
        self.model = stt_model.get_model()
    
    def _formatear_tiempo(self, segundos: float) -> str:
  
        return f"{int(segundos // 60):02d}:{int(segundos % 60):02d}"
    
    def transcribir(self, audio_bytes: bytes) -> tuple[str, str]:
        
        inicio = time.time()
        
        audio_procesado = self.procesar_audio(audio_bytes)
        result = self.model.transcribe(
            audio_procesado, 
            language=settings.AUDIO_LANGUAGE, 
            fp16=settings.AUDIO_FP16
        )
        
        duracion = time.time() - inicio
        tiempo = self._formatear_tiempo(duracion)
        
        return result["text"].strip(), tiempo
    
    def procesar_audio(self, audio_bytes: bytes) -> np.ndarray:
        khz = int(settings.AUDIO_SAMPLE_RATE)
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_bytes)
            tmp_path = tmp.name
        
        try:
            audio, _ = librosa.load(tmp_path, sr=khz, mono=settings.AUDIO_MONO)
            return audio.astype(np.float32)
        finally:
            os.unlink(tmp_path)


transcription_processing_service = TranscripcionProcessingService()

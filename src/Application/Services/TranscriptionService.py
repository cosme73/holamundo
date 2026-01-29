
import time
from src.Infrastructure.TranscriptionProcessingService import transcription_processing_service
from src.Infrastructure.TextToJsonService import tex_to_json_service

from src.Application.Models.DTOs.TranscriptionDto import TranscriptionResponse, ProcessingResponse
from src.API.config.settings import settings
from src.Domain.prompts import LLM_JSON_PROMPT
from src.Infrastructure.PromptProcessingService import prompt_processing_service

class TranscriptionService:
    MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB

    @staticmethod
    async def transcribe(audio_bytes: bytes) -> TranscriptionResponse:
        if not audio_bytes:
            raise ValueError("El archivo está vacío o corrupto")

        if len(audio_bytes) > TranscriptionService.MAX_FILE_SIZE:
            raise ValueError("El archivo excede el tamaño máximo permitido (50 MB)")

        texto, tiempo = transcription_processing_service.transcribir(audio_bytes)

        return TranscriptionResponse(
            transcription=texto,
            processing_time=tiempo
        )
    
    @staticmethod
    async def AudioProcessing(audio_bytes: bytes) -> ProcessingResponse:
        inicio_total = time.time()
        
        if not audio_bytes:
            raise ValueError("El archivo está vacío o corrupto")

        if len(audio_bytes) > TranscriptionService.MAX_FILE_SIZE:
            raise ValueError("El archivo excede el tamaño máximo permitido (50 MB)")

        audio_texto, tiempo = transcription_processing_service.transcribir(audio_bytes)
        prompt = LLM_JSON_PROMPT.replace("{transcription}", audio_texto)
        llm_response, llm_time = prompt_processing_service.PromptProcessing(prompt)
        json_data = tex_to_json_service.TextToJsnProcessing(llm_response)

        duracion_total = time.time() - inicio_total
        tiempo_total = f"{int(duracion_total // 60):02d}:{int(duracion_total % 60):02d}"

        return ProcessingResponse(
            transcription=TranscriptionResponse(
                transcription=audio_texto,
                processing_time=tiempo
            ),
            processing_complete_time=tiempo_total,
            data=json_data,
            data_processing_time=llm_time
        )


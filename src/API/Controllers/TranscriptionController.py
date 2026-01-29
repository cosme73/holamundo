
from fastapi import APIRouter, UploadFile, File, HTTPException
from src.Application.Models.DTOs.TranscriptionDto import TranscriptionResponse, ProcessingResponse
from src.Application.Services.TranscriptionService import TranscriptionService
from src.API.config.settings import settings
router = APIRouter(prefix="/api", tags=["Transcription"])


@router.post("/transcription", response_model=TranscriptionResponse)
async def transcribe_audio(file: UploadFile = File(...)):
    
  # Obtener la extensión del archivo
    file_extension = file.filename.split(".")[-1].lower()
    
    # Validar la extensión
    if f".{file_extension}" not in settings.FILES_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"Solo se permiten: {', '.join(settings.FILES_EXTENSIONS)}")
    
    try:
        audio_bytes = await file.read()
        response = await TranscriptionService.transcribe(audio_bytes)
        return response
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/audio-processing", response_model=ProcessingResponse)
async def audio_processing(file: UploadFile = File(...)):
    
  # Obtener la extensión del archivo
    file_extension = file.filename.split(".")[-1].lower()
    
    # Validar la extensión
    if f".{file_extension}" not in settings.FILES_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"Solo se permiten: {', '.join(settings.FILES_EXTENSIONS)}")
    
    try:
        audio_bytes = await file.read()
        response = await TranscriptionService.AudioProcessing(audio_bytes)
        return response
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
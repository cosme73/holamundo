"""
SIPA API - Main
"""
from fastapi import FastAPI

from src.API.config.settings import settings
from src.API.Controllers.TranscriptionController import router
from src.Infrastructure.IA.STTModel import stt_model
from src.Infrastructure.IA.LLMModel import llm_model



app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(router)


@app.get("/health")
def health():
    return {
        "status": "OK",
        "audio_model_loaded": stt_model.get_model() is not None,
        "llm_model_loaded": llm_model.get_model() is not None
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.API.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )

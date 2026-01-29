
from pydantic import BaseModel


class TranscriptionResponse(BaseModel):
    transcription: str
    processing_time: str


class ExtractedJsonResponse(BaseModel):
    transcription: str
    processing_time: str
    extracted_json: dict


class JsonData(BaseModel):
    fecha: str = ""
    couta_inicial_soles: str = ""
    deuda_capital_soles: str = ""
    plazo_meses: str = ""
    numero_cuotas: str = ""
    couta_aproximada_soles: str = ""
    primer_vencimiento: str = ""
    nombre_apellido: str = ""
    dni: str = ""
    correo_electronico: str = ""
    fecha_nacimiento: str = ""
    condiciones_producto_original: bool = False
    TEA_: str = ""
    Seguro_desgravamen: bool = False
    aceptacion_cliente: bool = False

class ProcessingResponse(BaseModel):
    transcription: TranscriptionResponse
    processing_complete_time: str
    data: str
    data_processing_time: str
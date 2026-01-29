# SIPA.Application.prompts.py
LLM_JSON_PROMPT = """
Extrae los datos de la transcripción y responde SOLO con el JSON completo.
NO razones, NO expliques.

Transcripción: {transcription}

JSON:
{{
  "fecha": "",
  "couta_inicial_soles": "",
  "deuda_capital_soles": "",
  "plazo_meses": "",
  "numero_cuotas": "",
  "couta_aproximada_soles": "",
  "primer_vencimiento": "",
  "nombre_apellido": "",
  "dni": "",
  "correo_electronico": "",
  "fecha_nacimiento": "",
  "condiciones_producto_original": false,
  "TEA%": "",
  "Seguro_desgravamen": false,
  "aceptacion_cliente": false
}}
"""

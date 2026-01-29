
import json
import re
class TextToJsonService:


    def TextToJsnProcessing( text: str):

        json_match = re.search(r"\{(?:[^{}]|(?R))*\}", text, re.DOTALL)
        if not json_match:
            raise ValueError("No se encontró un JSON en el texto proporcionado.")

        json_str = json_match.group(0)

        return json.loads(json_str)
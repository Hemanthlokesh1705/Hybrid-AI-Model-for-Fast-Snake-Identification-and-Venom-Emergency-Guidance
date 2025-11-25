import json
import re
from datetime import datetime
from google import genai

class SnakeInfoService:
    SYSTEM_PROMPT = """
    You are a factual assistant. Given a snake species name, output STRICT JSON (no text outside JSON) with:
    - input_label
    - canonical_name
    - scientific_name
    - habitat
    - venomous ("yes"/"no"/"unknown")
    - venom_type ("neurotoxic"/"hemotoxic"/"cytotoxic"/"mixed"/null)
    - first_aid (list of 3-6 short, safe steps)
    - emergency_priority ("immediate hospital", "urgent hospital", "monitor & consult", "low")
    - safety_info (3-5 short preventive tips)
    - confidence_note
    - verify_sources (short list of authoritative references)
    - timestamp (ISO 8601)

    If unsure about medical data, set fields to null and include note requesting expert verification.
    Return only valid JSON.
    """

    def __init__(self, model: str = "gemini-2.5-flash"):
        self.client = genai.Client()
        self.model = model

    def _call_gemini(self, predicted_name: str) -> dict:
        """Call Gemini to get structured snake info."""
        prompt = self.SYSTEM_PROMPT + f'\nPredicted name: "{predicted_name}"\nRespond with JSON only.'
        response = self.client.models.generate_content(model=self.model, contents=prompt)
        text = response.text.strip()

        # Parse JSON safely
        try:
            return json.loads(text)
        except Exception:
            m = re.search(r'(\{.*\})', text, flags=re.DOTALL)
            if m:
                try:
                    return json.loads(m.group(1))
                except Exception:
                    return {"error": "Failed to parse Gemini JSON", "raw_output": text}
            return {"error": "No valid JSON found", "raw_output": text}

    def get_snake_info(self, predicted_name: str) -> dict:
        """Returns structured snake information (JSON) for a given predicted snake name."""
        if not predicted_name or not isinstance(predicted_name, str):
            return {"error": "Invalid input — predicted_name must be a non-empty string."}

        info = self._call_gemini(predicted_name)
        # Ensure timestamp exists
        if "timestamp" not in info:
            info["timestamp"] = datetime.now().isoformat()
        return info


# Example usage
# if __name__ == "__main__":
#     service = SnakeInfoService()
#     snake_name = "king cobra"
#     info = service.get_snake_info(snake_name)
#     print(json.dumps(info, indent=2))

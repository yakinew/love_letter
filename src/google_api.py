import google.generativeai as genai
from pydantic import Field
from pydantic_settings import BaseSettings


class GeminiSettings(BaseSettings):
    api_key: str = Field(alias='GEMINI_API_KEY')
    model: str = Field(default='gemini-1.5-flash', alias='GEMINI_MODEL')


def get_love_letter() -> str:
    settings = GeminiSettings()

    genai.configure(api_key=settings.api_key)
    model = genai.GenerativeModel(settings.model)

    prompt = f"שמי הוא יעקב, אבל הכינוי שלי הוא יקי. אנא כתוב מכתב אהבה מרגש לאשתי, הדס. תביע את אהבתי העמוקה..."

    response = model.generate_content(prompt)
    love_letter = response.text
    return love_letter

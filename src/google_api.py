"""
This module provides an interface for interacting with the Google API.
It includes classes and functions for authentication, and making requests.
"""

import google.generativeai as genai
from pydantic import Field
from pydantic_settings import BaseSettings


class GeminiSettings(BaseSettings):
    """
    Settings for the Gemini model.

    Attributes:
        api_key (str): The API key for using the Gemini API.  Loaded from the environment
            variable 'GEMINI_API_KEY'.
        model (str): The name of the Gemini model to use. Defaults to 'gemini-1.5-flash'.
            Loaded from the environment variable 'GEMINI_MODEL'.
    """
    api_key: str = Field(alias='GEMINI_API_KEY')
    model: str = Field(default='gemini-1.5-flash', alias='GEMINI_MODEL')


def get_love_letter() -> str:
    """
    Generates a touching love letter to a wife, Hadas, using a Gemini language model.

    The function retrieves settings from the environment, configures the Gemini API,
    and uses the model to create a love letter with a specific tone.

    Returns:
        str: The generated love letter.
    """
    settings = GeminiSettings()

    genai.configure(api_key=settings.api_key)
    model = genai.GenerativeModel(settings.model)

    prompt = ('שמי הוא יעקב, אבל הכינוי שלי הוא יקי. אנא כתוב מכתב '
              'אהבה מרגש לאשתי, הדס. תביע את אהבתי העמוקה...')

    response = model.generate_content(prompt)
    love_letter = response.text
    return love_letter

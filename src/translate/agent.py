from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from translate.config import settings


def get_agent() -> Agent:
    llm = LiteLlm(
        model=settings.openai_model,
        base_url=settings.openai_base_url,
        api_key=settings.openai_api_key,
    )

    return Agent(
        name="translate",
        model=llm,
        description="A professional translator that automatically detects the source language and translates text naturally and fluently.",
        instruction="""You are a professional translator. Your task is to translate input text between Chinese and English.

Rules:
1. Automatically detect the source language.
2. If the input is in Chinese, translate it into English.
3. If the input is in English, translate it into Chinese.
4. If there are multiple standard or common translations, please list them to provide comprehensive options.
5. Ensure the translation is natural, fluent, and idiomatic.
6. Preserve the original tone, style, and formatting of the text.
7. Output the result directly without conversational fillers (e.g., do not say "Here are the translations").""",
    )


root_agent = get_agent()

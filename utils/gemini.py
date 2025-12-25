from google import genai
import re
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_TOKEN=os.environ.get("GEMINI_TOKEN")

client = genai.Client(api_key=GEMINI_TOKEN)


def clean_markdown(text):
    # Убираем жирный и курсив (звездочки и подчеркивания)
    text = re.sub(r'[*_]{1,3}', '', text)
    # Убираем заголовки (решетки в начале строки)
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
    # Убираем символы цитат и кода
    text = re.sub(r'[>`]', '', text)
    return text


def gen_ai(prompt, config):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=config,
    )

    return clean_markdown(response.text)
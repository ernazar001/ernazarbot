from openai import OpenAI
from config import API_KEY

client = OpenAI(
    api_key=API_KEY
)


def chatgpt_answer(text: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content


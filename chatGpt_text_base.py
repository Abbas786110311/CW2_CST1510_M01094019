import os
from app.env_loader import load_env

load_env()

try:
    from openai import OpenAI
except Exception:
    raise RuntimeError("openai package is not installed in the environment")

api_key = os.getenv("OPEN_AI_KEY")
if not api_key:
    raise RuntimeError("OPEN_AI_KEY not found in environment (.env)")

client = OpenAI(api_key=api_key.strip())

prompt = "What is the best AI related job available right now?"

try:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    print(completion.choices[0].message.content)
except Exception as e:
    print("OpenAI request failed:", e)

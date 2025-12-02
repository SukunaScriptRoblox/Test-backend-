from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

AI_API_KEY = "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"  # Replace
AI_URL = "https://openrouter.ai/api/v1/chat/completions"

class Mystery(BaseModel):
    text: str

@app.post("/solve")
def solve(mystery: Mystery):
    prompt = f"Solve this mystery, riddle or encrypted message:\n\n{mystery.text}\n\nExplain clearly."

    headers = {
        "Authorization": f"Bearer {AI_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a mystery solving detective AI."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(AI_URL, json=body, headers=headers)
    result = response.json()

    answer = result["choices"][0]["message"]["content"]

    return {"answer": answer}

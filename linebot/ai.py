import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=3000
    )

    reply_text = ""
    for choice in response.choices:
        reply_text += choice.text

    with open("line.json", "w", encoding="utf-8") as fp:
        json.dump(reply_text, fp, ensure_ascii=False, indent=4)

    return reply_text.replace('\n', '')
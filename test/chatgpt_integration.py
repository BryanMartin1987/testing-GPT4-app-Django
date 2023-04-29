import openai
import json

with open('openai_key.json') as f:
    openai.api_key = json.load(f)['key']

def get_how_to(query):
    prompt = f"Provide up to five concise steps with rationales for the following how-to query:\n\n{query}\n\nSteps:"
    message = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages = message,
        temperature=0.2,
        max_tokens=1000,
        frequency_penalty=0.0
    )
    steps = response['choices'][0]["message"]["content"].split('\n\n')

    return steps
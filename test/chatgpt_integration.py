import openai
import json

with open('openai_key.json') as f:
    openai.api_key = json.load(f)['key']

def get_how_to(query):
    prompt = f"Provide up to five concise steps with rationales for the following how-to query:\n\n{query}\n\nSteps:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    req = response['choices'][0]['text'].split('Rationales:')
    steps = req[0].split('\n')
    if len(req) > 1:
        rationales = req[1].split('\n')
    else:
        rationales = []
        
    return steps, rationales
import openai
import os
import json

# Read the API key from the environment
api_key = os.environ.get('OPENAI_API_KEY')

# Pass the API key to the openai package
openai.api_key = api_key

def generate_rhyme():
    prompt = "Was reimt sich auf Summe"

    try:
        response = openai.Completion.create(
            engine= "text-davinci-002",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.3,
            )

        rhyme = response["choices"][0]["text"]
        return {'statusCode': 200, 'body': json.dumps(rhyme)}
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps(str(e))}

generate_rhyme()

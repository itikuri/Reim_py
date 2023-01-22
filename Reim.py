import openai
import os

# Read the API key from the environment
api_key = os.environ.get('OPENAI_API_KEY')

# Pass the API key to the openai package
openai.api_key = api_key

def generate_rhyme():
    prompt = "Was reimt sich auf Summe"

    # Set the endpoint to text-davinci-002
    options = {
        "prompt": prompt,
        "max_tokens": 100,
        "model": "text-davinci-002"
    }

    try:
        response = openai.Completion.create(options)
        print(response["choices"][0]["text"])
    except Exception as e:
        print(e)

generate_rhyme()

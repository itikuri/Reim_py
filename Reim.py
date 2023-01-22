import openai
import os

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

        print(response["choices"][0]["text"])
    except Exception as e:
        print(e)

generate_rhyme()

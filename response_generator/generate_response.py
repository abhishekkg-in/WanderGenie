from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()
api_key = os.getenv('FIREWORKS_API_KEY')


def generate_response_from_llama(query):
    url = "https://api.fireworks.ai/inference/v1/chat/completions"
    payload = {
      "model": "accounts/fireworks/models/llama-v3p3-70b-instruct",
      "max_tokens": 4096,
      "top_p": 1,
      "top_k": 40,
      "presence_penalty": 0,
      "frequency_penalty": 0,
      "temperature": 0.6,
      "messages": [
        {
          "role": "user",
          "content": f"{query}"
        }
      ]
    }
    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json",
      "Authorization": f"Bearer {api_key}"
    }


    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    response_formated = json.loads(response.text).get("choices")[0].get("message").get("content")

    return  response_formated


def main():
    q = "generate a code to categorize anagrams from a list"
    print(generate_response_from_llama(q))


if __name__=="__main__":
    main()
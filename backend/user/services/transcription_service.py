import os
import requests


def transcribe_audio(file_path):

    api_key = os.getenv("DEEPGRAM_API_KEY")

    if not api_key:
        raise Exception("Deepgram API key not found")

    url = "https://api.deepgram.com/v1/listen"

    headers = {
        "Authorization": f"Token {api_key}",
        "Content-Type": "application/octet-stream",
    }

    params = {
        "model": "nova-2",
        "punctuate": "true",
        "smart_format": "true",
    }


    with open(file_path, "rb") as audio:
        response = requests.post(
            url,
            headers=headers,
            params=params,
            data=audio
        )

   
    response.raise_for_status()

    return response.json()

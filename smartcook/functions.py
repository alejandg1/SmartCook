import tiktoken
import requests
from django.template.loader import get_template
import os
import base64
from PIL import Image

directory = 'smartcook/media/'


def saveImg(image64):
    try:
        if os.path.exists(directory+'image.jpg'):
            os.remove(directory+'image.jpg')
        image = base64.b64decode(image64)
        with open(directory+'image.jpg', 'wb') as f:
            f.write(image)
        return True
    except Exception as e:
        print(e)
        return False


def showTokens(img):
    try:
        enc = tiktoken.encoding_for_model("gpt-4o")
        tokens = enc.encode(img)
        print(len(tokens))
    except Exception as e:
        print(e)


def compress():
    try:
        if os.path.exists(directory+'compressed.jpg'):
            os.remove(directory+'compressed.jpg')
        image = Image.open(directory+'image.jpg')
        quality = 40
        image.save(directory+'compressed.jpg', quality=quality)

        with open(directory+'image.jpg', 'rb') as f:
            img = base64.b64encode(f.read()).decode('utf-8')
        with open(directory+'compressed.jpg', 'rb') as f:
            imgC = base64.b64encode(f.read()).decode('utf-8')
        showTokens(img)
        showTokens(imgC)
        return True
    except Exception as e:
        print(e)
        return None


class Recipe:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name


def GPT():
    path = directory+'compressed.jpg'
    with open(path, 'rb') as f:
        img = base64.b64encode(f.read()).decode('utf-8')
    prompt = 'Eres un ayudante de cocina, detecta y lista, los ingredientes de cocina que encuentras en la imagen,no listes ingredientes que no sean plenamente reconocidos, no generes ingredientes que no estén en la imagen,luego lista recetas que se puedan preparar con los ingredientes detectados, cada receta debe tener su nombre, ingredientes y pasos de preparación'
    key = 'sk-proj-7YahWZVoc8lPw6VivwEnT3BlbkFJeUtCp4Kv6QcdsKqhh5ot'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{img}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 200
    }
    resp = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=payload)
    print(resp.json())
    return resp.json()


def temp():
    return get_template('components/recipe.html')

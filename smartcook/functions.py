import tiktoken
import re
import json
import requests
from django.template.loader import get_template
import os
import base64
from PIL import Image

directory = 'smartcook/media/'


def parse_resp(resp):
    try:
        data = resp['choices'][0]['message']['content']
        json_resp = {
            "recipes": []
        }
        recetas = data.split('Ingredientes en la imagen:')
        for receta in recetas:
            if receta == '':
                continue
            ingredientes = receta.split('**Ingredientes:**')[1]
            titulo = data.split(
                '**Ingredientes:**')[0].split('\n\n')[2]
            titulo = re.sub(r'#', '', titulo)
            titulo = re.sub(r'\d', '', titulo)
            titulo = re.sub(r'\.', '', titulo)
            ingredientes = receta.split(
                '**Ingredientes:**')[1].split('**Pasos:**')[0].split('\n')
            length = len(ingredientes)
            fix_list = [i for i in ingredientes if i != "" and i != " " and i]
            ingredientes = fix_list
            length = len(fix_list)
            for i in range(length):
                fix_list[i] = re.sub(r'- ', '', fix_list[i])
            pasos = receta.split('**Pasos:**')[1].split('\n')
            fix_list = [i for i in pasos if i != "" and i != " " and i]
            pasos = fix_list
            for i in range(len(pasos)):
                pasos[i] = re.sub(r'\d. ', '', pasos[i])
            json_resp['recipes'].append(
                {
                    "nombre": titulo,
                    "ingredientes": ingredientes,
                    "pasos": pasos
                }
            )
        print(json_resp)
        return json_resp
    except Exception as e:
        print(e)
        return None, None


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
    with open('response.json', 'w') as f:
        json.dump(resp.json(), f)
    data = parse_resp(resp.json())
    print(data)
    return data


def temp():
    return get_template('components/recipe.html')

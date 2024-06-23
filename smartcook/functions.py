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
            "ingredients": [],
            "recipes": []
        }
        recetas = data.split('### Recetas')[1].split('*Nombre:*')
        fix_list = [i for i in recetas if i !=
                    "" and i != " " and i and i != '\n\n']
        recetas = fix_list
        for receta in recetas:
            if receta == '':
                continue
            titulo = data.split(
                '*Ingredientes:*')[0].split('*Nombre:*')[1]
            titulo = re.sub(r'#', '', titulo)
            titulo = re.sub(r'\d', '', titulo)
            titulo = re.sub(r'\.', '', titulo)

            ingredientes = receta.split('*Ingredientes:*')[0]
            ingredientes = re.sub(r'- ', '', ingredientes)
            ingredientes = ingredientes.split('\n')
            fix_list = [i for i in ingredientes if i !=
                        "" and i != " " and i and '#' not in i and '*' not in i]
            ingredientes = fix_list

            pasos = receta.split('*Pasos:*')[1]
            pasos = re.sub(r'\d. ', '', pasos)
            pasos = pasos.split('\n')
            fix_list = [i for i in pasos if i !=
                        "" and i != " " and i and i != '**']
            pasos = fix_list
            print(pasos)

            detected = data.split('\n\n')[0]
            detected = re.sub(r'- ', '', detected)
            detected = re.sub(r'### Ingredientes', '', detected)
            detected = re.sub(r'\d. ', '', detected)
            detected = detected.split('\n')
            fix_list = [i for i in detected if i != "" and i !=
                        " " and i and i != '*Ingredientes*' and i != '*ingredientes*']
            detected = fix_list

            json_resp['ingredients'] = detected
            json_resp['recipes'].append(
                {
                    "nombre": titulo,
                    "ingredientes": ingredientes,
                    "pasos": pasos
                }
            )
        return json_resp
    except Exception as e:
        print("error")
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


def compress():
    try:
        if os.path.exists(directory+'compressed.jpg'):
            os.remove(directory+'compressed.jpg')
        image = Image.open(directory+'image.jpg')
        quality = 40
        image.save(directory+'compressed.jpg', quality=quality)
        return True
    except Exception as e:
        print(e)
        return None


class Recipe:
    def __init__(self, name, description):
        self.name = name
        self.ingredients = []
        self.description = description

    def __str__(self):
        return self.name

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)


def GPT():
    path = directory+'compressed.jpg'
    with open(path, 'rb') as f:
        img = base64.b64encode(f.read()).decode('utf-8')
    prompt = 'Eres un ayudante de cocina, detecta y lista, los ingredientes de cocina que encuentras en la imagen,no listes ingredientes que no sean plenamente reconocidos, no generes ingredientes que no estén en la imagen,luego lista recetas que se puedan preparar con los ingredientes detectados, cada receta debe tener su nombre, ingredientes y pasos de preparación, las cabeceras deben ser: ingredientes,recetas,nombre,pasos, solo el encabezado recetas y el encabezado ingredientes deben estar como H3, las partes de cada receta deben marcarse de esta forma: *nombre*, el resto del texto debe ser texto corriente'
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
        "temperature": 0.3,
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

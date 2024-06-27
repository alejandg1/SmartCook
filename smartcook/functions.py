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
        recetas = data.split('### recetas')[1].split('*nombre:*')
        fix_list = [i for i in recetas if i !=
                    "" and i != " " and i and i != '\n\n' and i != '\n']
        recetas = fix_list

        detected = data.split('\n\n')[0]
        detected = re.sub(r'- ', '', detected)
        detected = re.sub(r'### ingredientes', '', detected)
        detected = re.sub(r'\d. ', '', detected)
        detected = detected.split('\n')
        fix_list = [i for i in detected if i != "" and i !=
                    " " and i and i != '*ingredientes*'
                    and i != '*ingredientes*']
        detected = fix_list
        for receta in recetas:
            nombre = receta.split('*ingredientes:*')[0]
            nombre = re.sub(r'#', '', nombre)
            nombre = re.sub(r'\.', '', nombre)
            nombre = re.sub(r'\n', '', nombre)

            ingredientes = receta.split(
                '*ingredientes:*')[1].split('*pasos:*')[0]
            ingredientes = re.sub(r'- ', '', ingredientes)
            ingredientes = ingredientes.split('\n')
            fix_list = [i for i in ingredientes if i !=
                        "" and i != " " and i
                        and '#' not in i and '*' not in i]
            ingredientes = fix_list

            pasos = receta.split('*pasos:*')[1]
            pasos = re.sub(r'\d. ', '', pasos)
            pasos = re.sub(r'-. ', '', pasos)
            pasos = pasos.split('\n')
            fix_list = [i for i in pasos if i !=
                        "" and i != " " and i and i != '**'
                        and i != '-.']
            pasos = fix_list

            json_resp['ingredients'] = detected
            json_resp['recipes'].append(
                {
                    "nombre": nombre,
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
        if not os.path.exists(directory):
            os.makedirs(directory)
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
        if image.mode == "RGBA":
            image = image.convert("RGB")
        quality = 40
        image.save(directory+'compressed.jpg', quality=quality)
        return True
    except Exception as e:
        print("compress error")
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
    prompt = '''
            Detecta y lista los ingredientes de cocina que encuentras en la
            imagen, no listes ingredientes que no sean plenamente reconocidos,
            no generes ingredientes que no estén en la imagen,luego lista
            recetas que se puedan preparar con los ingredientes detectados,
            no generes texto que vaya a exceder los 300 tokens.
            La respuesta debe tener siempre el siguiente formato, no cambies
            el como están escritos los encabezados ni los separadores,
            no hagas cambios de ningun tipo en el formato:
            ### ingredientes
            - ingrediente 1
            - ingrediente 2
            - ingrediente n
            ### recetas
            *nombre:* Nombre de la receta
            *ingredientes:*
            - ingrediente 1
            - ingrediente n
            *pasos:*
            -. paso 1
            -. paso n
    '''
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
        "max_tokens": 300
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

import tiktoken
import openai
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
    # with open(directory+'compressed.jpg', 'rb') as f:
    #     img = base64.b64encode(f.read()).decode('utf-8')
    # print(img)
    # text = ''
    # key = ''
    # rep = openai.Completion.create(
    #     engine="gpt-4o",
    #     prompt=text,
    #     temperature=0.5,
    #     max_tokens=200,
    #     api_key=key,
    #     imput={
    #         "file": img,
    #         "prompt": text,
    #     }
    # )
    recipes = [
        Recipe('Receta 1', 'Descripcion 1'),
        Recipe('Receta 2', 'Descripcion 2'),
        Recipe('Receta 3', 'Descripcion 3')
    ]
    return recipes


def temp():
    return get_template('components/recipe.html')

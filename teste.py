from gettext import find
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
from csv import DictReader, DictWriter
from os import listdir, rename
import os.path
import asyncio
from os.path import isfile, join
import unicodedata
import re
from unidecode import unidecode
# 4ibq4au7

# print(unidecode('Arrepieí?'))

string = "Hey! Whát's up bro?"
# new_string = re.sub(r"[^a-zA-Z0-9]"," ",string)
# print(new_string)

def limpa_string(string):
    string = unidecode(string)
    string = re.sub(r"[^a-zA-Z0-9]"," ",string).strip().split()
    string = " ".join(string)
    return string

limpa_string(string)
# descricao = """Código Ref.: 65044A

# Material: Napa Croco na cor Preto;

# Enfeites: Zíper na Cor Preto;

# Palmilha: 8 mm de Espessura, Espuma em EVA, e Taloneira Napa Preto;

# Forro: Cacharrel, material espumado para maior conforto, na cor Preto;

# Salto: 10 cm de Altura e Revestido em Napa Croco na cor Preto;

# Solado de TR na cor Preto."
# Dimensões da Caixa: 31,5 x 30 x 9,5 cm
# Peso do Produto na Caixa: 1000 gramas (aproximadamente)"""



# estoque = {'34': '17', '35': '39', '36': '56', '37': '60', '38': '38', '39': '12'}
# marca = "Torricella"
# referencia = "65044A"
# titulo = "Bota Bico Fino Feminina"
# categoria = "Calçados Femininos Botas"
# preco = "R$ 179,90"

# obj = {

# 'referencia':referencia,
# 'titulo':titulo,
# 'categoria':categoria,
# 'preco': preco,
# 'descricao': descricao,
# 'estoque': estoque
# }



obj2 = {'referencia': 'teste', 'titulo': 'Bota Meia 7/8 Arrastão 0', 'categoria': 'Calçados Femininos Botas', 'marca': 'Torricella', 'descricao': 'Código Ref.: 65044A\n\nMaterial: Napa Croco na cor Preto;\n\nEnfeites: Zíper na Cor Preto;\n\nPalmilha: 8 mm de Espessura, Espuma em EVA, e Taloneira Napa Preto;\n\nForro: Cacharrel, material espumado para maior conforto, na cor Preto;\n\nSalto: 10 cm de Altura e Revestido em Napa Croco na cor Preto;\n\nSolado de TR na cor Preto.\nDimensões da Caixa: 31,5 x 30 x 9,5 cm\nPeso do Produto na Caixa: 1000 gramas (aproximadamente)', 'preco': 'R$ 179,90', 'estoque': '434', 'image0': 'img/65044A/Bota Bico Fino Feminina 0.jpg', 'image1': 'img/65044A/Bota Bico Fino Feminina 1.jpg', 'image2': 'img/65044A/Bota Bico Fino Feminina 2.jpg', 'image3': 'img/65044A/Bota Bico Fino Feminina 3.jpg', 'image4': 'img/65044A/Bota Bico Fino Feminina 4.jpg', 'image5': 'img/65044A/Bota Bico Fino Feminina 5.jpg', 'image6': 'img/65044A/Bota Bico Fino Feminina 6.jpg', 'image7': 'img/65044A/Bota Bico Fino Feminina 7.jpg', 'image8': 'img/65044A/Bota Bico Fino Feminina 8.jpg', 'image9': 'img/65044A/Bota Bico Fino Feminina 9.jpg', 'image10': 'img/65044A/Bota Bico Fino Feminina 10.jpg'}




# print(obj)

# def record_csv(obj):

#     headers = ['referencia', 'titulo', 'categoria', 'preco', 'descricao', 'variacao', 'estoque', 'marca', 'image0', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8', 'image9', 'image10', 'video1']
#     if not os.path.isfile('data.csv'):
#         with open('data.csv', "a+") as f:
#             writer = DictWriter(f, fieldnames=headers)
#             writer.writeheader()
#             f.close()

#     if type(obj['estoque']) == str:
#         loop = 1
#     else:
#         loop = len(obj['estoque'])    

#     estoque = obj['estoque']
#     for i in range(loop):
#         with open('data.csv', "r+") as f:

#             open_file = f.readlines()
#             if type(estoque) == str:
#                 obj['estoque'] = ''                 
#                 obj['estoque'] = estoque
#             else:
#                 obj['variacao'] = '' 
#                 obj['variacao'] = list(estoque.keys())[i]
#                 obj['estoque'] = '' 
#                 obj['estoque'] = list(estoque.values())[i]
                

#             kwargs = [{**obj}]
#             writer = DictWriter(f, fieldnames=headers)
#             writer.writerows(kwargs)
#             f.close()

# record_csv(obj2)


def rename_file_and_move(data):
    if not os.path.isdir(f'./img/{data["referencia"]}'):
        os.makedirs(f'./img/{data["referencia"]}')
    
    while any([filename.endswith(".crdownload") for filename in 
            listdir("./img")]):
        time.sleep(1)
    
    acha_novo_arquivo = [f for f in listdir('./img/') if isfile(join('./img/', f))][0]
    conta_arquivos = len(listdir(f'./img/{data["referencia"]}'))
    
    
    arquivo, extensao = os.path.splitext(acha_novo_arquivo)
    titulo = data['titulo'].replace('/',"")
    new_name = f'img/{data["referencia"]}/{titulo} {conta_arquivos}{extensao}'
    rename(f'./img/{acha_novo_arquivo}', f'./{new_name}')
    
    # data_to_record[f'image{conta_arquivos}'] = new_name
    return None


rename_file_and_move(obj2)


# for i in range(5):

#     asyncio.get_event_loop()

  
# to run the above function we'll 
# use Event Loops these are low 
# level functions to run async functions


  
# You can also use High Level functions Like:
# asyncio.run(function_asyc())
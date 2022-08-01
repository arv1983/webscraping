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

# data = {'referencia': '1000-66C', 'titulo': 'Sandália Rasteira de Dedo', 'categoria': 'Calçados Femininos Rasteiras', 'preco': 'R$ 46,90', 'descricao': 'Código Ref.: 1000-66C\n\nMaterial: Napa Off White / Napa Serpente Off White;\n\nEnfeite: Fivela de Ajuste na Cor Ouro Light, Tiras em Napa Serpente Off White e Canudo de Vinil na tira do dedo;\n\nPalmilha: 4 mm de Espessura, Espuma em EVA, Revestida em Napa Off White;\n\nSolado em PVC Flexível com antiderrapante e na cor Bege.\nDimensões da Caixa: 30 x 16 x 9,5 cm\nPeso do Produto na Caixa: 400 gramas (aproximadamente)', 'variacao': '34', 'estoque': {'34': '5', '35': '6', '36': '17', '37': '12', '38': '6', '39': '4'}, 'marca': 'Torricella', 'image0': 'img/1000-66C/Sandalia Rasteira de Dedo 0.jpg', 'image1': 'img/1000-66C/Sandalia Rasteira de Dedo 1.jpg', 'image2': 'img/1000-66C/Sandalia Rasteira de Dedo 2.jpg', 'image3': 'img/1000-66C/Sandalia Rasteira de Dedo 3.jpg', 'image4': 'img/1000-66C/Sandalia Rasteira de Dedo 4.jpg', 'image5': '', 'image6': '', 'image7': '', 'image8': '', 'image9': '', 'image10': '', 'image11': '', 'image12': '', 'image13': '', 'image14': '', 'image15': '', 'video1': ''}


# # for i in range(len(data['estoque']) -1):
# #     print(i)


# # for i, k in enumerate(data['estoque']):

# #     # print(data['estoque'][k])
# #     print(k)
# #     # print(k)

# def calcula_preco(preco):
#     COMISSAO_SHOPEE = 0.12
#     COMISSAO_FABRICANTE = 0.10
    
#     custo_produto = preco * COMISSAO_FABRICANTE + preco
    
#     print(custo_produto)



# calcula_preco(50)

        
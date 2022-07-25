from gettext import find
from optparse import OptionContainer
from numpy import empty, ones
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time, asyncio, os.path, re
from csv import DictReader, DictWriter
from os import listdir, rename
from os.path import isfile, join
# from unidecode import unidecode
from category import Category


# for i in range(len(get_data)):
async def login():
    time.sleep(10)
    driver.find_element(By.XPATH, "//*[@id='shop-login']/div[1]/div/div/div/div/input").send_keys("ciclista-rs@hotmail.com")
    driver.find_element(By.XPATH, "//*[@id='shop-login']/div[2]/div/div[1]/div/div/input").send_keys("Arv5683-3")
    driver.find_element(By.XPATH, "//*[@id='shop-login']/div[4]/div/div/button").click()
    time.sleep(10)
    return None

async def add_basic_Information_images_and_videos(ref, titulo, descricao):
    imagens = [f for f in listdir(f'./img/{ref}') if os.path.splitext(f)[1] == ".jpg"]
    videos = [f for f in listdir(f'./img/{ref}') if os.path.splitext(f)[1] == ".mp4"]

    for i in range(len(imagens)):
        driver.find_element(By.XPATH, f"//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[1]/div[2]/div[1]/div[{i + 1}]/div/div/div[1]/div/div/div/input").send_keys(os.path.abspath(f'img/{ref}/{imagens[i]}'))
        time.sleep(3) 


    if videos:
        driver.find_element(By.XPATH, f"//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[2]/div[2]/div/div/div/div/input").send_keys(os.path.abspath(f'img/{ref}/{videos[0]}'))
        time.sleep(5) 
        

    # Titulo
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[3]/div[2]/div/div/div/div/div/input").clear()
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[3]/div[2]/div/div/div/div/div/input").send_keys(titulo)
    # descricao
    time.sleep(1) 
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[4]/div[2]/div/div/div/div[1]/textarea").send_keys(descricao)
    time.sleep(1) 

    return None

async def specify_products(data):
    time.sleep(1)
    # Marca - CLICK
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[2]/div/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div").click()
    time.sleep(1)
    # MARCA nome da marca
    driver.find_element(By.XPATH, "/html/body/div[6]/ul/div[1]/div/input").send_keys("Torricella")
    time.sleep(1)
    # Seleciona torricela - click
    driver.find_element(By.XPATH, "/html/body/div[6]/ul/div[2]/div/div[1]").click()
    time.sleep(1)
    # Seleciona origem Brasil CLICK
    driver.find_element(By.XPATH, "/html/body/div[8]/ul/div[2]/div/div[13]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[7]/ul/div[2]/div/div[3]").click()    
    return None


async def variation(data):
    # NOME DA VARIACAO "Tamanho"
    print(data)
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[1]/div[2]/div/button").click()
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div/input").send_keys("Tamanho")


# Chega esses dados
# {'referencia': '1000-66C', 'titulo': 'Sandália Rasteira de Dedo', 'categoria': 'Calçados Femininos Rasteiras', 'preco': 'R$ 46,90', 'descricao': 'Código Ref.: 1000-66C\n\nMaterial: Napa Off White / Napa Serpente Off White;\n\nEnfeite: Fivela de Ajuste na Cor Ouro Light, Tiras em Napa Serpente Off White e Canudo de Vinil na tira do dedo;\n\nPalmilha: 4 mm de Espessura, Espuma em EVA, Revestida em Napa Off White;\n\nSolado em PVC Flexível com antiderrapante e na cor Bege.\nDimensões da Caixa: 30 x 16 x 9,5 cm\nPeso do Produto na Caixa: 400 gramas (aproximadamente)', 'variacao': '34', 'estoque': {'34': '5', '35': '6', '36': '17', '37': '12', '38': '6', '39': '4'}, 'marca': 'Torricella', 'image0': 'img/1000-66C/Sandalia Rasteira de Dedo 0.jpg', 'image1': 'img/1000-66C/Sandalia Rasteira de Dedo 1.jpg', 'image2': 'img/1000-66C/Sandalia Rasteira de Dedo 2.jpg', 'image3': 'img/1000-66C/Sandalia Rasteira de Dedo 3.jpg', 'image4': 'img/1000-66C/Sandalia Rasteira de Dedo 4.jpg', 'image5': '', 'image6': '', 'image7': '', 'image8': '', 'image9': '', 'image10': '', 'image11': '', 'image12': '', 'image13': '', 'image14': '', 'image15': '', 'video1': ''}


    # Adicionar opçones (se tem 8 opcoes clicar 7)

    # for i in range(len(data[]))
    # driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[1]/div[1]/div[2]/div/div[3]/div[2]/div/button").click() 
    


    # Coloca os tamanhanhos
    # //*[@id="app"]/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/input
    # //*[@id="app"]/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div/input
    # //*[@id="app"]/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[3]/div/div/div/div/div/input


    # Preco do produto
    # //*[@id="app"]/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[2]/div[1]/div[2]/form/div[1]/div/div/div/div/input

    # // aplicar em todos - CLICK
    # //*[@id="app"]/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[2]/div[1]/div[2]/button

    # 34..
    # //*[@id="app"]/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/input
    # 35..
    # //*[@id="app"]/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div/input

    # OPCAO click se tiva mais uma
    # //*[@id="app"]/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/input

    # edita estoque
    # 34..
    # //*[@id="app"]/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/input
    # 35..
    # //*[@id="app"]/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div/input





options = Options()

chromeOptions = webdriver.ChromeOptions()
# chromeOptions.add_argument("user-data-dir=/home/anderson/perfil/")

chromeOptions.add_argument("user-data-dir=/home/anderson/perfil/")
# chromeOptions.add_argument("user-data-dir=/home/anderson/.config/google-chrome/")
# chromeOptions.add_argument("profile-directory=Default")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chromeOptions)



url = "https://seller.shopee.com.br/portal/product/category"
driver.get(url) 



# asyncio.run(login())

time.sleep(10)
qty_sku = len(listdir(f'./img/'))
get_reference = listdir(f'./img/')[0]


diferentes = []


# for i in range(len(listdir(f'./img/'))):
for i in range(10):
 
    sku = listdir(f'./img/')[i]
    print(sku)

    with open('data.csv', "r") as f:
        open_file = f.readlines()
        get_data = []
        variacao = []
        estoque = []
        for data in DictReader(open_file):
            if(data['referencia'] == sku):
                
                if not get_data:
                    get_data.append(data)
                variacao.append(data['variacao'])
                estoque.append(data['estoque'])
                
        
        # print(variacao)

        if get_data[0]['variacao'] == '':
            get_data[0].pop('variacao')
            get_data[0].pop('estoque')
            get_data[0]['estoque'] = estoque[0]
        else:
            get_data[0]['estoque'] = dict(zip(variacao, estoque))
      
        
        

        match get_data[0]['categoria']:
            case 'Calçados Femininos Botas':
                asyncio.run(Category.botas(driver))
                
            case 'Calçados Femininos Tênis':
                asyncio.run(Category.tenis(driver))
                # break
            case 'Calçados Femininos Sapato Scarpin':
                asyncio.run(Category.scarpin(driver))
                # break
            case 'Calçados Femininos Sandálias':
                asyncio.run(Category.sandalia(driver))            
                
                
            case 'Calçados Femininos Anabela':
                asyncio.run(Category.anabela(driver))            
                # break
            case 'Calçados Femininos Meia Pata':
                asyncio.run(Category.meiapata(driver))   
                print('fim meia pata')         
                # break
            case 'Calçados Femininos Rasteiras':
                print('inicio rasteira')         
                asyncio.run(Category.rasteira(driver))            
                # break
                print('fim rasteora')
            case 'Calçados Femininos Sapato Peep Toe':
                asyncio.run(Category.peeptoe(driver))            
                # break
            case 'Calçados Femininos Bolsas':
                asyncio.run(Category.bolsa(driver))         
                # break
        


        asyncio.run(add_basic_Information_images_and_videos(get_data[0]['referencia'], get_data[0]['titulo'], get_data[0]['descricao']))
        print('fimnmmmmmmm')
        asyncio.run(variation(get_data[0]))
        time.sleep(50)
        





# variacoes




# lista = []
# for e in diferentes:

#     if e not in lista:
#         lista.append(e)

# print('lista')
# print(lista)
# print('diferentes')
# print(diferentes)

        

        
        # asyncio.run(Category.categoria_botas(driver))
        






















#     #     data_complete.append({'id': int(data['id']), 'name': data['name'], 'email': data['email'], 'age': int(data['age']), 'password': data['password']})    
#     # f.close()
#     # if(edit_data):
#     #     edit_data.pop('password')
#     #     with open('users.csv', 'w') as file:
#     #         writer = DictWriter(file, fieldnames=headers)
#     #         writer.writeheader()
#     #         writer.writedatas(data_complete)
#     #         file.close()
#     #     return jsonify(edit_data)







# time.sleep(10) 





# imagem1
# driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div[1]/div/div/div/input").send_keys("/home/anderson/Área de Trabalho/webscraping/img/T0057/Tenis Feminino 0.jpg")
# # imagem2
# driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div/div/div/input").send_keys("/home/anderson/Área de Trabalho/webscraping/img/T0057/Tenis Feminino 0.jpg")
# # imagem3
# driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[1]/div[2]/div[1]/div[3]/div/div/div[1]/div/div/div/input").send_keys("/home/anderson/Área de Trabalho/webscraping/img/T0057/Tenis Feminino 0.jpg")
# # imagem4
# driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[1]/div[2]/div[1]/div[4]/div/div/div[1]/div/div/div/input").send_keys("/home/anderson/Área de Trabalho/webscraping/img/T0057/Tenis Feminino 0.jpg")
# # imagem5
# driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[1]/div[2]/div[1]/div[5]/div/div/div[1]/div/div/div/input").send_keys("/home/anderson/Área de Trabalho/webscraping/img/T0057/Tenis Feminino 0.jpg")
# # imagem6
# driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[1]/div[2]/div[1]/div[6]/div/div/div[1]/div/div/div/input").send_keys("/home/anderson/Área de Trabalho/webscraping/img/T0057/Tenis Feminino 0.jpg")
# # imagem7
# driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[1]/div[2]/div[1]/div[7]/div/div/div[1]/div/div/div/input").send_keys("/home/anderson/Área de Trabalho/webscraping/img/T0057/Tenis Feminino 0.jpg")
# # imagem8
# driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[1]/div[2]/div[1]/div[8]/div/div/div[1]/div/div/div/input").send_keys("/home/anderson/Área de Trabalho/webscraping/img/T0057/Tenis Feminino 0.jpg")


# time.sleep(10) 

# time.sleep(120) 


from gettext import find
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






        




        # for i in range(len(get_data)):
def login():
    time.sleep(18)
    driver.find_element(By.XPATH, "//*[@id='shop-login']/div[1]/div/div/div/div/input").send_keys("arv-83@hotmail.com")
    driver.find_element(By.XPATH, "//*[@id='shop-login']/div[2]/div/div[1]/div/div/input").send_keys("Arv5683-3")
    driver.find_element(By.XPATH, "//*[@id='shop-login']/div[4]/div/div/button").click()
    time.sleep(30)


async def nome_e_categoria(data):
    # nome do produto
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[2]/div/div/div/div/div/input").send_keys("nome do produto")
    time.sleep(1) 
    # busca categoria
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div/input").send_keys("bota")
    time.sleep(1) 
    # clica em sapatos femininos
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[1]/li[2]/p").click()
    time.sleep(1) 
    # clica em botas
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[2]/li[1]/p").click()
    time.sleep(1) 
    # clica em botas da moda
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[3]/li[2]/p").click()
    time.sleep(1) 
    # clica em proximo
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/button").click()
    time.sleep(3) 



async def add_images_and_videos(ref):
    imagens = [f for f in listdir(f'./img/{ref}') if os.path.splitext(f)[1] == ".jpg"]
    videos = [f for f in listdir(f'./img/{ref}') if os.path.splitext(f)[1] == ".mp4"]

    # os.path.abspath(path)
    for i in range(len(imagens)):
        driver.find_element(By.XPATH, f"//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[1]/div[2]/div[1]/div[{i + 1}]/div/div/div[1]/div/div/div/input").send_keys(os.path.abspath(f'img/{ref}/{imagens[i]}'))
        time.sleep(1) 

    if videos:
        print("tem videos")
        driver.find_element(By.XPATH, f"//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[2]/div[2]/div/div/div/div/input").send_keys(os.path.abspath(f'img/{ref}/{videos[0]}'))
        time.sleep(1) 








options = Options()

time.sleep(2)

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("user-data-dir=home/anderson/.config/google-chrome/Anderson")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chromeOptions)

options = webdriver.ChromeOptions() 

url = "https://seller.shopee.com.br/portal/product/category"
driver.get(url) 


login()



qty_sku = len(listdir(f'./img/'))
get_reference = listdir(f'./img/')[0]
for i in range(1):
    sku = listdir(f'./img/')[i]

    with open('data.csv', "r") as f:
        open_file = f.readlines()
        get_data = []
        variacao = []
        estoque = []
        for data in DictReader(open_file):
            if(data['referencia'] == sku):
                get_data.append(data)
                variacao.append(data['variacao'])
                estoque.append(data['estoque'])
                
        data['estoque'] = dict(zip(variacao, estoque))
        data.pop('variacao')

        asyncio.run(nome_e_categoria(data))






















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





# # imagem1
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


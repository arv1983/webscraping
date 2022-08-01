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
import time, asyncio, os.path
from csv import DictReader
from os import listdir, rename
from os.path import isfile, join
from category import Category
from preco import Preco
from selenium.webdriver.common.action_chains import ActionChains

from senhas import Senhas

options = Options()

chromeOptions = webdriver.ChromeOptions()

chromeOptions.add_argument("user-data-dir=/home/anderson/perfil/")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chromeOptions)

actions = ActionChains(driver)

url = "https://seller.shopee.com.br/portal/product/category"
driver.get(url) 

time.sleep(10)
qty_sku = len(listdir(f'./img/'))
get_reference = listdir(f'./img/')[0]


diferentes = []

async def login():
    time.sleep(10)
    driver.find_element(By.XPATH, "//*[@id='shop-login']/div[1]/div/div/div/div/input").send_keys(Senhas.email)
    driver.find_element(By.XPATH, "//*[@id='shop-login']/div[2]/div/div[1]/div/div/input").send_keys(Senhas.shopeesenha)
    driver.find_element(By.XPATH, "//*[@id='shop-login']/div[4]/div/div/button").click()
    time.sleep(10)
    return None

async def add_basic_Information_images_and_videos(ref, titulo, descricao):
    imagens = [f for f in listdir(f'./img/{ref}') if os.path.splitext(f)[1] == ".jpg"]
    videos = [f for f in listdir(f'./img/{ref}') if os.path.splitext(f)[1] == ".mp4"]
    for i in range(len(imagens)):

        if i < 9:
            driver.find_element(By.XPATH, f"//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[1]/div[2]/div[1]/div[{i + 1}]/div/div/div[1]/div/div/div/input").send_keys(os.path.abspath(f'img/{ref}/{imagens[i]}'))
            time.sleep(3) 

    if videos:
        driver.find_element(By.XPATH, f"//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[2]/div[2]/div/div/div/div/input").send_keys(os.path.abspath(f'img/{ref}/{videos[0]}'))
        time.sleep(10) 
        try:
            driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[3]/div[2]/button[2]").click()
            time.sleep(5)
        except:                                                                                                      
            None
        try:
            driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div/div[3]/div[2]/button[2]").click()
            time.sleep(5)
        except:                                                                                                      
            None

    # Titulo
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[3]/div[2]/div/div/div/div/div/input").clear()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[3]/div[2]/div/div/div/div/div/input").send_keys(titulo)
    # descricao
    time.sleep(1) 
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[1]/div/div/div[4]/div[2]/div/div/div/div[1]/textarea").send_keys(descricao)
    time.sleep(1) 

    return None

async def specify_products():
    
    time.sleep(2)                
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[3]/div[1]/ul/li[2]/a").click()
    time.sleep(1)                
    # Marca - CLICK
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[2]/div/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div").click()
    time.sleep(2)
    # MARCA nome da marca        
    try:
        driver.find_element(By.XPATH, "/html/body/div[6]/ul/div[1]/div/input").send_keys("Torricella")
    except:
        driver.find_element(By.XPATH, "/html/body/div[7]/ul/div[1]/div/input").send_keys("Torricella")

    
    
    
    time.sleep(3)
    # Seleciona torricela - click
    try:
        driver.find_element(By.XPATH, "/html/body/div[6]/ul/div[2]/div/div[1]").click()
    except:
        driver.find_element(By.XPATH, "/html/body/div[7]/ul/div[2]/div/div").click()
                                   
    time.sleep(1)
    # Seleciona origem Brasil CLICK
    # driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[2]/div/div[2]/div/div[5]/div/div[2]/div/div/div/div/div/div/div[1]").click()
    # time.sleep(1)

    # driver.find_element(By.XPATH, "/html/body/div[7]/ul/div[1]/div/input").send_keys("Brasil")
    # time.sleep(1)
    # driver.find_element(By.XPATH, "/html/body/div[7]/ul/div[2]/div/div[13]").click()    
    return None


async def variation(data):
    time.sleep(1)           
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[3]/div[1]/ul/li[3]/a").click()
    time.sleep(1)    
    if type(data['estoque']) == dict:
        # CLICA EM HABILITAR VARIACAO
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[1]/div[2]").click()
        time.sleep(1)
        # NOME DA VARIACAO "Tamanho"
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div/input").send_keys("Tamanho")
        time.sleep(1)
        for i, k in enumerate(data['estoque']):
            if i != 1:
                # # Clica em add variaçoes
                driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[1]/div[1]/div[2]/div/div[3]/div[2]/div/button").click()
                time.sleep(1)

            # variacao
            driver.find_element(By.XPATH, f"//*[@id='app']/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[{i + 1}]/div/div/div/div/div/input").send_keys(k)
            time.sleep(1)           
            # estoque
            print('-----------------')   
            driver.find_element(By.XPATH, f"//*[@id='app']/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[{i+1}]/div[2]/div/div/div/div/div/div/div/div/input").send_keys(data['estoque'][k])
            time.sleep(1)           
            # PRECO
            print('+++++++++++++++++')
            driver.find_element(By.XPATH, f"//*[@id='app']/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[{i+1}]/div[1]/div/div/div/div/div/div/input").send_keys(Preco.precifica(data['preco']))
            time.sleep(1)
    else:
        # PRECO   
        
        driver.find_element(By.XPATH, f"//*[@id='app']/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div/input").send_keys(Preco.precifica(data['preco']))
        time.sleep(1)
        
        driver.find_element(By.XPATH, f"//*[@id='app']/div[2]/div/div/div/div/div[1]/section[3]/div/div[1]/div[3]/div[2]/div/div/div/div/div/div/div/input").send_keys(data['estoque'])
        time.sleep(1)

    print('terminou variacao')
    return None

async def ship():
    time.sleep(1)           
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[3]/div[1]/ul/li[4]/a").click()
    time.sleep(1)           
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[4]/div/div[1]/div[1]/div[2]/div/div/div/div/div/input").send_keys("0.50")
    time.sleep(1)           
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[4]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div/div/input").send_keys("25")
    time.sleep(1)           
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[4]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/input").send_keys("25")
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[4]/div/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/input").send_keys("25")
    time.sleep(2)           
    # driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[4]/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div").click()
    # time.sleep(1)           
    # driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div[1]/section[4]/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div").click()
    # time.sleep(1) 
    try:
        driver.find_element(By.CLASS_NAME, "shopee-switch--close").click()

    except:

        None
    
    return None          

async def others(sku):
    driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[1]/section[5]/div/div[3]/div[2]/div/div/div/div/div/input").send_keys(sku)
    time.sleep(1)           
    return None


# asyncio.run(login())


for i in range(len(listdir(f'./img/'))):
    if i < 559:
        continue
    sku = listdir(f'./img/')[i]

    print(i)
    print(sku)
    print(len(listdir(f'./img/')))

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

        if get_data[0]['variacao'] == '':
            get_data[0].pop('variacao')
            get_data[0].pop('estoque')
            get_data[0]['estoque'] = estoque[0]
        else:
            get_data[0]['estoque'] = dict(zip(variacao, estoque))
        print(get_data[0]['categoria'])
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

            case 'Calçados Femininos Sapatilhas':
                asyncio.run(Category.sandalia(driver))            
            case 'Calçados Femininos Anabela':
                asyncio.run(Category.anabela(driver))            
                # break
            case 'Calçados Femininos Meia Pata':
                asyncio.run(Category.meiapata(driver))   
                # break
            case 'Calçados Femininos Rasteiras':
                asyncio.run(Category.rasteira(driver))            
                # break
            case 'Calçados Femininos Sapato Peep Toe':
                asyncio.run(Category.peeptoe(driver))            
                # break
            case 'Calçados Femininos Bolsas':
                asyncio.run(Category.bolsa(driver))         
                # break
        time.sleep(5)
        asyncio.run(add_basic_Information_images_and_videos(get_data[0]['referencia'], get_data[0]['titulo'], get_data[0]['descricao']))
        asyncio.run(specify_products())
        asyncio.run(variation(get_data[0]))
        asyncio.run(ship())
        asyncio.run(others(get_data[0]['referencia']))
        
        # Grava  
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div[2]/div[1]/div/div[2]/button[3]").click()
        time.sleep(8)
        # add novo
        driver.find_element(By.XPATH, "//*[@id='product']/ul/li[2]/a").click()
        time.sleep(3)                  

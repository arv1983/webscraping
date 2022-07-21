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
from unidecode import unidecode
from senhas import Senhas


# 4ibq4au7

options = Options()

time.sleep(2)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "/home/anderson/Área de Trabalho/webscraping/img"}
chromeOptions.add_experimental_option("prefs",prefs)
# chromedriver = "path/to/chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chromeOptions)





url = "https://www.revendadecalcados.com.br/areadorevendedor/produtos"

driver.get(url) 


driver.find_element(By.ID, "requiredcodigo").send_keys(Senhas.email)
driver.find_element(By.ID, "requiredsenha").send_keys(Senhas.shopeesenha)
driver.find_element(By.XPATH, '//*[@id="acessar"]/input').click()
time.sleep(1) 
driver.find_element(By.XPATH, '//*[@id="navbar-collapse-1"]/ul/li[1]/a').click()
  

# clica em menu
driver.find_element(By.XPATH, '//*[@id="navbar-collapse-1"]/ul/li[1]/ul/li[4]').click()

# clica em todos os produtos
html = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div').get_attribute('outerHTML')
                                    
soup = BeautifulSoup(html, 'html.parser')


tds = soup.find_all(name='div', class_="listing-item")



def check_exists_by_xpath(path):

    try:
        driver.find_element(By.XPATH, path)
    except:
        return False

    return True



async def rename_file_and_move(data):
    if not os.path.isdir(f'./img/{data["referencia"]}'):
        os.makedirs(f'./img/{data["referencia"]}')
    
    while any([filename.endswith(".crdownload") for filename in 
            listdir("./img")]):
        time.sleep(1)
    
    acha_novo_arquivo = [f for f in listdir('./img/') if isfile(join('./img/', f))][0]
    conta_arquivos = len(listdir(f'./img/{data["referencia"]}'))

    arquivo, extensao = os.path.splitext(acha_novo_arquivo)
    titulo = limpa_string(data['titulo'])
    new_name = f'img/{data["referencia"]}/{titulo} {conta_arquivos}{extensao}'
    rename(f'./img/{acha_novo_arquivo}', f'./{new_name}')
    data_to_record[f'image{conta_arquivos}'] = new_name
    return None

def limpa_string(string):
    string = unidecode(string)
    string = re.sub(r"[^a-zA-Z0-9]"," ",string).strip().split()
    string = " ".join(string)
    return string

def record_csv(obj):

    headers = ['referencia', 'titulo', 'categoria', 'preco', 'descricao', 'variacao', 'estoque', 'marca', 'image0', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8', 'image9', 'image10', 'image11', 'image12', 'image13', 'image14', 'image15', 'video1']
    if not os.path.isfile('data.csv'):
        with open('data.csv', "a+") as f:
            writer = DictWriter(f, fieldnames=headers)
            writer.writeheader()
            f.close()

    if type(obj['estoque']) == str:
        loop = 1
    else:
        loop = len(obj['estoque'])    

    estoque = obj['estoque']
    for i in range(loop):
        with open('data.csv', "r+") as f:

            open_file = f.readlines()
            if type(estoque) == str:
                obj['estoque'] = ''                 
                obj['estoque'] = estoque
            else:
                obj['variacao'] = '' 
                obj['variacao'] = list(estoque.keys())[i]
                obj['estoque'] = '' 
                obj['estoque'] = list(estoque.values())[i]
                

            kwargs = [{**obj}]
            writer = DictWriter(f, fieldnames=headers)
            writer.writerows(kwargs)
            f.close()

#loop em todos os produtos

for i in range(len(tds)):

    data_to_record = {}
    # 357
    driver.find_element(By.XPATH, f'/html/body/div[6]/div[3]/div/div/div/div[{i + 357}]/div/div[2]/h6/a').click()
    # driver.find_element(By.XPATH, f'/html/body/div[6]/div[3]/div/div/div/div[{i + 357}]/div/div[2]/h6/a').click()

    data_to_record['referencia'] = driver.find_element(By.XPATH, "//*[contains(text(), 'Referência')]").text
    data_to_record['referencia'] = " ".join(data_to_record['referencia'].split()[1:])
    
    data_to_record['titulo'] = driver.find_element(By.CLASS_NAME, "page-title.text-left").text
    
    if check_exists_by_xpath("//*[contains(text(), 'Categoria')]"):
        data_to_record['categoria'] = driver.find_element(By.XPATH, "//*[contains(text(), 'Categoria')]").text
        data_to_record['categoria'] = " ".join(data_to_record['categoria'].split()[1:])
    
    if check_exists_by_xpath("//*[contains(text(), 'Marca')]"):
        data_to_record['marca'] = driver.find_element(By.XPATH, "//*[contains(text(), 'Marca')]").text
        data_to_record['marca'] = " ".join(data_to_record['marca'].split()[1:])


    data_to_record['descricao'] = driver.find_element(By.ID, "h2tab1").text

    # data_to_record['preco'] = driver.find_element(By.CLASS_NAME, "price").text
    data_to_record['preco'] = driver.find_element(By.XPATH, "//strong[contains(text(), 'R$')]").text

    if check_exists_by_xpath("//*[contains(text(), 'Confira abaixo o estoque disponível no momento')]"):
        variacoes = driver.find_element(By.CSS_SELECTOR, "[name*='form']").get_attribute('outerHTML')
        soup = BeautifulSoup(variacoes, 'html.parser')
        tds = soup.find_all(name='td')    
        tds = [valor.text for valor in tds if 'Confira' not in valor.text]
        metade = int((str(len(tds) / 2)).split('.')[0])
        numero = tds[:metade]
        estoque = tds[metade:]
        data_to_record['estoque'] = dict(zip(numero, estoque))
    else:
        qtd = driver.find_element(By.XPATH, "//*[contains(text(), 'Estoque disponível no momento: ')]").text
        data_to_record['estoque'] = qtd.split()[4:-1][0]

    time.sleep(2)  
    
    images = driver.find_elements(By.PARTIAL_LINK_TEXT, "Baixar sem")
        # PEGA IMAGEM OK
    for k in range(len(images)):
        driver.find_elements(By.PARTIAL_LINK_TEXT, "Baixar sem")[k].click()
        time.sleep(2) 

        asyncio.run(rename_file_and_move(data_to_record))
        
    videos = driver.find_elements(By.CSS_SELECTOR, "[title*='Assistir & Baixar Vídeo']")
    
    for v in range(len(videos)):
        driver.find_elements(By.CSS_SELECTOR, "[title*='Assistir & Baixar Vídeo']")[v].click()
        time.sleep(4)
        driver.find_element(By.ID, 'botaodownvideo').click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#ModalVideoProduto > div > div > div:nth-child(3) > div > button").click()
        time.sleep(2)
        asyncio.run(rename_file_and_move(data_to_record))
        driver.execute_script("window.history.go(-1)")
    time.sleep(2)         
    driver.execute_script("window.history.go(-1)")


    record_csv(data_to_record)


    time.sleep(2) 
    
time.sleep(5)  







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


# 4ibq4au7



# if not os.path.isfile("dados.csv"):
#     headers = ['id', 'sku', 'titulo', 'descricao', 'preco']
#     if not os.path.isfile(filename):
#         with open(filename, "a+") as f:
#             writer = DictWriter(f, fieldnames=headers)
#             writer.writeheader()
#             f.close()


options = Options()


# webdriver.ChromeOptions.experimental_options("download.default_directory", '/teste/imagem')
# chromePrefs.put("download.default_directory", '/teste/imagem')
# options = webdriver.ChromeOptions() 


# options.add_argument("download.default_directory=$PATH:/usr_teste/")



# options = webdriver.ChromeOptions() 
# options.add_argument("download.default_directory=///home/anderson/Downloads/sss/")

# prefs = {
# "download.default_directory": r"C:\Users\XXXX\downdir\stamp"+timestr,
# "download.prompt_for_download": False,
# "download.directory_upgrade": True
# }


time.sleep(2)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "/home/anderson/Área de Trabalho/webscraping/img"}
chromeOptions.add_experimental_option("prefs",prefs)
# chromedriver = "path/to/chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chromeOptions)


# driver = webdriver.Chrome(chrome_options=options)

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# url = "https://www.catalogodecalcados.com.br/estoque"
# driver.get(url) 
# driver.implicitly_wait(10)



# driver.find_element(By.ID, "revendedor").send_keys("arv-83@hotmail.com")
# time.sleep(1)  
# driver.find_element(By.ID, 'referencia').send_keys("1941")
# time.sleep(1)  
# driver.find_element(By.XPATH, '/html/body/div/div/input[6]').click()
# time.sleep(2)  

# html = driver.find_element(By.ID, "resultado").get_attribute('outerHTML')


# soup = BeautifulSoup(html, 'html.parser')


# tds = soup.find_all(name='td')

# for k in tds:
#     # teste = pd.read_html(k)
#     print(k.text)

def check_exists_by_xpath(path):

    try:
        driver.find_element(By.XPATH, path)
    except:
        return False

    return True


url = "https://www.revendadecalcados.com.br/areadorevendedor/produtos"

driver.get(url) 


driver.find_element(By.ID, "requiredcodigo").send_keys("arv-83@hotmail.com")
driver.find_element(By.ID, "requiredsenha").send_keys("4ibq4au7")
driver.find_element(By.XPATH, '//*[@id="acessar"]/input').click()
time.sleep(1) 
driver.find_element(By.XPATH, '//*[@id="navbar-collapse-1"]/ul/li[1]/a').click()
  

# clica em menu
driver.find_element(By.XPATH, '//*[@id="navbar-collapse-1"]/ul/li[1]/ul/li[4]').click()

# clica em todos os produtos
html = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div').get_attribute('outerHTML')
                                    
soup = BeautifulSoup(html, 'html.parser')


tds = soup.find_all(name='div', class_="listing-item")


#loop em todos os produtos

for i in range(len(tds)):

    data_to_record = {}

    driver.find_element(By.XPATH, f'/html/body/div[6]/div[3]/div/div/div/div[{i + 1}]/div/div[2]/h6/a').click()
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

    data_to_record['preco'] = driver.find_element(By.CLASS_NAME, "price").text

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
        estoque = qtd.split()[4:-1][0]

    time.sleep(2)  
    
    print(data_to_record['descricao'])        
    print(data_to_record['estoque'])
    print(data_to_record['marca'])
    print(data_to_record['referencia'])
    print(data_to_record['titulo'])
    print(data_to_record['categoria'])
    print(data_to_record['preco'])
    print('+++++')








    images = driver.find_elements(By.PARTIAL_LINK_TEXT, "Baixar sem")
        # PEGA IMAGEM OK
    for k in range(len(images)):
        driver.find_elements(By.PARTIAL_LINK_TEXT, "Baixar sem")[k].click()
        time.sleep(2) 
    
    videos = driver.find_elements(By.CSS_SELECTOR, "[title*='Assistir & Baixar Vídeo']")
    
    for v in range(len(videos)):
        driver.find_elements(By.CSS_SELECTOR, "[title*='Assistir & Baixar Vídeo']")[v].click()
        time.sleep(2)
        driver.find_element(By.ID, 'botaodownvideo').click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#ModalVideoProduto > div > div > div:nth-child(3) > div > button").click()

        time.sleep(2)
        driver.execute_script("window.history.go(-1)")
    time.sleep(2)         
    driver.execute_script("window.history.go(-1)")
    time.sleep(2) 
    
time.sleep(5)  




def rename_file_and_move(data):
    if not os.path.isdir(f'./img/{data["referencia"]}'):
        os.makedirs(f'./img/{data["referencia"]}')
    
    while any([filename.endswith(".crdownload") for filename in 
            listdir("./img")]):
        time.sleep(1)
    
    acha_novo_arquivo = [f for f in listdir('./img/') if isfile(join('./img/', f))][0]
    conta_arquivos = len(listdir(f'./img/{data["referencia"]}'))
    rename(f'./img/{acha_novo_arquivo}', f'./img/{data["referencia"]}/{data["titulo"]} {conta_arquivos}.jpg')
    return None


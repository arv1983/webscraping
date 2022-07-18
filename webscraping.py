from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
from csv import DictReader, DictWriter
from os import close
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


# webdriver.ChromeOptions.experimental_options.put("download.default_directory", '/teste/imagem')
# chromePrefs.put("download.default_directory", '/teste/imagem')
options = webdriver.ChromeOptions() 
options.add_argument("download.default_directory=$PATH:/usr_teste/")

time.sleep(2)

# driver = webdriver.Chrome(chrome_options=options)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)
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
    # driver.find_element(By.XPATH, f'/html/body/div[6]/div[3]/div/div/div/div[{i + 1}]/div/div[2]/h6/a').click()
    driver.find_element(By.XPATH, f'/html/body/div[6]/div[3]/div/div/div/div[{i + 357}]/div/div[2]/h6/a').click()

    
    referencia = driver.find_element(By.XPATH, "//*[contains(text(), 'Referência')]").text
    referencia = " ".join(referencia.split()[1:])
    
    titulo = driver.find_element(By.CLASS_NAME, "page-title.text-left").text
    
    categoria = driver.find_element(By.XPATH, "//*[contains(text(), 'Categoria')]").text
    categoria = " ".join(categoria.split()[1:])
    
    marca = driver.find_element(By.XPATH, "//*[contains(text(), 'Marca')]").text
    marca = " ".join(marca.split()[1:])

    descricao = driver.find_element(By.ID, "h2tab1").text

    preco = driver.find_element(By.CLASS_NAME, "price").text

    # if(driver.find_element(By.CSS_SELECTOR, "[name*='form']")):
        
        
        # if driver.find_element(By.XPATH, "//*[contains(text(), 'Estoque disponível no momento: ')]") != 0:
        #     qtd = driver.find_element(By.XPATH, "//*[contains(text(), 'Estoque disponível no momento: ')]").text
        #     estoque = qtd.split()[4:-1][0]
        # else:

    time.sleep(2)  
    variacoes = driver.find_element(By.CSS_SELECTOR, "[name*='form']").get_attribute('outerHTML')
    soup = BeautifulSoup(variacoes, 'html.parser')
    tds = soup.find_all(name='td')    
    tds = [valor.text for valor in tds if 'Confira' not in valor.text]
    metade = int((str(len(tds) / 2)).split('.')[0])
    numero = tds[:metade]
    estoque = tds[metade:]
    estoque = dict(zip(numero, estoque))

    print(descricao)        
    print(estoque)
    print(marca)
    print(referencia)
    print(titulo)
    print(categoria)
    print(preco)
    print('+++++')








    # images = driver.find_elements(By.PARTIAL_LINK_TEXT, "Baixar sem")
    #     # PEGA IMAGEM OK
    # for k in range(len(images)):
    #     driver.find_elements(By.PARTIAL_LINK_TEXT, "Baixar sem")[k].click()
    #     time.sleep(2) 
    
    # videos = driver.find_elements(By.CSS_SELECTOR, "[title*='Assistir & Baixar Vídeo']")
    
    # for v in range(len(videos)):
    #     driver.find_elements(By.CSS_SELECTOR, "[title*='Assistir & Baixar Vídeo']")[v].click()
    #     time.sleep(2)
    #     driver.find_element(By.ID, 'botaodownvideo').click()
    #     time.sleep(2)
    #     driver.find_element(By.CSS_SELECTOR, "#ModalVideoProduto > div > div > div:nth-child(3) > div > button").click()
    #     time.sleep(2)
    #     driver.execute_script("window.history.go(-1)")
    time.sleep(2)         
    driver.execute_script("window.history.go(-1)")
    time.sleep(2) 
    
time.sleep(5)  

from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time, asyncio, os.path, re


class Category():
    async def botas(driver):
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[2]/div/div/div/div/div/input").send_keys("nome do produto")
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div/input").send_keys("bota")
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[1]/li[2]/p").click()
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[2]/li[1]/p").click()
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[3]/li[2]/p").click()
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/button").click()
        time.sleep(3) 
        return None

    async def tenis(driver):
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[2]/div/div/div/div/div/input").send_keys("nome do produto")
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div/input").send_keys("tênis")
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[1]/li[2]/p").click()
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[2]/li[2]/p").click()
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/button").click()
        time.sleep(3) 
        return None

    async def sandalia(driver):
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[2]/div/div/div/div/div/input").send_keys("nome do produto")
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div/input").send_keys("sandália")
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[1]/li[2]/p").click()
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[2]/li[6]/p").click()
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[3]/li[1]/p").click()
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/button").click()
        time.sleep(3) 
        return None

    async def bolsa(driver):
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[2]/div/div/div/div/div/input").send_keys("nome do produto")
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div/input").send_keys("bolsa")
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[1]/li[2]/p").click()
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[2]/li[6]/p").click()
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/button").click()
        time.sleep(3) 
        return None

    async def scarpin(driver):
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[2]/div/div/div/div/div/input").send_keys("nome do produto")
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div/input").send_keys("sapato")
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[1]/li[2]/p").click()
        time.sleep(1)   
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[2]/li[4]/p").click()
        time.sleep(1)   
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/button").click()
        time.sleep(3) 
        return None

    async def meiapata(driver):
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[2]/div/div/div/div/div/input").send_keys("nome do produto")
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div/input").send_keys("sapato")
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[1]/li[2]/p").click()
        time.sleep(1)   
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[2]/li[4]/p").click()
        time.sleep(1)   
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/button").click()
        time.sleep(3) 
        return None   


    async def rasteira(driver):
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[2]/div/div/div/div/div/input").send_keys("nome do produto")
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div/input").send_keys("sapato")
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[1]/li[2]/p").click()
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[2]/li[6]/p").click()
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[2]/li[6]/p").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[3]/li[5]/p").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/button").click()
        time.sleep(3) 
        return None  

    async def peeptoe(driver):
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[2]/div/div/div/div/div/input").send_keys("nome do produto")
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div/input").send_keys("bota")
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[1]/li[2]/p").click()
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[2]/li[1]/p").click()
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[3]/li[2]/p").click()
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/button").click()
        time.sleep(3) 
        return None        

    async def anabela(driver):
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[2]/div/div/div/div/div/input").send_keys("nome do produto")
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div/input").send_keys("bota")
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[1]/li[2]/p").click()
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/ul[2]/li[4]/p").click()
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/button").click()
        time.sleep(3) 
        return None                


        
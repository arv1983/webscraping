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

def f(x):
    match x:
        case 'a':
            return 1
        case 'b':
            return 2
        case _:
            return 0 


print(f('a'))
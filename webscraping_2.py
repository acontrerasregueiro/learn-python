from selenium import webdriver
from bs4 import BeautifulSoup
import time
options = webdriver.ChromeOptions()

wd = webdriver.Edge()
busqueda = 'cerveza turia'

#wd.get("https://www.carrefour.es/?q="+busqueda.replace(" ","+"))
wd.get("https://www.carrefour.es/?q=cerveza+turia")

soup = BeautifulSoup(wd.page_source,'lxml')
time.sleep(20)

for elemento in soup.find_all('h1',{"class":"ebx-result-title ebx-result__title"}):
    print(elemento.contents[0])
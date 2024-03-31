from selenium import webdriver
from bs4 import BeautifulSoup
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome()
#busqueda = 'cerveza turia'
wd.get("https://www.carrefour.es/?q=cerveza+turia")

soup = BeautifulSoup(wd.page_source,'html.parser')
print(soup.find_all('div',{'class':"ebx-result-title ebx-result__title"}))
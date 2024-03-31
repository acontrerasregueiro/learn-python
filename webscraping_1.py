#Video Deusto https://vimeo.com/571136282/8f3d3238b8
#Ejemplo de webscraping Selenium y BeatifullSoup

import requests
from bs4 import BeautifulSoup

web = requests.get("https://amazon.es")
soup = BeautifulSoup(web.text,"html")
print(soup)
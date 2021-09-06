import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.options import Options
import json

# 1. Pegar conteúdo HTML a partir da URL
url = "https://marketplace.axieinfinity.com/axie"

option = Options()
option.headless = True
#driver = webdriver.Firefox(options=option)
driver = webdriver.Firefox()

driver.get(url)
time.sleep(10)

#driver.find_element_by_xpath("span[@class='mr-24']")

#axie-card > border border-gray-3 bg-gray-4 rounded transition hover:shadow hover:border-gray-6 > px-12 py-16 > h-0 pb-24 flex flex-row flex-wrap justify-center overflow-hidden items-baseline > truncate font-medium md:text-20 md:leading-24




#driver.quit()
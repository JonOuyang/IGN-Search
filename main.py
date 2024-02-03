import random
import nltk
from nltk.corpus import words
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import TimeoutException
nltk.download('words')

word_list = words.words()
# cuts list down from 236736 -> 233080
word_list = [word for word in word_list if 3 <= len(word) <= 16]
available_list = []

driver = webdriver.Chrome()

driver.get(f'https://minecraftuuid.com/?search=Dimensionz_')
time.sleep(2)

#WARNING: Page fails after 100 rapid API calls (server side)

for ign in word_list:
    driver.get(f'https://minecraftuuid.com/?search={ign}')
    timeout = 1
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="Player-Info-Row"]/div'))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        available_list.append(ign)

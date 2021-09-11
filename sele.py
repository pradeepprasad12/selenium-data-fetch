from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import pandas as pd
import requests
#from bs4 import BeautifulSoup
from lxml import html


driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")

driver.get("https://www.google.com/")

xpath1="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"

search_bar =driver.find_element_by_xpath(xpath1)
search_bar.clear()
search_bar.send_keys("hello world")
search_bar.send_keys(Keys.RETURN)

# fetch the url
url= driver.current_url
# making requests instance
reqs = requests.get(url)
tree = html.fromstring(reqs.content)  
  
# Get element using XPath
title = tree.xpath('/html/head/title/text()')
print(title)
# save the data in CSV file
col=[title,url]
df = pd.DataFrame(col)
df.to_csv('title_url.csv',mode='w',header = False)

# close the program
driver.quit()
  







from selenium import webdriver
from selenium.webdriver.common.by import By


from bs4 import BeautifulSoup

import time
import pandas as pd
data = pd.DataFrame({'Productname':[''],'Price':['']})
driver = webdriver.Chrome()
driver.get('https://www.hoojan.com/fr/boutiques-officielles/vetements-et-accessoires/nike.html')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    try:
        driver.find_element(By.CLASS_NAME, 'ias-noneleft')
        print('done')
        break
    except:
        pass
    
soup=BeautifulSoup(driver.page_source,'lxml')
postings = soup.find_all('div',class_='details-area')  

for post in postings:       
            post_data = post.find('a')
            product_name = post_data.find('h3',class_="product-name").text
            price = post_data.find('span',class_='price').text
            pricee = price.strip()
            data=data._append({'Productname':product_name,'Price':pricee},ignore_index = True)
       
data.to_csv('C:/Users/hp/Desktop/Python web-scraping project/course/Nike.csv')
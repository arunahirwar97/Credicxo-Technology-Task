from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")

title=[] #List to store title of the product
price =[] #List to store price of the product
status=[] #List to store status of the product
mfd=[] #List to store Manufactured of the product
driver.get("https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1")
content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('div',href=False, attrs={'class':'product-description'}):
    name=a.find('a', attrs={'class':'catalog-item-name'})
    title.append(name.text)


for a in soup.findAll('div',href=False, attrs={'class':'catalog-item-price'}):
    name=a.find('span', attrs={'class':'price'})
    price.append(name.text)
    
for a in soup.findAll('span',href=False, attrs={'class':'status'}):
    name=a.find('span')
    status.append(name.text)

    
final_status = []
for i in status:
    if i == 'Out of Stock':
        final_status.append('false')
    elif i == 'In Stock':
        final_status.append('true')

for a in soup.findAll('a',href=True, attrs={'class':'catalog-item-brand'}):
    name=a.find()
    mfd.append(a.text)

title = pd.DataFrame(title)
price = pd.DataFrame(price)
final_status = pd.DataFrame(final_status)
mfd = pd.DataFrame(mfd)

title.columns = ['title']
price.columns = ['price']
final_status.columns = ['stock']
mfd.columns = ['maftr']

data = [title,price,final_status,mfd]
main_data = pd.concat(data,axis=1)
main_data.T.to_json('output.json')
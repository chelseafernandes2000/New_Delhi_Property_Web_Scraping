#!/usr/bin/env python
# coding: utf-8

# In[84]:


import requests
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import pandas as pd


# In[50]:


link="https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import SessionNotCreatedException

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(link)
initial_value=0
next_value=500
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
while next_value<30000:
    driver.execute_script("window.scrollTo({},{});".format(initial_value, next_value))
  
    initial_value=next_value
    next_value+=300


# In[51]:


html = driver.page_source
soup = BeautifulSoup(html)
driver.close()


# In[93]:


df = pd.DataFrame()
  


# In[94]:


for k in soup.find_all("div", class_="filter-property-list detailurl"):
    title=k.find("h1", class_="filter-pro-heading").text.split("  ")[0]
    address=k.find("h1", class_="filter-pro-heading").text.split("  ")[1]
    price=k.find("span", class_="price").text
    image=k.find("img")['src']
    area=k.find("div", class_="col-4").text.replace("Area","")
    facing=k.find("div", class_="col-sm-7").find("div", class_="col-3").text.replace("Facing","")
    status=k.find("div", class_="col-sm-7").find("div", class_="col-5").text.replace("Status","")
    contact_name=k.find("div", class_="contact-details").text.split("\n")[1]
    posted=k.find("div", class_="contact-details").text.split("\n")[2].replace("Posted:  ","")
    
    df2 = {'Title': title, 'Address': address, "Price": price, "Area":area, "Facing":facing, 
          'Status':status, "Contact_Name": contact_name, "Posted": posted, "Image":image}
    df = df.append(df2, ignore_index = True)
    
    


# In[95]:


print(df)


# In[96]:


df.to_excel("2BHK_Property_Output.xlsx")


# ### For 3 BHK

# In[113]:


link="https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import SessionNotCreatedException
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(link)

bhkbutton=driver.find_element_by_xpath("//a[@id='navbarDropdownMenuLink' and text()='BHK']").click()

checkboxElement = driver.find_element_by_xpath("//input[@id='2']")
driver.execute_script("arguments[0].click();", checkboxElement)

reqcheckboxElement = driver.find_element_by_xpath("//input[@id='3']")
driver.execute_script("arguments[0].click();", reqcheckboxElement)

initial_value=0
next_value=500
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
while next_value<30000:
    driver.execute_script("window.scrollTo({},{});".format(initial_value, next_value))
  
    initial_value=next_value
    next_value+=300


# In[114]:


newhtml = driver.page_source
newsoup = BeautifulSoup(newhtml)
driver.close()


# In[115]:


newdf = pd.DataFrame()
for k in newsoup.find_all("div", class_="filter-property-list detailurl"):
    title=k.find("h1", class_="filter-pro-heading").text.split("  ")[0]
    address=k.find("h1", class_="filter-pro-heading").text.split("  ")[1]
    price=k.find("span", class_="price").text
    image=k.find("img")['src']
    area=k.find("div", class_="col-4").text.replace("Area","")
    facing=k.find("div", class_="col-sm-7").find("div", class_="col-3").text.replace("Facing","")
    status=k.find("div", class_="col-sm-7").find("div", class_="col-5").text.replace("Status","")
    contact_name=k.find("div", class_="contact-details").text.split("\n")[1]
    posted=k.find("div", class_="contact-details").text.split("\n")[2].replace("Posted:  ","")
    
    df2 = {'Title': title, 'Address': address, "Price": price, "Area":area, "Facing":facing, 
          'Status':status, "Contact_Name": contact_name, "Posted": posted, "Image":image}
    newdf = newdf.append(df2, ignore_index = True)
print(newdf)


# In[116]:


newdf.to_excel("3BHK_Property_Output.xlsx")


# In[ ]:





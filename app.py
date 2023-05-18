from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time 
import csv

browser = webdriver.Chrome("chromedriver.exe")
start = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs#Field_brown_dwarfs"
browser.get(start)
time.sleep(10)

def scrap():
    header = ['Name','Distance','Mass','Radius']
    sun = []
    name = []
    distance = []
    mass = []
    temp_list = []
    rad = []
    time.sleep(1)
    soup = BeautifulSoup(browser.page_source,'html.parser')
    star_table = soup.find_all('table')
    table_rows =  star_table[7].find_all("tr")
    for tr in table_rows:
        td = tr.find_all("td")
        row = [i.text.rstrip() for i in td]
        temp_list.append(row)
        for i in range(1,len(temp_list)):
            name.append(temp_list[i][0])
            distance.append(temp_list[i][5])
            mass.append(temp_list[i][7])
            rad.append(temp_list[i][8])
    
    df2 = pd.DataFrame(list(zip(name,distance,mass,rad)),columns=['name','distance','mass','radius']) 
    
    df2.to_csv('brown_dwarf.csv')

scrap()
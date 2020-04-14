import requests
from bs4 import BeautifulSoup
import xlrd
import lxml
from googlesearch import search
import time

Exelfile = xlrd.open_workbook(r'C:\Users\Daniel\Desktop\Virus_Archive\Dorker\Dorks.xlsx') # Excel path
sheet = Exelfile.sheet_by_index(0)
website = input("Type in the website name: ")

my_results_list = []

for x in range(sheet.nrows): 
    test = sheet.cell_value(x, 2) + " site:" + website
    for i in search(test, tld = 'com', num = 2, start = 0, stop = 3, pause = 2.0):
        my_results_list.append(i)
        if len(my_results_list) > 0:
            print ("Dork found: " + sheet.cell_value(x, 2) + " | " + sheet.cell_value(x, 3) + " | By: " + sheet.cell_value(x, 4))
        time.sleep(5)
    my_results_list.clear()
    time.sleep(5)

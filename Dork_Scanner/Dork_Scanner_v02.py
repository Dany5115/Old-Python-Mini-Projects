import requests
from bs4 import BeautifulSoup
import xlrd
import lxml
from googlesearch import search
import time


Excelfile = xlrd.open_workbook(r'C:\Users\Daniel\Desktop\Virus_Archive\Dorker\Dorker_v01\Dorks.xlsx') # Excel path
sheet = Excelfile.sheet_by_index(0)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

website = input("Type in website to scan for dorks: ")

for x in range(sheet.nrows):
    try:
        URL = "https://www.google.com/search?q=" + sheet.cell_value(x, 2) + " site:" + website
        result = requests.get(URL, headers=headers)
        soup = BeautifulSoup(result.content, 'html.parser')
        total_results_text = soup.find("div", {"id": "result-stats"}).find(text=True, recursive=False) # this will give you the outer text.
        results_num = ''.join([num for num in total_results_text if num.isdigit()]) # now will clean it up and remove all the characters that are not a number.
        if int(results_num) > 0:
            print ("Vulnerable!: " + sheet.cell_value(x, 2) + " | " + sheet.cell_value(x, 3) + " | By: " + sheet.cell_value(x, 4))
        time.sleep(10)
        
    except:
        print ("Invulnerable: " + sheet.cell_value(x, 2) + " | " + sheet.cell_value(x, 3) + " | By: " + sheet.cell_value(x, 4))
        time.sleep(11)

print("Scan Complete!") # After the scan

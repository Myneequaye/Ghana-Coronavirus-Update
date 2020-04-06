from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
import sqlite3


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://ghanahealthservice.org/covid19/'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup.findAll('p',attrs = {'class':'information-line-text'})

arr = []
for tag in tags:
    arr.append(tag.text)
    

confirmed = int(arr[0]) + int(arr[6]) + int(arr[12])
recovered = int(arr[1]) + int(arr[7]) + int(arr[13])
discharged = int(arr[2]) + int(arr[8])
responding = int(arr[3]) + int(arr[9]) + int(arr[14])
condition = int(arr[4]) + int(arr[10]) + int(arr[15])
deaths = int(arr[5]) + int(arr[11]) + int(arr[16])

print(f"""
Ghana's Situation
Routine Surveillance

Confirmed: {confirmed}
Recovered: {recovered}
Discharged(Home Mgt.): {discharged}
Well/Responding to Treatment: {responding}
Critical Condition: {condition}
Deaths: {deaths}
 """)    







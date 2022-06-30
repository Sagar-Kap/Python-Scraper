import webbrowser
import csv
import time
import random
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import os
import csv
import pandas as pd

Notino_dic= {"RMN02460" : "F5000","RMN02459": "F4000","RMN02458": "F3000","RMN02449":"CI5519","RMN02461":"PG3000","RMN02457":"F0050","RMN02456" : "EP7300","RMN02124" :  "S3580", "RMN1720" : "S8590", "RMN02365" : "S6500", "RMN1719" :  "S8500", "RMN01922" : "S8540", "RMN02374" : "CI96W1", "RMN1860" :  "D5219", "RMN1715" :  "CI95", "RMN1857" :  "S9600", "VZR10901" :  "B95P", "RMN1739" :  "KF40E", "RMN01934" : "NE3850", "RMN01965" : "FC500", "RMN02376" : "D1500", "RMN1866" : "AC8002", "RMN01937" : "CI91X1", "RMN02351" : "S8550", "RMN02401" :   "CI5408" , "RMN1714" :   "AS7051", "RMN1716" :   "S3500", "RMN1717" :   "S5505", "RMN1758" :   "MB4120", "RMN1767" :   "S6300", "RMN1757" :   "CI9532", "RMN1859" :   "S6505", "RMN1861" :   "H5670", "RMN01939" :   "AC9140", "RMN01938" :   "S9100", "RMN02371" :   "MB4130", "RMN02373" :   "PG6045", "RMN02441" :   "CI5700", "RMN02444" :   "MB4110", "RMN1721" :   "D3010", "RMN1718" :   "S5525", "RMN1712" :   "D5000", "RMN1711" :   "D3015", "RMN1768" :   "S7300", "RMN1759" :   "BKT4000", "RMN1849" :   "HC5035", "RMN1858" :   "S9500", "RMN1862" :   "CB7400", "RMN01916" :   "MB6850", "RMN01936" :   "CI9132", "RMN01935" :   "CI5318", "RMN02122" :   "HF9000", "RMN02123" :   "EP7070", "RMN02349" :   "EP7500", "RMN02375" :   "AC9096", "RMN02350" :   "S7350", "RMN02397" :   "S6606", "RMN02402" :   "D5408" , "RMN02403" :   "S5408", "RMN02404" :   "HC7110", "RMN02408" :   "HC450", "RMN02413" :   "PR1350", "RMN02409" :   "MB4000", "RMN02412" :   "PG2000", "RMN02411" :   "MB4050", "RMN02410" :   "MB5000", "RMN02405" :   "HC5018", "RMN02406" :   "HC7130", "RMN02407" :   "HC363C", "RMN02442" :   "AC5700", "RMN02450" :   "MB4046" , "RMN02454" :   "EC9001", "RMN02453" :   "S9001", "RMN02452" :   "CI91AW" , "RMN1743" :   "CI63E1", "RMN1744" :   "CI5319", "RMN01920" :   "MB050", "RMN01983" :   "PG6150", "RMN01985" :   "IPL6750", "RMN02021" :   "HC5100", "RMN02125" :   "MPT3900", "RMN02372" :  "NE3455", "RMN02445" : "PG4000", "RMN02447" : "CI5538", "RMN02448" : "CI6525", "RMN02446" : "EP7700"}

filename= "noti.csv"
f= open(filename, "w")
headers= "Model, Price\n"
f.write(headers)

enigma=1  #Notino

def Notino_Loop():
    url= "https://www.notino.bg/remington/?f="+str(enigma)+"-1-17015" # enigma= 1 for starting page, ends to 4 hence 4 iterations 
    
    request = uReq(url)
    page= request.read()
    soupa = soup(page, "html.parser")  # turned page into soup
    containers = soupa.findAll("li", {"class": "item"})
    request.close()
    print(len(containers))
    for dabba in containers:
        try:

            tag= dabba.a["href"]
            next_page_url = ("https://www.notino.bg"+str(tag))
            name_request= uReq(next_page_url)
            name_page_read = name_request.read()
            name_request.close()
            page_soupa= soup(name_page_read, "html.parser")
            num=page_soupa.find("span", {"class" : "styled__CodeBlock-mu8uqe-1 kNrous"})
            numfu= num.get_text()
            model= numfu.replace("Код: ","")
            try:
                modelo= Notino_dic[model]
                f.write(modelo)
                print(modelo)

            except:

                real_name = page_soupa.find("span", {"class" : "styled__Span-sc-3sotvb-6 eboaty"})
                RealName = real_name.get_text()
                print(RealName)
                f.write(RealName)

            suki= dabba.find("p", {"class": "price"})
            hate= suki.get_text()
            hatred= hate.replace("," , ".")
            price= hatred.replace("\xa0лв." , "")      #price
            print(price+"\n")


            f.write("," + price + "\n")
            
        except:
            f.write(","+ str(0) +"\n")
            print("Out\n")
            print(numfu)
            continue    

def Notino():
    
    global enigma
    while enigma <= 4:
        
        Notino_Loop()
        enigma+=1
        n= random.randint(10,20)
        time.sleep(n)

    

###############################################NOTINO##########################################################################

Notino()
f.close()
webbrowser.open("https://youtu.be/dQw4w9WgXcQ", new=2)

df = pd.read_csv("noti.csv")
fd = df.drop_duplicates()
fd = fd.reset_index(drop= True)
fd.to_csv("notino.csv", index = False)
os.remove("noti.csv")



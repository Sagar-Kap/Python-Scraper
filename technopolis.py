import csv
import time
import random
import bs4
import webbrowser
from urllib.request import urlopen as uReq
import requests
from bs4 import BeautifulSoup as soup 

Technopolis_dic = {"830715": "D3195GP","830547":"PG6030","830714":"S9001","830495":"HC4000","830494":"HC3000","830496":"PG9100","830709":"CI5901","830708":"D5901","830706":"AC7200","830493":"MB3000","830712":"MB320C","830499":"HG5000","830498":"HG3000","830497":"HG1000","830713":"S8670", "830710":"S7970", "830707":"S5901", "830593":"D8700","830711": "XR1500", "830469":"CB7400","830514"	:"S9600","830463" :  "S7412","830451" :  "S9100","830466" :  "S8598","830473" :  "S3580","830474" :  "S8605","830478" :  "S9700","830479" :  "S6606","830491" :  "S3505GP","830492" :  "S5408","830573" :  "S6505","830471" :  "NE3870","830520" :  "NE3150","830464" :  "MB050","830484" :  "PG3000","830485" :  "PG4000","830486" :  "PG5000","830489" :  "PG2000","830490" :  "PG6000","830452" :  "CR4000","830579" :  "FC1000","830455" :  "SP-BB1","830588" :  "RS401","830456" :  "SP-BB2","830591" :  "HC5035","830559" :  "D3015","830560" :  "D5220","830569" :  "AC5999","830450" :  "AC9140","830475" :  "AC8605","830476" :  "AC6330","830480" :  "D5706","830481" :  "CI5538","830488" :  "CI5408","830487" :  "MB4128","830470" :  "HC7130","830482" :  "HC9100","830562" :  "CI96W1","830472" :  "CI83V6", "830469":"CB7400", "830590":"HC5018"}


filename= "technopolis.csv"
f= open(filename, "w")
headers= "Model, Price\n"
f.write(headers)

url = "https://www.technopolis.bg/en/search/?pricerange=&pageselect=90&page=0&q=remington:relevance&text=remington&layout=List"
#request= uReq(url)
#reader = request.read()
request = requests.get(url)

soupa = soup(request.text, "html.parser")
mo = soupa.find("div", {"class" : "products-list"})
list_item = mo.findAll("li", {"class": "list-item"})
request.close()
for item in list_item:
	try:
		num = item.find("span", {"class": "item-number"})
		number = num.get_text()
		numfu = number.replace("Code: ", "")	
		try:
			model_number= Technopolis_dic[numfu]
			f.write(model_number)
			print(model_number)
		except:
			f.write("New model")
			print("New model " + number)
			continue		

		p = item.find("span", {"class":"price-value"})
		print(p)
		price= p.get_text()
		print(price+"\n")
		f.write(","+price+"\n")

	except:
		try:
			n=item.findAll("span", {"class":"price-value"})
			inf= n[1]
			price=inf.get_text()
			print(price)
			f.write(","+price+"\n")
		except:
			print("there is a new item")
			f.write("There is a problem"+"\n")
			continue

		continue



webbrowser.open("https://youtu.be/dQw4w9WgXcQ", new=2)



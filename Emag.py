import os
import csv
import requests 
from bs4 import BeautifulSoup as soup
from time import sleep
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')

PATH = "C:\Program Files (x86)\chromedriver.exe"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}

emag_dic = {"Преса за коса Remington PRO-Sleek & Curl S6505" :	"S6505",
"Преса за коса Remington Keratin Therapy Pro S8590"	: "S8590",
"Преса за коса Remington S9600"	: "S9600",
"Преса за коса Remington S8540 Keratin Protect"	: "S8540",
"Преса за изправяне Remington PROluxe S9100" : 	"S9100",
"Преса за коса Remington Keratin Protect S8598"	: "S8598",
"Преса за коса Remington S6500" :	"S6500",
"Комплект за изправяне на косата Remington PRO-Ceramic Titanium S5506GP" : "S5506GP",
"Преса за коса Remington S9500"	: "S9500",
"Преса Remington Curl & Confidence 2 в 1 S6606" :	"S6606",
"Преса за коса Remington S8901 HYDRAluxe"	: "S8901",
"Преса за обем и вафлички Remington S3580 Ceramic Crimp" :	"S3580",
"Преса за коса Remington PRO-Ceramic Extra S5525"	: "S5525",
"Преса за коса Remington Shine Therapy S8500"	: "S8500",
"Преса за коса Remington S9505 Rose Luxe"	: "S9505",
"Преса за коса REMINGTON S3500"	: "S3500",
"Преса за коса Remington PRO-Ceramic Ultra S5505" :	"S5505",
"Преса за коса Remington S1A100"	: "S1A100",
"Подаръчен комплект преса за коса Remington S3505GP" :	"S3505GP",
"Сешоар Remington D3190" :	"D3190",
"Преса за коса Remington S8605 Advanced Colour Protect" :	"S8605",
"Преса за коса Remington RE-2084"	: "S2084",
"Преса за коса Remington S9100B Proluxe Midnight Edition"	: "S9100B",
"Маша за коса Remington Ci5408 Mineral Glow"	: "CI5408",
"Преса за коса Remington S5700"	: "S5700",
"Преса за коса Remington S6300" :	"S6300",
"Маша за коса Remington Ci9532"	: "CI9532",
"Сешоар Remington D5220" :	"D5220",
"Сешоар Remington Power Volume D3015" :	"D3015",
"Тример за тяло Remington BHT250"	: "BHT250",
"Преса за коса Remington Ultimate Glide S9700" :	"S9700",
"Машинка за подстригване Remington HC5200 ProPower"	: "HC5200",
"Маша Remington Ci95"	: "CI95",
"Четка за коса Remington Keratin Therapy Volume & Protect AS8090"	: "AS8090",
"Сешоар Remington Your Style D5219"	: "D5219",
"Маша за коса Remington Keratin Protect CI83V6" :	"CI83V6",
"Машинка за подстригване Remington HC5150 Alpha" : "HC5150",
"Сешоар Remington d3010" :	"D3010",
"Четка за изправяне на коса Remington CB7400" :	"CB7400",
"Комплект Remington Groom Kit PG6130"	: "PG6130",
"Маша за коса Remington S8670"	: "S8670",
"Машинка за подстригване Remington HC5810"	: "HC5810",
"Сешоар Remington D5715 E51"	: "D5715",
"Преса за коса Remington S1510" :	"S1510",
"Машинка за подстригване Remington MB320C"	: "MB320C",
"Сешоар Remington D5210" :	"D5210",
"Tример за нос и уши Remington NE3150"	: "NE3150",
"Маша за коса Remington Ci96W1" :	"CI96W1",
"Маша за коса Remington Pro Soft Curl CI6525" :	"CI6525",
"Тример за тяло Remington Bodyguard BHT2000A" :	"BHT2000A",
"Сешоар Remington PROluxe AC9140"	: "AC9140",
"Сешоар Remington Thermacare Pro 2200 D5710" :	"D5710",
"Сешоар Remington AC5999"	: "AC5999",
"Четка за изправяне на коса Remington Volume & Straight CB7A138" :	"CB7A138",
"Преса за коса Remington Wet2Straight S7300" : "S7300",
"Машинка за подстригване Remington HC5035":	"HC5035",
"Маша за коса Remington CI86X8 Advanced Coconut Therapy 25-28mm Wand" :	"CI86X8",
"Преса за коса Remington S1400 Straightener 210 за изправяне"	: "S1400",
"Сешоар Remington AC5700 Copper Radiance"	: "AC5700",
"Комбиниран тример Remington PG2000 G2 Graphite" :	"PG2000",
"Маша за коса Remington PROluxe CI9132"	: "CI9132",
"Тример Remington PG4000 Graphite Series G4" :	"PG4000",
"Сешоар Remington Shine Therapy D5216"	: "D5216",
"Сешоар Remington Pro-Air Turbo D5226"	:"D5226",
"Тример за лице Remington MB4045" :	"MB4045",
"Сешоар за коса Remington AC5911"	: "AC5911",
"Електрическа самобръсначка Remington R3000 Style Series R3" :	"R3000",
"Самобръсначка Remington Style Series F5 F5000"	: "F5000",
"Тример за брада Remington MB4000 Style Series B4" :	"MB4000",
"Самобръсначка Remington Ultimate Series F9 XF9000"	 : "XF9000",
"Машинка за подстригване Remington HC363C"	: "HC363C",
"Комбиниран тример Remington PG5000 G5 Graphite" :	"PG5000",
"Преса за коса Remington Air Plates S2412"	: "S2412",
"Преса за коса Remington S1450"	: "S1450",
"Преса за коса Remington S5408 Mineral Glow" : "S5408",
"Преса за коса Remington Air Plates S7412" :	"S7412",
"Маша за коса Remington Ci5408 Mineral Glow"	: "CI5408",
"Преса за коса Remington S6755 Sleek & Curl Manchester United Edition"	: "S6755",
"Преса за коса Remington Straightini S2880" :	"S2880",
"Комплект Преса за коса 215 градуса + Сешоар Remington 2000W D3012GP"	: "D3012GP",
"Преса за коса Remington Wet2Straight S7350"	: "S7350",
"Преса за коса Remington S3500 E51"	: "S3500",
"Преса за коса Remington S7710"	: "S7710",
"Тример за лице Remington Endurance MB4200"	: "MB4200",
"Машинка за подстригване Remington HC7110 Pro Power Precision Steel"	: "HC7110",
"Тример за тяло Remington FLEX BHT100"	: "BHT100",
"Комплект за постригване Remington PG6030"  : "PG6030",
"Електрическа Четка за почистване на лице Remington Reveal FC250" :	"FC250",
"Самобръсначка Remington Titanium-X F7800"	: "F7800",
"Електрическа самобръсначка Remington R3 Style"	: "R3000",
"Електрическа четка за коса Remington Airstyler Amaze AS1220"	: "AS1220",
"Сешоар Remington AC9140B OPTIheat Proluxe Midnight Edition"	: "AC9140B",
"Електрическа четка за коса REMINGTON Keratin Protect CB8338"	: "CB8338",
"Маша за коса Remington CI91W1B Proluxe Midnight Edition"	: "CI91W1B",
"Сешоар Remington D7779 Air3D"	: "D7779",
"Тример за нос и уши Remington Nano Series Lithium NE3870"	: "NE3870",
"Машинка за подстригване Remington Pro Power Titanium HC7130"	: "HC7130",
"Тример за лице Remington MB4850" :	"MB4850",
"Машинка за подстригване Remington HC5018 Apprentice" :	"HC5018",
"Дамска електрическа самобръсначка Remington WSF4810" :	"WSF4810",
"Машинка за подстригване Remington Heritage HC9100" :	"HC9100",
"Маша за коса Remington Pro Spiral Curl CI5519" :	"CI5519",
"Електрическа четка за коса Remington AS7051" :	"AS7051",
"Сешоар Remington D5720" :	"D5720",
"Мини самобръсначка Remington R95" :	"R95",
"Тример за лице Remington MB4110" :	"MB4110",
"Самобръсначка Remington Heritage HF9000" :	"HF9000",
"Тример Remington Smooth & Silky Cordless BKT4000" :	"BKT4000",
"Маша за коса Remington CI8605" :	"CI8605",
"Машинка за подстригване Remington My Groom HC5100" :	"HC5100",
"Самобръсначка Remington XF8505" :	"XF8505",
"Козметичен тример + Пинсети Remington Reveal MPT4000C" :	"MPT4000C",
"Машинка за подстригване Remington QuickCut HC4250" :	"HC4250",
"Комбиниран тример Remington PG6030" :	"PG6030",
"Тример за брада Remington MB055 Durablade Manchester United" :	"MB055",
"Машинка за подстригване Remington Virtually Indestructible HC5880" :	"HC5880",
"Машинка за подстригване Remington Graphite G2" :	"PG2000",
"Четка с топъл въздух Remington Style & Curl AS404" :	"AS404",
"Сешоар Remington D5215" :	"D5215",
"Тример за брада B3 Style" :	"MB3000",
"Маша за коса Remington CI1A119" :	"CI1A119",
"Сешоар Remington PRO Air Power AC6330" :	"AC6330",
"Сешоар Remington PRO АC5913W" :	"AC591W",
"Въртяща се четка Remington AS8090" :	"AS8090",
"Четка за лице за мъже Remington Recharge FC2000" :	"FC2000",
"Почистваща четка Remington SP-FC11" :	"SPFC11",
"Тример за брада Remington The Crafter MB4050" :	"MB4050",
"Сешоар Remington PRO-Air Light 2200 AC6120" :	"AC6120",
"Уред за почистване на лице Remington Reveal FC500" :	"FC500",
"Самобръсначка Remington MyGroom R0050" :	"R0050",
"Електрическа самобръсначка Remington MS5120 Titanium" :	"MS5120",
"Самобръсначка Remington HyperFlex Aqua XR1430" :	"XR1430",
"Конусовидна маша за коса Remington Ci52W0 Shine Therapy" :	"CI52W0",
"Електрическа самобръсначка Remington F3805" :	"F3805",
"Електрическа самобръсначка Remington PF7600 Comfort" :	"PF7600",
"Самобръсначка XR1350" : "XR1350",
"Сешоар Remington PROtect D8700" :	"D8700",
"Самобръсначка Remington HyperFlex Golfer XR1340G"      :	"XR1340G",
"Автоматична маша за коса Remington Keratin Protect CI8019" :	"CI8019",
"Маша за коса Remington PROtect Ci8725" :	"CI8725",
"Машинка за подстригване Remington HC335" :	"HC335",
"Сешоар Remington D6090" :	"D6090",
"Електрическа самобръсначка Remington XR1550" :	"XR1550",
"Самобръсначка Remington R4000 Power Series Aqua Manchester United Edition" :	"R4000",
"Сaмобръснaчкa Remington HyperFlex Wet & Dry XR1470" :	"XR1470",
"Самобръсначка Remington Power Advanced F9200" :	"F9200",
"Remington CB4N 620792"	: "CB4N",
"Сешоар Remington AC3300" :	"AC3300",
"Подаръчен комплект лимитирана серия с тример за брада Beard Boss Remington MB4122" :	"MB4122",
"Тример за брада Remington Beard Boss MB4120" :	"MB4120",
"Четка Remington Shine Therapy Paddle Brush B80P" :	"B80P",
"Самобръсначка Remington DuraBlade Pro" :	"MB050",
"Сешоар Remington Keratin Protect AC8002" :	"AC8002",
"Сгъваем Сешоар Remington D1500" :	"D1500",
"Ротационна четка Remington Keratin Protect AS8810" :	"AS8810",
"Тример за лице Remington MB350L" :	"MB350L",
"Тример за брада Remington Beard Boss Styler MB4125" :	"MB4125",
"Ретро преса Remington CI91AW" : "CI91AW",
"Маша за коса Remington CI5700": "CI5700",
"Комплект машинка за подстригване и приставка Remington Pro Power Titanium Ultra HC7170" : "HC7170",
"Тример за брада Remington MB4128 Manchester United" : "MB4128",
"Сешоар Remington D3080" : "D3080",
"Маша за коса Remington Ci6325" : "CI6325",
"Самобръсначка Remington Ultimate Series R9 XR1570" : "XR1570",
"Електрическа самобръсначка Remington Style Series F3 F3000" : "F3000",
"Електрическа четка за коса Remington Dry & Style AS800" : "AS800",
"Апарат за бръснене Remington Power Flex PR1330" : "PR1330",
"Тример Remington BHT2000" : "BHT2000",
"Сешоар за коса Remington D2121" : "D2121",
"Сешоар Remington D5755 Thermacare Manchester United" : "D5755",
"Сешоар Remington AC9007" : "AC9007",
"Маша за коса Remington Keratin Protect CI5318" : "CI5318",
"Самобръсначка Remington Power Series Aqua Pro PR1370" : "PR1370",
"Машина за микродермабразио Remington REVEAL MD3000" : "MD3000",
"Маша за коса Remington Dual Curl Ci63E1" : "CI63E1",
"Самобръсначка Remington HF9050 Heritage Manchester Edition" : "HF9050",
"Тример за нос и уши Remington Nano NE3455" : "NE3455",
"Сешоар Remington D2400" : "D2400",
"Сешоар Remington D5408 Mineral Glow" : "D5408",
"Тример Remington Pilot PG180"	: "PG180",
"Сешоар Remington Pro Air Ionic D4200"	: "D4200",
"Самобръсначка Remington XF8705"	: "XF8705",
"Самобръсначка Remington XR1450"	: "XR1450",
"Машинка за подстригване Remington Pro Power Alpha HC5155" :	"HC5155",
"Конична маша за коса Remington Ci53W Shine Therapy"	: "CI53W",
"Тример за нос и уши Remington Nano Series NE3850"	: "NE3850",
"Самобръсначка и тример за брада Remington DuraBlade MB050"	: "MB050",
"Четка за лице Remington Reveal FC1000"	: "FC1000",
"Сешоар Remington D5706 CURL and STRAIGHT CONFIDENCE" : "D5706",
"Сешоар Remington On The Go D1500" : "D1500",
"Маша за коса Remington PROluxe CI91X1" :	"C191X1",
"Самобръсначка Remington LiftLogic Smart Edge XF8500" :	"XF8500",
"Електрическа четка за изправяне на коса Remington Keratin Protect CB7480" :	"CB7480",
"Сешоар Remington Pro Air Dry D5950" :	"D5950",
"Машинка за подстригване Remington Heritage Manchester United Edition HC9105"	: "HC9105",
"Сешоар Remington Keratin Protect AC8820" :	"AC8820",
"Сешоар Remington Pro 2100 D5017"	: "D5017",
"Сешоар Remington D5408 Mineral Glow" :	"D5408",
"Сешоар Remington AC8901 HYDRAluxe"	: "AC8901",
"Машинка за подстригване Remington Pro Power Titanium Plus HC7150" :	"HC7150",
"Машинка за подстригване Remington ColourCut HC503"	: "HC5038",
"Маша за коса Remington Ci5538"	: "CI5538",
"Маша за коса Remington Pearl Rose CI9525"	: "CI9525",
"Маша Remington Ci5319"	: "CI5319",
"Почистваща четка Remington SP-FC10"	: "SPFC10",
"Резервни филтри за уред за микродермоабразио Remington MD3000"	: "SPMD3000",
"Маша за коса Remington Ci89H1 HYDRAluxe"	: "CI89H1",
"Резервна ексфолираща четка за лице Remington"	: "SPFC3",
"Резервна масажираща четка за лице Remington"	: "SPFC4",
"Резервни ролки за автоматична пила Remington CR4000 Reveal"	: "CR4000",
"Сешоар Remington AC8605"	: "AC8605",
"Резервна ексфолираща четка SP-BB1 за уред Reveal" :	"SPBB1",
"Сешоар Remington AC9096"	: "AC9096",
"Сешоар Remington D5000"	: "D5000",
"Самобръсначка Remington XR1470"	: "XR1470",
"Маша за коса Remington 2in1 Curls CI67E1"	: "CI67E1",
"Маша за коса Remington CI91W1B Proluxe Midnight Edition " : "CI91W1B",
"Ротационна самобръсначка Remington R3000" : "R3000",
"Машинка за подстригване Remington HC620" : "HC620",
"Маша за коса Remington CI5408 Mineral Glow" : "CI5408",
"Преса за коса Remington S1005" : "S1005",
"Ретро преса Remington CI91AW PROluxe" : "CI91AW",
"Сешоар Remington D7777 Air3D" : "D7777",
"Комплект електрически ролки за коса Remington Ionic H5600" : "H5600",
"Комплект сешоар с аксесоари Remington D3195GP" : "D3195GP",
"Сешоар Remington Advanced Colour Protect AC8605" : "AC8605",
"Машинка за подстригване на брада и коса 6 в 1 Remington Graphite Series G3 PG3000" : "PG3000",
"Машинка за подстригване Remington Heritage Manchester United Edition" : "HC9105",
"Сешоар Remington D7777 Air3D" : "D7777",
"Комплект електрически ролки за коса Remington Ionic H5600" : "H5600",
"Комплект сешоар с аксесоари Remington D3195GP" : "D3195GP",
"Сешоар Remington Advanced Colour Protect AC8605" : "AC8605",
"Машинка за подстригване на брада и коса 6 в 1 Remington Graphite Series G3 PG3000" : "PG3000",
"Машинка за подстригване Remington Heritage Manchester United Edition" : "HC9105",
"Електрическа четка за коса 2в1 Remington Hydraluxe As8901" : "AS8901",
"Комплект за грижа на лицето Remington Smooth & Silky EP7070" : "EP7070",
"Електрически ролки за коса Remington Jumbo Curls H5670" : "H5670",
"Преса за мокра коса Remington S7970 WET 2 STRAIGHT PRO" : "S7970",
"Сешоар Remington D41110OP" : "D41110OP",
"Комплект ролки за коса REMINGTON PROluxe H9100" : "H9100",
"Преса за коса Remington Keratin Therapy Pro S8590 *214568632-20-2/3" : "S8590",
"Преса за коса Remington S7710 Pro-Ion Straight 237403083-20-2" : "S7710",
"Комплект за лице и тяло Remington PG6045" : "PG6045"
}


"""
def get_url(url):
	#returns an object of a get request to passed url in the parameter
	sleep(random.randint(20, 30))
	return requests.get(url, headers = headers)
	


def get_soup(url):
	#Returns soup of the GET requetsed page
	page_soup = soup(get_url(url).text, "html.parser")
	return page_soup

def container_array(url):
	#Returns array of containers from soup
	return get_soup(url).findAll("div", {"class":"card-item card-standard js-product-data"})

def open_product_link():
	#Returns a performed GET request of the product's page 
	#link from the given container's HTML
	i = 1
	j = 1
	
	with open("EMA.csv", "w", newline="") as file:
		thewriter = csv.writer(file)
		thewriter.writerow(["Model", "Price"])
		while i <= 4:
			page_url = "https://www.emag.bg/search/remington/p"+str(i)
			array = container_array(page_url)
			for container in array:
				nam = container.a.img["alt"].split(",")
				n = nam[0].strip()
				price = container.find("p", {"class" : "product-new-price"}).get_text().replace(" лв.", "")
				price = int(price)
				price = price/100
				price = str(price)
				try:
					name = emag_dic[n]
					thewriter.writerow([name, price])
					print(str(j) + ". " + name)
					print(price+"\n")
					j+=1
				except:
					
					name = "NewProduct"
					thewriter.writerow([name, price])
					print(str(j)+". "+n)
					print(price+"\n")
					j+=1
					continue
			i+=1


open_product_link()

df = pd.read_csv("EMA.csv")
Test= df.sort_values("Price")

Test2 = Test.drop_duplicates(["Model"],"first")
Test2 = Test2.reset_index(drop= True)
print(Test2)
Test2.to_csv("emag.csv", index = False)
os.remove("EMA.csv")"""


p =1
j =1

with open("EMA.csv", "w", newline="") as file:
		thewriter = csv.writer(file)
		thewriter.writerow(["Model", "Price"])
		while p<=4:

			driver = webdriver.Chrome(PATH, chrome_options = options)
			driver.get("https://www.emag.bg/search/remington/"+str(p))
			sleep(10)

			button = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/section[1]/div/div[2]/div/div[3]/div[2]/div[2]/div[4]/div/div[4]/div/button[1]")
			button.click()
			sleep(5)
			button2 = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/section[1]/div/div[2]/div/div[3]/div[2]/div[2]/div[4]/div/div[3]/div/button")
			button2.click()
			sleep(5)
			select = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/section[1]/div/div[2]/div/div[3]/div[2]/div[2]/div[4]/div/div[3]/div/div/ul/li[3]/a")
			select.click()
			sleep(5)

			page = driver.page_source
			page_soup = soup(page, "html.parser")

			containers = page_soup.find_all("div", class_ ="card-item card-standard js-product-data")
			
			for container in containers:
				full_name = container.find("a", class_="card-v2-title semibold mrg-btm-xs js-product-url").text
				name_array = full_name.split(",")
				Rname = name_array[0]
				

				full_price = container.find("p", class_="product-new-price").text
				price_str = full_price.replace(" лв.", "")
				price = int(price_str)/100
				price = str(price)
				

				try:
					name = emag_dic[Rname]
					thewriter.writerow([name, price])
					print(str(j) + ". " + name)
					print(price+"\n")
					j+=1
				except:
					name = "NewProduct"
					thewriter.writerow([name, price])
					print(str(j)+". "+Rname)
					print(price+"\n")
					j+=1
					continue
			
			p+=1
			driver.close()


df = pd.read_csv("EMA.csv")
Test= df.sort_values("Price")

Test2 = Test.drop_duplicates(["Model"],"first")
Test2 = Test2.reset_index(drop= True)
print(Test2)
Test2.to_csv("emag.csv", index = False)
os.remove("EMA.csv")

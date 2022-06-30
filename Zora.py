import csv
import random
import requests
from bs4 import BeautifulSoup as soup 
from time import sleep
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')

Zora_dict = {
"S3500 E51"   : "S3500",
"HC5035 E51"  :	"HC5035",
"S3580" 	  : "S3580",
"NE3850" 	  : "NE3850",
"HC5018 E51" :	"HC5018",
"HC5100 E51"	 :"HC5100",
"D3015" :	"D3015",
"PG3000" 	: "PG3000",
"D5715 E51"	: "D5715",
"CI5318 E51":	"CI5318",
"HC7110 E51":	"HC7110",
"S1510 E51"	: "S1510",
"D5219 E51":	"D5219",
"D5220" :	"D5220",
"S3505GP" :	"S3505GP",
"S6300 E51":	"S6300",
"CI83V6" :	"CI83V6",
"BHT2000A E51":	"BHT2000A",
"CI91AW" 	: "CI91AW",
"S5505 E51"	: "S5505",
"HC7130 E51":	"HC7130",
"AC8002 E51":	"AC8002",
"S8540 E51"	:   "S8540",
"S6505 E51"	:   "S6505",
"HC7150 E51":	"HC7150",
"S8670" :	    "S8670",
"S5506GP" :	"S5506GP",
"S6606 E51"	: "S6606",
"AC8820" :	"AC8820",
"S9505 E51"	:"S9505",
"S8598" :	"S8598",
"CB7400 четка" : "CB7400",
"NE3870 E51" : "NE3870",
"CI9132 Proluxe 32mm Tong" : "CI9132",
"HC7110 E51***":"HC7110",
"HC7130 E51***":"HC7130",
"HC7150 E51***":"HC7150",
"S5506GP****": "S5506GP",
"S3500 E51***": "S3500",
"BHT2000A E51***" : "BHT2000A",
"CI83V6***" : "CI83V6",
"S6505 E51***" : "S6505",
"S9505 E51***" : "S9505",
"AC8820***" : "AC8820",
"S8670***" : "S8670",
"S8598***" : "S8598",
"PG2000" : "PG2000",
"D5715 E51***" : "D5715",
"CI5408 E51 Mineral Glow" : "CI5408",
"D5408 E51 Mineral Glow" : "D5408",
"S5408 E51 Mineral Glow" : "S5408",
"AC7200W" : "AC7200W",
"AC8901" : "AC8901",
"D7777 Air 3D": "D7777"
}


def get_url(url):
	"""This function performs a GET request to URL
	passed as a parameter within its execution"""                   			 
	with requests.Session() as session:
		return session.get(url)

def make_soup(url):
	"""Function returns a soup object stored in the variable""" 
	return soup(get_url(url).text, "html.parser")

def container_array(url):
	"""Get container array from make_soup(url) function's
	returned soup"""
	return make_soup(url).findAll("div", {"class" : "_product js-product one-fourth"})

def print_data(url):
	"""Perform a GET request to product url of each product and call the and
	record its name and product"""
	containers = container_array(url)
	print("This will be displayed on top")
	print(len(containers))
	with open("Zora.csv", "w", newline="") as file:
		thewriter = csv.writer(file)
		thewriter.writerow(["Model", "Price"])

		srl=1

		for box in containers:
			link = box.a.get("href")
			data = open_product_link(link)
			model_name = data[0]
			try:
				model = Zora_dict[model_name]
				price = data[2]
				print(str(srl)+". "+model)
				print(price +"\n")
				srl+=1
				thewriter.writerow([model, price])
				
			except:
				model = data[1]
				price = data[2]
				print(str(srl)+". "+model)
				print(price +"\n")
				srl+=1
				#thewriter.writerow([model, price])

				continue

def open_product_link(url):
	"""Function performs a GET request to url
	passed to it from the selected container's href tag"""
	PATH = "C:\Program Files (x86)\chromedriver.exe"
	driver = webdriver.Chrome(PATH, chrome_options=options)
	driver.get(url)
	#sleep(random.randint(1,3))   Not using it because it slows down the script
	page_html = driver.page_source
	page_soup = soup(page_html, "html.parser")
	model = page_soup.find("span", {"class":"_product-details-sku variant-sku-js"}).i.get_text()
	name = page_soup.find("h1", {"class", "js-product-title"}).get_text()
	price = page_soup.find("span", {"class" : "_product-details-price-new price-new-js price-new-js-product"}).get_text().replace("  лв.", "").replace(",",".")
	driver.quit()
	return [model, name, price]

print_data("https://zora.bg/search?per_page=50&query=remington")






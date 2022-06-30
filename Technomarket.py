import time
import bs4
from bs4 import BeautifulSoup as soup
import re
import csv

from time import sleep
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')

PATH = "C:\Program Files (x86)\chromedriver.exe"

techno_dic={" СЕШОАР REMINGTON AC9140":"AC9140",

" ПРЕСА ЗА КОСА REMINGTON S6500":"S6500",

" МАШИНКА ЗА ПОДСТРИГВАНЕ REMINGTON  HC5200":"HC5200",

" САМОБРЪСНАЧКА REMINGTON PR1330": "PR1330",

" САМОБРЪСНАЧКА REMINGTON F3000": "F3000",

" ПРЕСА REMINGTON S9100":"S9100",

" МАША REMINGTON CI9525":"CI9525",

" МАША REMINGTON CI8605":"CI8605",

" ТРИМЕР REMINGTON BHT2000A":"BHT2000A",

" ПРЕСА ЗА КОСА REMINGTON S9700": "S9700",

" ЕЛЕКТРИЧЕСКА ЧЕТКА ЗА КОСА REMINGTON AS8810": "AS8810",

" ПРЕСА ЗА КОСА REMINGTON S-1510": "S1510",

" ПРЕСА ЗА КОСА REMINGTON S1A100 STRAIGHTENER": "S1A100",

" СЕШОАР REMINGTON AC8605 E51": "AC8605",

" ТРИМЕР REMINGTON MB050 DURABLADE": "MB050",

" ПРЕСА ЗА КОСА REMINGTON S9505": "S9505",

" МАША REMINGTON CI-95": "CI95",

" ТРИМЕР REMINGTON NE-3150": "NE3150",

" СЕШОАР REMINGTON D-3010": "D3010",

" СЕШОАР REMINGTON D 3080": "D3080",

" МАШИНКА ЗА ПОДСТРИГВАНЕ REMINGTON HC 5900": "HC5900",

" МАШИНКА ЗА ПОДСТРИГВАНЕ REMINGTON HC 5018": "HC5018",

" ТРИМЕР REMINGTON WPG4010C E51": "WPG4010C",

" МАШИНКА ЗА ПОДСТРИГВАНЕ REMINGTON MB-4110":"MB4110",

" ПРЕСА REMINGTON S6755 MAN STRAIGHTENER": "S6755",

" ПРЕСА ЗА КОСА REMINGTON S-6505": "S6505",

" МАША REMINGTON CI5219GPR COMPLETE HAIR": "CI5219GPR",

" ПРЕСА ЗА КОСА REMINGTON S-5505": "S5505",

" ПРЕСА ЗА КОСА REMINGTON S-3500": "S3500",

" ПРЕСА REMINGTON S-1450": "S1450",

" ПРЕСА ЗА КОСА REMINGTON S3580 E51": "S3580",

" ФОТОЕПИЛАТОР REMINGTON IPL-6500  PRO": "IPL6500",

" МАША REMINGTON CI91AW PROLUXE": "CI91AW",

" ФОТОЕПИЛАТОР REMINGTON IPL-6250 ESSENTIAL": "IPL6250",

" ПРЕСА ЗА КОСА REMINGTON S-5525": "S5525",

" СЕШОАР REMINGTON AC-5999 PRO": "AC5999",

" СЕШОАР REMINGTON AC8820 KERATIN THERAPY": "AC8820",

" ПРЕСА ЗА КОСА REMINGTON S8598 KERATIN INTELLIGENT": "S8598",

" МАШИНКА ЗА ПОДСТРИГВАНЕ REMINGTON HC5100 E51": "HC5100",

" САМОБРЪСНАЧКА REMINGTON XF8705 E51 FOIL SHAVER": "XF8705",

" ЕЛЕКТРИЧЕСКА ЧЕТКА ЗА КОСА REMINGTON AS800 E51": "AS800",

" МАША REMINGTON CI1A119 E51 19 MM": "CI1A119",

" МАШИНКА ЗА ПОДСТРИГВАНЕ REMINGTON HC5038 MAN HAIR CLIPPER": "HC5038",

" МАШИНКА ЗА ПОДСТРИГВАНЕ REMINGTON HC9100 HERITAGE HAIR CLIPPER": "HC9100",

" СЕШОАР REMINGTON D2121 HAIR DRYER": "D2121",

" ТРИМЕР REMINGTON PG5000 GRAPHITE GROOMERG5": "PG5000",

" СЕШОАР REMINGTON AC5700 Copper Radiance Dryer": "AC5700",

" ТРИМЕР REMINGTON NE3850 E51 NANO SERIES": "NE3850",

" ТРИМЕР REMINGTON PG3000 GRAPHITE GROOMER G3": "PG3000",

" СЕШОАР REMINGTON D5408 E51 MINERAL GLOW HAIRDRYER": "D5408",

" ПРЕСА ЗА КОСА REMINGTON S7412 AIR PLATES": "S7412",

" СЕШОАР REMINGTON DC4110OB BOMBSHELL BLUE RETRO": "DC4110OB",

" ПРЕСА ЗА КОСА REMINGTON S5506GP PRO-CERAMIC TITANIUM": "S5506GP",

" ТРИМЕР REMINGTON PG2000 E51 G2 GRAPHITE GROOMER": "PG2000",

" МАШИНКА ЗА ПОДСТРИГВАНЕ REMINGTON HC5035  COLOUR HAIR CLIP": "HC5035",

" ПРЕСА ЗА КОСА REMINGTON S5700 Copper Radiance Straightener": "S5700",

" СЕШОАР REMINGTON D-3015 POWER VOLUME 2000": "D3015",

" МАША REMINGTON CI-5319 PRO-SPIRAL CURL": "CI5319",

" МАША REMINGTON CI5700 Copper Radiance Tong": "CI5700",

" ТРИМЕР REMINGTON PG6000 E51 G6 GRAPHITE GROOMER": "PG6000",

" ТРИМЕР REMINGTON MB4128 MAN BEARD BOSS STYLER": "MB4128",

" СЕШОАР REMINGTON D5706 CURL and STRAIGHT CONFIDENCE": "D5706",

" СЕШОАР REMINGTON AC9096 E51 SILK DRYER": "AC9096",

" ТРИМЕР REMINGTON PG4000 GRAPHITE GROOMER G4": "PG4000",

" ПРЕСА ЗА КОСА REMINGTON S-9600 SILK ULTIMATE STRAIGHTE": "S9600",

" ГРИЖА ЗА ТЯЛОТО REMINGTON SP-6000 IPL PRO REFILL BULB": "SP6000",

" СЕШОАР REMINGTON D5219 E51 STYLE DRYER KIT": "D5219",

" ПРЕСА ЗА КОСА REMINGTON S5408 E51 MINERAL GLOW STRAIGHTENER": "S5408",

" МАША REMINGTON CI5408 E51 MINERAL GLOW CURLING WAND": "CI5408",

" СЕШОАР REMINGTON D5215 E51 PRO-AIR SHINE": "D5215",

" СЕШОАР REMINGTON D3012GP GIFT PACK S1450/D3010": "D3012GP",

" СЕШОАР REMINGTON D5755 MAN HAIR DRYER PRO 2400": "D5755",

" МАША REMINGTON CI96W1 E51 SILK CURLING WAND": "CI96W1",

" МАШИНКА ЗА ПОДСТРИГВАНЕ REMINGTON HC7170 E51 PRO POWER TITANIUM PRO": "HC7170",

" МАШИНКА ЗА ПОДСТРИГВАНЕ REMINGTON HC7130 E51 PRO POWER TITANIUM": "HC7130",

" МАШИНКА ЗА ПОДСТРИГВАНЕ REMINGTON HC7110 E51 PRO POWER STAINLESS STEEL": "HC7110",

" ПРЕСА ЗА КОСА REMINGTON S6606 E51 CURL and STRAIGHT CONFIDENCE": "S6606",

" СЕШОАР REMINGTON AC8901 Hydraluxe Pro": "AC8901",

" ПРЕСА ЗА КОСА REMINGTON S8901 Hydraluxe Pro": "S8901",

" МАША REMINGTON CI89H1 Hydraluxe Pro": "CI89H1",
" ТРИМЕР REMINGTON HG1000 OmniBlade": "HG1000",
" МАШИНКА ЗА ПОДСТРИГВАНЕ REMINGTON HC-5150": "HC5150",
" СЕШОАР REMINGTON D5901 Coconut Smooth":"D5901",
" ЕЛЕКТРИЧЕСКА ЧЕТКА ЗА КОСА REMINGTON AS8901 HYDRALUX":"AS8901",
" МАША REMINGTON CI5901 Coconut Smooth": "CI5901",
" ПРЕСА ЗА КОСА REMINGTON S7970 Wet2Straight PRO":"S7970",
" СЕШОАР REMINGTON D6940GP E51 Hairdryer GS": "D6940GP",
" - REMINGTON D8700 PROTECT DRYER": "D8700",
" ПРЕСА ЗА КОСА REMINGTON S5901 Coconut Smooth":"S5901",
" СЕШОАР REMINGTON D3195GP E51 Hairdryer Gift": "D3195GP",
" МАШИНКА ЗА ПОДСТРИГВАНЕ REMINGTON HC5000 E51 X5 Power-X Series": "HC5000",
" МАШИНКА ЗА ПОДСТРИГВАНЕ REMINGTON HC3000 E51 X3 Power-X Series": "HC3000",
" МАШИНКА ЗА ПОДСТРИГВАНЕ REMINGTON HC6000 E51 X6 Power-X Series": "HC6000",
" ПРЕСА ЗА КОСА REMINGTON S8540": "S8540",
" ПРЕСА ЗА КОСА REMINGTON S9001 E51 Hydraluxe Pro Straightener": "S9001"
}

driver = webdriver.Chrome(PATH, chrome_options= options)
driver.get(f"https://www.technomarket.bg/search?query=remington")

wait = WebDriverWait(driver, 5)
try:
    sleep(5)
    driver.switch_to_frame("cp_iframe")
    element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[3]")))
    element.click()
except Exception as e:
    print(e)

sleep(5)
driver.switch_to_default_content()
sleep(3)
element = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/mat-dialog-container/tm-terms-settings/div/div[5]/button")
element.send_keys(Keys.RETURN)

sleep(2)
element = driver.find_element_by_id("mat-select-value-3")
element.click()

element = driver.find_elements_by_class_name("mat-option-text")[2]
element.click()

sleep(5)

newpage = driver.page_source
soupa = soup(newpage, "html.parser")

sleep(2)



model = soupa.find_all(class_ = re.compile("title-link ng-tns-c207"))
price = soupa.find_all(class_ = re.compile(r"product-price-standard_price|product-price-retail_promo|product-price-internet_promo"))
print(len(model))

model_list = []

for i in model:
    try:
        model_name= i.get_text()
        modelNumber= techno_dic[model_name]
        model_list.append(modelNumber)
    except:
        model_list.append(model_name)

x = zip(model_list,price)

filename= "technomarket.csv"
f= open(filename, "w")
headers= "Model, Price\n"
f.write(headers)

for _model,_price in x:
    print(_model)
    f.write(_model+",")
    price_rectify= _price.get_text()
    price= price_rectify.replace("-","0")
    if price == "ИЗЧЕРПАН":
        price = 0
        print("out")
        f.write(str(0)+"\n")
        print()
        continue
    else:
        print(price)
        f.write(price+"\n")
    
    print()

driver.close()
f.close()
print("ok, done go ahead")
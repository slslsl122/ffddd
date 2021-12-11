import requests
from bs4 import BeautifulSoup
url = "https://tumen.bankiros.ru/currency/usd"
headres = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36"}
text = requests.get(url, headers=headres)
soup = BeautifulSoup(text.content, "html.parser")
convert = soup.findAll("span", {"class": "bank_usd_437_sell"})
pop = input("видите сколька вы хотите долларов перевести в рубли:")
pos = float(pop)
asa = float(convert[0].text)
ads = asa*pos
print("руб:", ads)

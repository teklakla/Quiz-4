import requests
from bs4 import BeautifulSoup
import csv
import time
from random import randint

info = []

for page in range(1, 5):
    path = f"https://dressup.ge/ka/75-mamakaci?page={page}"
    pasuxi = requests.get(path)

    soup = BeautifulSoup(pasuxi.text, 'html.parser')

    produqtebi = soup.find("div", class_='products row products-grid')
    yvela_produqti = produqtebi.find_all('div', class_="js-product-miniature-wrapper col-6 col-md-4 col-lg-3 col-xl-15")

    for produqti in yvela_produqti:
        fasi = produqti.find("div", class_="product-price-and-shipping").span.text
        kategoria = produqti.find('div', class_='product-category-name text-muted').text
        saxeli = produqti.find('h2', class_='h3 product-title').a.text

        info.append((saxeli, kategoria, fasi))

    time.sleep(randint(15, 20))

with open('info.csv', 'w', newline='\n', encoding="utf-8_sig") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    for i in info:
        writer.writerow([i[0], i[1], i[2]])








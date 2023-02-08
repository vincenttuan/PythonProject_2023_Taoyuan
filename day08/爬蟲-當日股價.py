# https://tw.stock.yahoo.com/quote/2330
#<span class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)">538</span>
import requests
from bs4 import BeautifulSoup

url = 'https://tw.stock.yahoo.com/quote/2330'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
tag = '<span class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)">'
for span in soup.findAll('span'):
    if tag in str(span):
        print(span.text)

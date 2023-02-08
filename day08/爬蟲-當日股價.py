# https://tw.stock.yahoo.com/quote/2330
#<span class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)">538</span>
import requests
from bs4 import BeautifulSoup

url = 'https://tw.stock.yahoo.com/quote/2330'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
# <span class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)">538</span>
class_value = 'Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)'
span = soup.find(name="span", attrs={"class": class_value})
print(span.text)

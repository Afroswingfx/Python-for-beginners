import re
import urllib.request
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()
numbers = re.findall(r"[0-9]+(?=\s|$)", text)

total = sum(int(n) for n in numbers)
print(total)
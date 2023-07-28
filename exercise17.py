# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the
# New York Times homepage.

import requests  # "http for humans"
from bs4 import BeautifulSoup  # html parsing

url = "https://www.nytimes.com/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
headlines = soup.find_all(class_="indicate-hover")
for title in headlines:
    print(title.get_text())

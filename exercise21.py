# Take the code from the How To Decode A Website exercise, and instead of printing the results to a screen, write the
# results to a txt file. In your code, just make up a name for the file you are saving to.
#
# Extras:
#
# Ask the user to specify the name of the output file that will be saved.

import requests  # "http for humans"
from bs4 import BeautifulSoup  # html parsing

file_name = input("Enter name for file (.txt): ")
file = open(file_name, "a")

url = "https://www.nytimes.com/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
headlines = soup.find_all(class_="indicate-hover")
for title in headlines:
    file.write(title.get_text() + "\n")
file.close()

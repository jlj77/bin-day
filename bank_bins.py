# Importing the required libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Downloading contents of the bank holiday bin collection page
url = "https://www.cheltenham.gov.uk/bank-holiday-collections"
data = requests.get(url).text

# Creating BeautifulSoup object
soup = BeautifulSoup(data, 'html.parser')

# Verifying the tables and their captions
print('Caption of each table:')
for table in soup.find_all('table'):
    print(table.caption.text)
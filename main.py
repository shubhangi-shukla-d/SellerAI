import requests
from bs4 import BeautifulSoup
import os

# URL of the website to scrape
url = 'https://sellerai.org/'

# Create a requests session and get the HTML content
session = requests.Session()
response = session.get(url)
html_content = response.content

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Create a directory to save the website content
if not os.path.exists('SellerAI'):
    os.mkdir('SellerAI')

# Save the HTML content of the homepage
with open('SellerAI/index.html', 'w') as f:
    f.write(str(soup))

# Find all links on the homepage and save their content recursively
for link in soup.find_all('a'):
    href = link.get('href')
    print(href)
    if href.startswith(url):
        filename = href.replace(url, '').strip('/')
        print(filename)
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        response = session.get(href)
        with open(filename, 'wb') as f:
            f.write(response.content)

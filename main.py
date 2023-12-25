from bs4 import BeautifulSoup
import requests
import lxml

url_to_scrape = 'https://www.google.com/news'
response = requests.get(url_to_scrape)
html_content = response.content
soup =  BeautifulSoup(html_content, 'lxml')
soup2 = soup.find_all('h2')
print(soup2)
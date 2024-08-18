import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/dp/B07FZ8S74R'
print("URL: "+url+"\n")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
print("HEADERS: \n")
print(headers)
response = requests.get(url, headers=headers)
print("RESPONSE: \n")
print(response)
soup = BeautifulSoup(response.content, 'html.parser')
print("SOUP: \n")
print(soup)
print("\n\nTITLE sOUP: ")
print(soup.title.text)

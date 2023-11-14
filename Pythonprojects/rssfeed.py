from bs4 import BeautifulSoup
import requests
url = requests.get('https://realpython.com/atom.xml')
print(url)
soup = BeautifulSoup(url.content,'xml')
entries = soup.findAll('entry')
for entry in entries:
    title = entry.title.text
    summary = entry.summary.text
    link = entry.link['href']
    print(f'title:{title}\n summary:{summary}\nlink"{link}')


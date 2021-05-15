from bs4 import BeautifulSoup
import requests
import webbrowser

command = input("Enter a command")
res = requests.get("https://google.com/search?q=" + command)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select('.kCrYT a')
for i in links[:5]:
    webbrowser.open('https://google.com/'+i.get('href'))
    print(i.get('href'))


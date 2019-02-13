import requests
from bs4 import BeautifulSoup


response=requests.get('https://www.instagram.com/accounts/login/?hl=en')

soup=BeautifulSoup(response.content,'lxml')
#first occurence of script
script=soup.script
body=soup.body
print(body)
Title=soup.title
print(Title)


print(script)
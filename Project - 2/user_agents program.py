"""
pip install fake_useragent
"""
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


UA=UserAgent()

header={'user-agent':UA.chrome}
webpage = requests.get('https://www.instagram.com/accounts/login/?hl=en',headers=header)
soup = BeautifulSoup(webpage.content,'lxml')
print(soup.prettify())












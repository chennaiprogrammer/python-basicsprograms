"""request  url  send webpage  along  with status code
values 1XX = information tranfers code
2XX = success code
3XX = redirection
4XX = client_error
5XX = server_error
"""

import  requests

url='https://hack.me/s/'
response=requests.get(url)
print(response)
"""return content of webpage"""
#print(response.content)

header=response.headers.items()
for key,values in header:
    print(key," ",values)
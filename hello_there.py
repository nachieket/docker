import requests

x = requests.get('https://www.google.com')

if x.status_code == 200:
    print('yay!')
else:
    print('oh!')

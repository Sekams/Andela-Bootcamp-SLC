import requests
""" 
    This application is written in Python 3.6.1.
    It uses the requests library by Kenneth Reitz available at https://github.com/kennethreitz/requests. 
    This library can also be installed via command line by running the command: python -m pip install requests
    The application consumes an API which returns currency rates as obtained from http://api.fixer.io/latest
"""

resp = requests.get('http://api.fixer.io/latest')
if resp.status_code != 200:
    raise requests.HTTPError('http://api.fixer.io/latest: ' + str(resp.status_code))
result = resp.json()
print('The currency rates based on the ' + str(result['base']) + ' on ' + str(result['date']) + ' are:')
print(result['rates'])

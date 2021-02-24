import requests
import sys
import os
import re
import logging
import json

argv = sys.argv
print('arguments : ', argv)
filename = os.path.split(sys.argv[0])[1] + '.log'
print(filename)

logging.basicConfig(handlers=[logging.FileHandler(filename=filename,
                                                 encoding='utf-8', mode='a+')],
                    format="%(message)s", 
                    level=logging.INFO)
p = re.compile('(\{\"+.{1,}\})')
url = argv[1]
response = requests.get(url=url)
if response.status_code != 200:
    print('Request failed.')
else:
    print(response)
    # logging.info(response.text)
    # logging.info(response.json)
    # logging.info(response.content)
    result = p.findall(response.text)
    if len(result) == 0:
        print('There is no json string extracted.')
    else:
        for row in result:
            logging.info(str(row))


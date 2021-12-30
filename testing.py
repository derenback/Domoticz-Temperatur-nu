#!/usr/bin/env python
import requests
import sys

#url = "https://www.temperatur.nu/termo/gettemp.php?stadname=mosas&what=temp"
#response = requests.get(url)
#print(response.content.decode('latin'))

c = sys.maxsize
print(c / ((60/5)*60*24*365))
for _ in range(121):
    if c % 60 == 0:
        print(c)
    c += 1
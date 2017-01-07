import requests
import time

latest='2017-01-07T20:01:09.706Z'

url='http://159.203.128.53/output/MM34dG0vpWs6a9dy0gQaCz8gGVe/latest.csv'

while True:

    time.sleep(2)
    r=requests.get(url)
    #print(r.text)

    s=r.text.split('\n')
    items=s[1].split(',')
    timestamp=items[-1]

    if (latest!=timestamp):
	with open("datshare/sbox.csv","a") as myfile:
	    myfile.write(s[1]+"\n")
	print(timestamp)
	latest=timestamp



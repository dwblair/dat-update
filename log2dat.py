import serial
import requests
import time
import json

#### some basic variables


baseURL = 'http://159.203.128.53'
#baseURL = 'https://data.sparkfun.com'

publicKey='KydOPJNdDNhzKlJjqm0KFPMGEVN'
privateKey='ALNEGp5N35in7vg30OW7IGpzL3d'

#serialPort="/dev/ttyACM0"
serialPort="/dev/ttyUSB0"

serialBaud = 9600

loopDelay = 10 #seconds

endl="\n"

ser = serial.Serial(serialPort, serialBaud)

#print "Waiting for serial port ..."
time.sleep(3)
#ser.flush() # flush to get rid of extraneous char

print "\n"

###### main loop 

while True:

    #cmd = "READ"
    #cmd = cmd.strip() + endl
    #ser.write(cmd.encode())
    print "Waiting for serial port ..."
    
    line = ser.readline()
    line=line.decode('utf-8')
    
    #print 'raw serial input: ', line.strip()
  
    parsed = line.split('\t')
    
    if len(parsed) == 2:
    
        rssi=parsed[0].split(':')[1].replace(" ","")

        j = str(parsed[1])

        #print 'rssi='+str(rssi)+" json="+j
        
        p = json.loads(j)
    
        #print p
	id = str(p["id"])
        rssi = str(rssi)
        temp = str(p["data"]["temp"])
        #light = str(p["data"]["light"])
	solar = str(p["data"]["A0"])
	humidity = str(p["data"]["humidity"])

	mdate = time.strftime("%x")

	mtime = time.strftime("%X")

	line = str(rssi)+","+str(solar)+","+str(temp)+","+str(humidity)+","+mdate+","+mtime

	print(line)

	with open("datshare/sbox.csv","a") as myfile:
	    myfile.write(line+"\n")
		
 

    

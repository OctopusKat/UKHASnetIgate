import urllib
import urllib2
import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 9600) # serial connection settings go here

while True:
  rawpkt = ser.readline().rstrip() # incoming data, one line at the time
  print (time.strftime("%c") + '\n\tIncoming raw: \t' + rawpkt) # %c should produce "Sun Feb  9 21:51:48 2014"-like dates

  if rawpkt.startswith('rx: '): # received RF packets get send down the serial connection with the rx prefix
    strppkt = rawpkt.strip('rx: ') # remove the rx-prefix
    print ('\tSending to API: ' + strppkt)

    url = 'http://ukhas.net/api/upload'
    values = {'origin' : 'RS00', 'data' : strppkt} # origin, who submitted it to the API?

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    print ('\tAPI response: \t' + the_page + '\n') # error chekking goes here

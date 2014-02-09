import urllib
import urllib2
import serial
import time
serialbuf = serial.Serial('/dev/ttyUSB0', 9600) # Configured for my setup
igatename = 'RS00' # should be the same as it's RF-id

while True:
  rawpacket = serialbuf.readline().rstrip() # We should look at the incoming data one line at the time
  print (time.strftime("%c") + '\n\tIncoming raw: \t' + rawpacket) # Timestamp in "Sun Feb  9 21:51:48 2014" formar

  if rawpacket.startswith('rx: '): # We are only intrested in received RF packets
    strippacket = rawpacket.strip('rx: ') # Remove the prefix
    print ('\tSending to API: ' + strippacket)

    url = 'http://ukhas.net/api/upload'
    values = {'origin' : igatename, 'data' : strippacket} # API requires origin and data

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    apifeedback = response.read().rstrip() # Once again we clean it up before parsing
    print ('\tAPI response: \t' + apifeedback + '\n') # error checking goes here

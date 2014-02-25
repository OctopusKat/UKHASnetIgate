import urllib
import urllib2
import serial
import time
import sys

serialbuf = serial.Serial('/dev/ttyUSB1', 9600) # Configured for my setup
igatename = 'RS00' # should be the same as it's RF-id

try:
  while True:
    try:
      rawpacket = serialbuf.readline().rstrip() # We should look at the incoming data one line at the time
      print (time.strftime("%c")) # Timestamp in "Sun Feb  9 21:51:48 2014" format

      if rawpacket.startswith('rx: '): # We are only intrested in received RF packets
        print ('\tIncoming raw: \t' + rawpacket)

        strippacket = rawpacket.strip('rx: ') # Remove the prefix
        print ('\tSending to API: ' + strippacket)

        url = 'http://ukhas.net/api/upload'
        values = {'origin' : igatename, 'data' : strippacket} # API requires origin and data

        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        apifeedback = response.read().rstrip() # Once again we clean it up before parsing
        print ('\tAPI response: \t' + apifeedback + '\n')

      else:
        print ('\tIncoming raw: \t\033[1m' + rawpacket + '\033[0m\n')

    except Exception, e:
      continue

except KeyboardInterrupt:
    print '\nClean exit. Bye bye!'
    serialbuf.close() # Close serial port
    sys.exit()

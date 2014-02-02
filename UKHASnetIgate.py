import urllib
import urllib2
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)

# API (POST) http://ukhas.net/api/upload
# origin: [callsign of gateway node]
# data: [raw data packet]

while True:
  rawpkt = ser.readline().rstrip()
  print ('Incoming raw: ' + rawpkt)

  url = 'http://ukhas.net/api/upload'
  values = {'origin' : 'REVSPACE00', 'data' : rawpkt}

  data = urllib.urlencode(values)
  req = urllib2.Request(url, data)
  response = urllib2.urlopen(req)
  the_page = response.read()
  print ('API response: ' + the_page)

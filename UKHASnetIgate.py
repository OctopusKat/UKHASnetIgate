import urllib
import urllib2
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600) # Serial connection settings go here

while True:
  rawpkt = ser.readline().rstrip() # incoming data, one line at the time, stripped from all kind of whitespaces
  print ('Incoming raw: ' + rawpkt)

  url = 'http://ukhas.net/api/upload'
  values = {'origin' : 'REVSPACE00', 'data' : rawpkt} # origin, who submitted it to the API?

  data = urllib.urlencode(values)
  req = urllib2.Request(url, data)
  response = urllib2.urlopen(req)
  the_page = response.read()
  print ('API response: ' + the_page)

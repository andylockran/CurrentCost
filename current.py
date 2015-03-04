#!/usr/bin/python

import serial,sys,time,io,re
from BeautifulSoup import BeautifulSoup
from datetime import datetime
import paho.mqtt.client as mqtt
import xmltodict
import json


ser = serial.Serial(
  port='/dev/ttyUSB0',
  baudrate=57600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1)

sio = io.TextIOWrapper(io.BufferedReader(ser), line_buffering=True)

while True:
  x = sio.readline()
  if x:
    time.sleep(2)
    if re.search("kwh",x):
      pass
    else:
      mins = x
      break

results = xmltodict.parse(mins)
osinfo = json.dumps(results)
osensor = mqtt.Client(client_id="CLIENTID")
osensor.username_pw_set("USERNAME", password="PASSWORD")
osensor.connect("opensensors.io")
osensor.publish("TOPICURL",payload=osinfo,qos=0,retain=False)
osensor.disconnect()
exit(5)

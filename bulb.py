###########
# In this code we subscribe to a topic(paho/bulb) and turn on bulb when message is received using shell commands
############

import time
import paho.mqtt.client as mqtt
#import subprocess as sp
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.IN)



def on_connect(client, userdata, flags, rc):
 print "Connected with result code "+str(rc)
 (result,mid)= client.subscribe("paho/bulb/team_001")


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    data = int(msg.payload)
   # print(data)
    if(data is 1):
     GPIO.output(12,1)
    else:
     GPIO.output(12,0)
#    arg = ('gpio write 1 %d' %(data))    
#    sp.call(arg,shell=True)



mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("iot.eclipse.org", 1883,60)
mqttc.loop_start()
#mqttc.loop_start()
mqttc.loop_forever()

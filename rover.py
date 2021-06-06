import RPi.GPIO as gpio
import time
from threading import Thread
import paho.mqtt.client as mqtt

gpio.setmode(gpio.BOARD)
gpio.setup(11,gpio.OUT)
gpio.setup(12,gpio.OUT)
gpio.setup(37,gpio.OUT)
gpio.setup(35,gpio.OUT)
#gpio.setup(36,gpio.OUT)
gpio.setup(38,gpio.OUT)#enable pin to te l293d
gpio.setup(7,gpio.OUT)
gpio.setup(5,gpio.IN)
gpio.output(38,0)


def ultrasonic():
   while 1:
    gpio.output(7,1)
    time.sleep(0.00001)
    gpio.output(7,0)
    t1=time.time()
    t2=time.time()
    while gpio.input(5) == 0:
     t1=time.time()
    while gpio.input(5) == 1:
     t2=time.time()
    dif=t2-t1
    d=dif*(343/2)
    if(d <= 0.15):
       gpio.output(36,0)
       gpio.output(38,0)
       return


t1 = Thread(target = ultrasonic, args = ())

def on_connect(client, userdata, flags, rc):
 print "Connected with result code "+str(rc)
 (result,mid)= client.subscribe("foo/bar5")


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    k  = int(msg.payload)
    gpio.output(38,0)
    time.sleep(50)

    if ( k==0):
      gpio.output(38,0)
    if(k == 1):
      gpio.output(38,1)
      gpio.output(37,0)
      gpio.output(35,1)
      gpio.output(12,0)
      gpio.output(11,1)
    if(k == 2):
      gpio.output(38,1)
      gpio.output(37,1)
      gpio.output(35,0)
      gpio.output(12,1)
      gpio.output(11,0)
    
    if(k == 3):
     gpio.output(38,1)
     gpio.output(37,1)
     gpio.output(35,0)
     gpio.output(12,0)
     gpio.output(11,1)
     

    if(k == 4):
     gpio.output(38,1)
     gpio.output(37,0)
     gpio.output(35,1)
     gpio.output(12,1)
     gpio.output(11,0)
     


#    arg = ('gpio write 1 %d' %(data))
#    sp.call(arg,shell=True)



mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("broker.hivemq.com", 1883,60)
mqttc.loop_start()
mqttc.loop_forever()


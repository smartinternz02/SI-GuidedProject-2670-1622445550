import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "tcq2tg",
        "typeId": "ESP32",
        "deviceId":"20R15A0"
    },
    "auth":  {
        "token": "qcRudH(FaJ&ijZy)9&"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    allow=random.randint(0,100)
    out=random.randint(0,100)
    parslots1=random.randint(0,100)
    parslots2=random.randint(0,100)
    parslots3=random.randint(0,100)
    parslots4=random.randint(0,100)
    parslots5=random.randint(0,100)
    parslots6=random.randint(0,100)
    myData={'U':{'allow':allow, 'out':out, 'parslots1':parslots1, 'parslots2':parslots2, 'parslots3':parslots3, 'parslots4':parslots4, 'parslots5':parslots5, 'parslots6':parslots6}}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(10)
client.disconnect()

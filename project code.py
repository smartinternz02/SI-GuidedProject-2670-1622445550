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
    entrygate=input("Enter your value:  ")
    print(entrygate)
    exitgate=input("Enter your value:   ")
    print(exitgate)
    numberofvechiclesentering=input("Enter your value:   ")
    numberofvechiclesleaving=input("Enter your value:   ")
    parslots1=input("Enter your value:  ")
    parslots2=input("Enter your value:  ")
    parslots3=input("Enter your value:  ")
    parslots4=input("Enter your value:  ")
    parslots5=input("Enter your value:  ")
    parslots6=input("Enter your value:  ")
    myData={'U':{'entrygate':entrygate, 'exitgate':exitgate,  'numberofvechiclesentering':numberofvechiclesentering, 'numberofvechiclesleaving':numberofvechiclesleaving, 'parslots1':parslots1, 'parslots2':parslots2, 'parslots3':parslots3, 'parslots4':parslots4, 'parslots5':parslots5, 'parslots6':parslots6}}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(10)
client.disconnect()

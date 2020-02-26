import cv2
import requests
import paho.mqtt.client as mqttClient
import time

SMART_BIN_CHECK_STATE = "https://smartbin-sut.herokuapp.com/SmartBin/State/B001"

while True:
    getState = requests.get(SMART_BIN_CHECK_STATE).json()
    print("State:", getState)

    if(getState == 0):
        print("--------------------Wernning--------------------")
        time.sleep(3)
    elif(getState == 1):
        print("---------------------Ready---------------------")
        time.sleep(3)
    elif(getState == 2):
        KERAS_REST_API_URL = "http://localhost:5000/predict"

        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, frame = cap.read()
        else:
            ret = False

        image = cv2.imwrite("img.jpg",frame)
        cap.release() 

        IMAGE_PATH = "img.jpg"
        image = open(IMAGE_PATH, "rb").read()
        payload = {"image": image}

        post = requests.post(KERAS_REST_API_URL, files=payload).json()
        global BinType
        BinType = post['typebin']
        print(BinType)

        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                global connected                
                connected = True
                print("Connected to broker")

            else:
                print("Connection failed")

        connected = False 

        broker_address= "broker.mqttdashboard.com"
        port = 1883
        user = "apichate"
        password = "0885090659"

        client = mqttClient.Client("Python")               
        client.username_pw_set(user, password=password)    
        client.on_connect= on_connect                      
        client.connect(broker_address, port=port)

        client.loop_start()
            
        while connected != True:
            print("Wait for connection")
            time.sleep(0.1)

        try:
                
            if(BinType == "G"):
                client.publish("TEST/MQTT","L")
                print("L")
            elif(BinType == "B"):
                client.publish("TEST/MQTT","R")
                print("R")
        except:
            client.disconnect()
            client.loop_stop()
        put = requests.put("https://smartbin-sut.herokuapp.com/SmartBin/B001/" + BinType).json()
        print(put['Ids'])
        time.sleep(15)
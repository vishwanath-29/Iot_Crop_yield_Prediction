import random  
import time
import sys


from azure.iot.device import IoTHubDeviceClient, Message  

CONNECTION_STRING = "HostName=crop-yield-prediction.azure-devices.net;DeviceId=raspberry-pi-3;SharedAccessKey=if+wMzeH69a/JSQ7qzyHayHpilk2JSIwZ3l21JC64UE=" 

MSG_SND = '{{"temperature": {temperature},"humidity": {humidity},"Moisture":{moisture},"pH":{pH}}}'  

while True:
    
    def iothub_client_init():
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)  
        return client  
    def iothub_client_telemetry_sample_run():  
        try:  
            client = iothub_client_init()  
            print ( "Sending data to IoT Hub, press Ctrl-C to exit" )  
            while True: 
                try:
                    temperature = round(random.uniform(20,25), 3)
                    humidity = round(random.uniform(9,15), 3)
                    moisture = round(random.uniform(100,170), 2)
                    pH = round(random.uniform(6.1,6.9), 2)
                except RuntimeError:
                    print("Error")
                msg_txt_formatted = MSG_SND.format(temperature=temperature, humidity=humidity,moisture=moisture,pH=pH)  
                message = Message(msg_txt_formatted)  
                print( "Sending message: {}".format(message) )  
                client.send_message(message)  
                print ( "Message successfully sent" )  
                time.sleep(3)  
        except KeyboardInterrupt:  
            print ( "IoTHubClient stopped" ) 
            sys.exit(0)
    if __name__ == '__main__':  
        print ( "Press Ctrl-C to exit" )  
        iothub_client_telemetry_sample_run()

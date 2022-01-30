import serial
import time
import csv
import json
import websocket
import random
import time
import json
import requests


arduino_port = "com6"
baud = 115200
header = ["DateTime","TimeEpoch","Temperature","Humidity","xaccelaration","yaccelaration", "zaccelaration"]

#title = open("Online_DAQ.csv", "w+")
#block = csv.writer(title)
#block.writerow(header)
#title.close()

ser = serial.Serial(arduino_port,baud)
time.sleep(1)
ser.flushInput()

class readData():
    def main(self):
        while (ser.inWaiting()==0):
            #print("No data")
            pass


        ser_data = ser.readline()
        decoded_data = str(ser_data, 'utf-8')
        data_by_data = decoded_data.split(',')
        TempC = data_by_data[0]
        Humidity = data_by_data[1]
        X = float(data_by_data[2])
        Y = float(data_by_data[3])
        Z = float(data_by_data[4])


        x=[]
        y=[]
        z=[]
        x.append(X)
        y.append(Y)
        z.append(Z)


        with open("Online_DAQ.csv", "a") as f:
            file = csv.writer(f)
            time_now = time.localtime()
            file.writerow([time.strftime("%Y/%m/%d %H:%M:%S", time_now), time.time(), TempC, Humidity, X, Y, Z])

        return (x,y,z)


    def flushData(self):
        self.x.clear()
        self.y.clear()
        self.z.clear()
        
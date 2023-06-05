#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: hami mohsen
"""

import socket

#define default parameter to establish a tcp connection 
IP = socket.gethostbyname(socket.gethostname())
PORT = 4455 #default port of connection 
ADDR = (IP, PORT)
SIZE = 4096   #default size of each packet
FORMAT = "utf-8" #file and connection encoding

#this fucntion get data as parameter and return the reversed text 
def proc_data(data):
    temp_data = data.split('\n')
    temp_data.reverse()
    res = ""
    
    for line in temp_data:
        res = res + line + "\n"
    return res  
    

def main():
    # establish a TCP socket connection
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connecting to the server 
    client.connect(ADDR)

    #get filename from input and send that to the server 
    file_name = str(input('-> please enter your file name and directory to send : '))
   # Sending the filename to the server to reterive
    client.send(file_name.encode(FORMAT))
    
    #recieve status of sending file name from server (tcp is reliable !)
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"-> [SERVER]: {msg}")

    #recieve data from server 
    data = client.recv(SIZE).decode(FORMAT)
    
   #reverse data using function and write to the file 
    proc_data(data)
    f = open(file_name, "w")
    f.write(proc_data(data))
    print("-> data received and write in file successfully !! ")
    
    
    f.close()
    client.close()


if __name__ == "__main__":
    main()
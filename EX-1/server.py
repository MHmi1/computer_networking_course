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

#this function split file line by line and return data
def extract_data(filename):
    data = ""
    
    with open(filename) as file:
        for line in file:
            data = data + line.rstrip() + "\n"
    return data
        
            
def main():
    print("-> Server is starting.")
    # establish a TCP socket conection
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind IP and PORT to server """
    server.bind(ADDR)

    #Server is listening
    server.listen()
    print("-> Server is listening.")

    while True:
        #Server has accepted the connection from the client 
        conn, addr = server.accept()
        print(f"-> [NEW CONNECTION] {addr} connected.")

        # Receiving the filename from the client
        filename = conn.recv(SIZE).decode(FORMAT)
        
        print(f"[RECV] filename recieved from client ! " )
        
        
        #send data of requested file to the client
        conn.send("Filename received .".encode(FORMAT))
        conn.send(extract_data(filename).encode(FORMAT))
    

        """ Closing  file and socket connection """
        file.close()
        conn.close()
        print(f"-> [DISCONNECTED] {addr} disconnected.")

if __name__ == "__main__":
    main()
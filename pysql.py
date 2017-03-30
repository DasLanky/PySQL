#!/usr/bin/env python2
import mysql.connector
import socket
import thread

#TODO: Implement SSL encryption
#from OpenSSL import SSL

import SocketServer

props = {}
with open('pysql.properties', 'rb') as f:
    for line in f:
        try:
            (key, val) = line.strip().split('=')
            props[key] = val
        except ValueError:
            print("Properties file invalid line")


#Establish connection with port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', int(props['max_connections'])))

#SSL Decryption
def _decrypt(line):
    #TODO: Implement
    return line

#SSL encryption
def _encrypt(line):
    #TODO: Implement
    return line

#Forward-declaration of client handler
def handle_client(client):
    #Establish connection with MySQL
    connection = mysql.connector.connect(
                    user=props['user'],
                    password=props['pass'],
                    host='127.0.0.1',
                    database=props['dbname']
    )
    cursor = connection.cursor()
    #Main loop
    while True:
        line = ""
        while ';' not in line:
            line = line + _decrypt(client.readline())
        cursor.execute(line)
        for line in cursor:
            client.send(_encrypt(line))
        client.send(props['delimiter'])

#Initiate connections with clients
while True:
    (client, address) = server.accept()
    thread.start_new_thread(handle_client, (client))

#Close the MySQL connections
cursor.close()
connection.close()

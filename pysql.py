#!/usr/bin/env python2
import mysql.connector
import socket
import thread

#TODO: Implement SSL encryption
#from OpenSSL import SSL

import SocketServer

from socket import error as socket_error

BUFFER_SIZE = 1

props = {}
with open('pysql.properties', 'rb') as f:
    for line in f:
        try:
            (key, val) = line.strip().split('=')
            props[key] = val
        except ValueError:
            print("Properties file invalid line")

print('Initializing server:')
print('\tHostname: localhost')
print('\tPort: ' + props['server_port'])
print('\tMax connections: ' + props['max_connections'])
print('\tDatabase name: ' + props['dbname'])
print('\tDatabase username: ' + props['user'])

#Establish connection with port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', int(props['server_port'])))
server.listen(int(props['max_connections']))
print('Listening for new connections')

#SSL Decryption
def _decrypt(line):
    #TODO: Implement
    return line

#SSL encryption
def _encrypt(line):
    #TODO: Implement
    return line
    
#Forward-declaration of client reader
def readall(client):
    try:
        data = client.recv(BUFFER_SIZE)
        while ';' not in str(data):
            data = data + client.recv(BUFFER_SIZE)
    except socket.timeout:
        print("Connection timeout")
        return None
    return data

#Forward-declaration of client handler
def handle_client(client, *args):
    #Establish connection with MySQL
    connection = mysql.connector.connect(
                    user=props['user'],
                    password=props['pass'],
                    host='127.0.0.1',
                    database=props['dbname']
    )
    cursor = connection.cursor()
    request = readall(client)
    if request == None:
        cursor.close()
        connection.close()
        return false
    request = _decrypt(request)
    print('Executing command: ' + request)
    cursor.execute(request)
    client_writer = client.makefile(mode='w')
    for l in cursor:
        print(str(l))
        client_writer.write(_encrypt(str(l)))
    client_writer.write(props['delimiter'])
    client_writer.flush()
    client.close()
    #Close the MySQL connections
    cursor.close()
    connection.close()

#Initiate connections with clients
try:
    while True:
        (client, address) = server.accept()
        print('New client:', address)
        thread.start_new_thread(handle_client, (client, 1))
except socket_error as serr:
    if serr.errno != errno.ECONNREFUSED:
        raise serr

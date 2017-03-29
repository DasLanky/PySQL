#!/usr/bin/env python2
import mysql.connector

#TODO: Implement SSL encryption
#from OpenSSL import SSL

import SocketServer

props = {}
with open('pysql.properties', 'rb') as f:
    props = dict(map(str.strip, line.split(':', 1)) for l in f.splitlines())

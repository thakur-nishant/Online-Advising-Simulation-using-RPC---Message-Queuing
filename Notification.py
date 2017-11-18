'''
TCP Client - Nishant Thakur
University of Texas at Arlington - UID: 1001544591
RPC server implementation from: https://docs.python.org/3/library/xmlrpc.server.html#module-xmlrpc.server
'''
import xmlrpc.client
from time import sleep

#connect to the RPC server
s = xmlrpc.client.ServerProxy('http://localhost:8000')

#check the queue continiously for available advisor response
while True:
    print(s.notification_process())
    sleep(7)

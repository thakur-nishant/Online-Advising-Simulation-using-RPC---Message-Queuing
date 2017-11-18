'''
TCP Client - Nishant Thakur
University of Texas at Arlington - UID: 1001544591
RPC server implementation from: https://docs.python.org/3/library/xmlrpc.server.html#module-xmlrpc.server
'''
import xmlrpc.client
from time import sleep
import random

#connect to the RPC server
s = xmlrpc.client.ServerProxy('http://localhost:8000')

#check the queue continiously for available student request
while True:
    #RPC function call to check for student request in the queue
    req = s.advisor_queue_check()
    print(req)
    if req != "no message found" and req != "":
        decision = random.choice([True, False])
        if (decision):
            advise = 'Approved'
        else:
            advise = 'Not Approved'

        # print(req[0],req[1],advise)
        #RPC function call to append the advisor decision to the queue
        s.advisor_response(req,advise)
    sleep(3)



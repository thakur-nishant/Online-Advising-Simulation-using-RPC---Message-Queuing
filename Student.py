'''
TCP Client - Nishant Thakur
University of Texas at Arlington - UID: 1001544591
RPC server implementation from: https://docs.python.org/3/library/xmlrpc.server.html#module-xmlrpc.server
'''
import xmlrpc.client

#connect to the RPC server
s = xmlrpc.client.ServerProxy('http://localhost:8000')

#ask user to input their name and course they need approval of
while True:
    student_name = input("Please enter your name: ")
    course = input("Please enter course name: ")
    #RPC function call to append the student request in the queue
    print(s.seek_clearence(student_name, course))



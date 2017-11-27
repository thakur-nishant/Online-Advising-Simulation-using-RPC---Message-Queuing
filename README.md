# Online Advising Simulation using RPC & Message Queuing
Project Specification:
In this lab you will simulate an online advising system which is similar to what you might
have used for registering your classes. Students request clearance for a course from the
adviser. At some other time the adviser approves or disapproves the request and then
the student is notified of the adviser’s decision. You will require 4 processes to simulate
this: a student process, an adviser process, a notification process and a message
queuing server (MQS). The student process, adviser process and notification process
communicate through the message queuing server (message oriented middleware).
Communication from these processes to the message queuing server is through remote
procedure calls.

'''
TCP Client - Nishant Thakur
University of Texas at Arlington - UID: 1001544591
RPC server implementation from: https://docs.python.org/3/library/xmlrpc.server.html#module-xmlrpc.server
'''
import threading
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import json
import collections

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler, allow_none=True)
server.register_introspection_functions()

print("RPC Server Start")

#initiating the queue from the file
queue = {}
queue = collections.defaultdict(dict)

with open("data.json","r") as f:
    queue = json.load(f)
f.close()

#lock on queue for mutual exclusion
queue_lock = threading.Lock()

print("Current queue:", queue)

#classes containing all the RPC functions
class RPCfunctions:

    #function to add student request to the queue
    def seek_clearence(self, student_name, course):
        with queue_lock:
            new_student = {'name': student_name, 'course': [course]}
            if 'student_request' in queue:
                if not queue['student_request']:
                    queue['student_request'].append(new_student)
                else:
                    for i in range(len(queue['student_request'])):
                        if queue['student_request'][i]['name'] == student_name:
                            queue['student_request'][i]['course'].append(course)
                            break
                        else:
                            queue['student_request'].append(new_student)
            else:
                queue['student_request'] = [new_student]
            with open('data.json', 'w') as f:
                json.dump(queue, f)
            f.close()
            print(queue)
            return "Requested Clearence for "+course

    #function to check the students request pending in the queue
    def advisor_queue_check(self):
        with queue_lock:
            print("Current queue:", queue)
            request = 'no message found'
            if 'student_request' in queue:
                if not queue['student_request']:
                    del queue['student_request']
                    return request
                else:
                    if not queue['student_request'][0]['course']:
                        del queue['student_request'][0]
                        with open('data.json', 'w') as f:
                            json.dump(queue, f)
                        f.close()
                        return request
                    else:
                        request = queue['student_request'][0]['course'][0]
                        del queue['student_request'][0]['course'][0]
                        with open('data.json', 'w') as f:
                            json.dump(queue, f)
                        f.close()
                        return (queue['student_request'][0]['name'], request)
            else:
                return request

    #function to append advisor response to a student request in a queue
    def advisor_response(self,details,advise):
        with queue_lock:
            if 'advisor_response' in queue:
                queue['advisor_response'].append([details,advise])
            else:
                queue['advisor_response'] = [[details,advise]]
            with open('data.json', 'w') as f:
                json.dump(queue, f)
            f.close()

    #function to check for available advisor response available in the queue
    def notification_process(self):
        with queue_lock:
            print("Current queue:", queue)
            request = 'no message found'
            if 'advisor_response' in queue:
                if not queue['advisor_response']:
                    del queue['advisor_response']
                else:
                    request = queue['advisor_response'][0]
                    del queue['advisor_response'][0]
                    # if 'notify' in queue:
                    #     queue['notify'].append(request)
                    # else:
                    #     queue['notify'] = [request]
                with open('data.json', 'w') as f:
                    json.dump(queue, f)
                f.close()
            return(request)

#register all the functions in the class RPCfunctions on the server
server.register_instance(RPCfunctions())

# Run the server's main loop
server.serve_forever()

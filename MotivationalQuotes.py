import zmq
import random

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

def getQuotes(quantity, category):
    return "Test Test"

while(True):
    message = socket.recv()
    if(len(message)>0):
        s = message.decode().split()
        quantity = s[0]    
        category = "random"
        
        if len(s) > 1:
            category = s[1]
            
        quote = getQuotes(quantity, category)
        socket.send_string(quote)
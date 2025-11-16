import zmq
import time
context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

def Get_Quote(quantity, category):
    time.sleep(1)
    socket.send_string(f"{quantity} {category}")
    recieved = socket.recv_multipart()
    quoteArray = [frame.decode('utf-8') for frame in recieved]
    return quoteArray

while True:
    q = input("choose quantity of quotes: ")
    c = input("choose category of quote(or random): ")
    quotes = Get_Quote(q, c)
    print(f"Received: {quotes}")
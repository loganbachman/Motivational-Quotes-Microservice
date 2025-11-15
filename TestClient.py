import zmq
import time
context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

def get_quote(quantity, category = "random"):
    time.sleep(1)
    socket.send_string(f"{quantity} {category}")
    quoteArray = socket.recv()
    return quoteArray

while True:
    q = input("choose quantity of quotes: ")
    c = input("choose category of quote(or random): ")
    noun = get_quote(q, c)
    print(noun)
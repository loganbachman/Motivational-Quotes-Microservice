import zmq
import random

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

with open("Music.txt", 'r') as f: musicQuotes = f.readlines()
with open("Pets.txt", 'r') as f: petsQuotes = f.readlines()
with open("School.txt", 'r') as f: schoolQuotes = f.readlines()
with open("Sports.txt", 'r') as f: sportsQuotes = f.readlines()
with open("Games.txt", 'r') as f: GamesQuotes = f.readlines()

def Get_Quote(category):
    
    if(category == ""):
        rand = random.randint(0,4)
        category = rand
    else:
        category = category.lower()
    
    if(category == "music" or category == 0):
        quotes = musicQuotes
    elif(category == "pets" or category == 1):
        quotes = petsQuotes
    elif(category == "school" or category == 2):
        quotes = schoolQuotes
    elif(category == "sports" or category == 3):
        quotes = sportsQuotes
    elif(category == "video games" or category == 4):
        quotes = GamesQuotes
    else:
        quotes = GamesQuotes
    return random.choice(quotes).strip()

def Get_Quotes(quantity, category):
    quotes = []
    if(category == ""):
        for ii in range(int(quantity)):
            quotes.append(Get_Quote(""))
    else:
        for ii in range(int(quantity)):
            quotes.append(Get_Quote(category))


    return quotes

while(True):
    message = socket.recv()
    if(len(message)>0):
        s = message.decode().split()
        quantity = s[0]    
        category = "random"
        
        if len(s) > 1:
            category = s[1]
            quotes = Get_Quotes(quantity, category)
        else: 
            quotes = Get_Quotes(quantity, "")
        socket.send_multipart([l.encode('utf-8') for l in quotes])
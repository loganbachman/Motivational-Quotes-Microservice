import zmq
import random

#setup ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

#load in each file and save each files contents
with open("Music.txt", 'r') as f: musicQuotes = f.readlines()
with open("Pets.txt", 'r') as f: petsQuotes = f.readlines()
with open("School.txt", 'r') as f: schoolQuotes = f.readlines()
with open("Sports.txt", 'r') as f: sportsQuotes = f.readlines()
with open("Games.txt", 'r') as f: GamesQuotes = f.readlines()

#This function is responsible for determining which quote category to pull a quote from and returning a random quote
def Get_Quote(category):
    #logic for a random category
    if(category == ""):
        rand = random.randint(0,4)
        category = rand
    else:
        category = category.lower()
    
    #select the category to pull from
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
    
    #Return a random quote from the category selected
    return random.choice(quotes).strip()

#This makes the list of quotes to send back to the user
def Get_Quotes(quantity, category):
    quotes = []
    if(category == ""):
        #random category
        for ii in range(int(quantity)):
            quotes.append(Get_Quote(""))
    else:
        #user defined category
        for ii in range(int(quantity)):
            quotes.append(Get_Quote(category))
    return quotes

while(True):
    #get the message from the user
    message = socket.recv()
    if(len(message)>0):
        s = message.decode().split()
        quantity = s[0]    
        #default category is random to handle the case that the user does not provide a category
        category = "random" 
        
        if len(s) > 1:
            #get the list of quotes in the selected category
            category = s[1]
            quotes = Get_Quotes(quantity, category)
        else:
            #get a list of quotes in a random category 
            quotes = Get_Quotes(quantity, "")
            
        #encode the list and send it back to the user
        socket.send_multipart([l.encode('utf-8') for l in quotes])
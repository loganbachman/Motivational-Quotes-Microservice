import zmq
import random

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

# Load files 
with open("Music.txt", 'r') as f: musicQuotes = f.readlines()
with open("Pets.txt", 'r') as f: petsQuotes = f.readlines()
with open("School.txt", 'r') as f: schoolQuotes = f.readlines()
with open("Sports.txt", 'r') as f: sportsQuotes = f.readlines()
with open("Games.txt", 'r') as f: gamesQuotes = f.readlines()

# Dictionary fcategory 
categories = {
    "music": musicQuotes,
    "pets": petsQuotes,
    "school": schoolQuotes,
    "sports": sportsQuotes,
    "video games": gamesQuotes
}

# Return random quote from given category
def get_quote(category):
    category = category.lower()

    if category == "" or category == "random":
        category = random.choice(list(categories.keys()))

    quotes = categories.get(category, gamesQuotes)  
    return random.choice(quotes).strip()

# Return list of quotes given quantity and category.
def get_quotes(quantity, category):
    return [get_quote(category if category else "") for _ in range(int(quantity))]

while True:
    message = socket.recv()

    if len(message) > 0:
        parts = message.decode().split()
        quantity = parts[0]
        category = parts[1] if len(parts) > 1 else ""

        quotes = get_quotes(quantity, category)

        # Print each quote separately
        socket.send_multipart([q.encode('utf-8') for q in quotes])

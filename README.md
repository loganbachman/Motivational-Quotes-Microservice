Local mircroservice where the client can request random motivational quotes from using ZeroMQ implemented in python.
The user can request a random quote from a category (Video Games, Music, Pets, School, Sports), or from a random category

Once sockets are bound/connected on port 5555, you can request and recieve data from the random motivational quote generation microservice.

**To request data send a string message:** 
<br>
socket.send_string(f"{quantity} {category}")
<br>
Where quantity is an integer and category is one of the following categories: Video Games, Music, Pets, School, Sports.
If the second argument is left blank then the category will be randomized or if the category is not valid it will default to Video Games

**To recieve data:**
<br>
recieved = socket.recv_multipart()
quote_list = [frame.decode('utf-8') for frame in recieved]
<br>
recieved is a variable to hold the un decoded data from the socket. and quote_list is an array that will hold the quotes once they have been
converted back into a string array

**Example request (Python):**
<br>
socket.send_string("2 Music")
<br>
**Example request with random category:**
<br>
socket.send_string("1")
<br>
**Example receiving code:**
<br>
received = socket.recv_multipart()
quote_list = [frame.decode('utf-8') for frame in received]
<br>
**Example output:**
<br>
['"Music gives a soul to the universe."', '"Feel the rhythm, own the day."']
<br>
**How to Run**

1. Start the microservice
<br>
python motivational_quote_service.py
<br>
2. Run the test client:
<br>
python test_client.py
<br>
**Provided UML Diagram to show ZeroMQ request flow**
<img width="1189" height="606" alt="Screenshot 2025-11-16 at 1 05 47 PM" src="https://github.com/user-attachments/assets/51525a42-01d9-4b0c-9870-a86d8bd48387" />

Local mircroservice where the client can request random motivational quotes from using ZeroMQ implemented in python.
The user can request a random quote from a category (Video Games, Music, Pets, School, Sports), or from a random category

Once sockets are bound/connected on port 5555, you can request and recieve data from the random motivational quote generation microservice.

To request data send a string message: 
    socket.send_string(f"{quantity} {category}")
where quantity is an integer and category is one of the following categories: Video Games, Music, Pets, School, Sports.
If the second argument is left blank then the category will be randomized or if the category is not valid it will default to Video Games

To recieve data: 
    recieved = socket.recv_multipart()
    quote_list = [frame.decode('utf-8') for frame in recieved]
recieved is a variable to hold the un decoded data from the socket. and quote_list is an array that will hold the quotes once they have been
converted back into a string array

Example test client is included
import socket
import random

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

port = random.randint(10000, 20000)

# Bind to the port
s.bind((host, port))

# get host:port from user
print ('Enter host:port')
host_port = input()

# connect to server
s.connect((host_port.split(':')[0], int(host_port.split(':')[1])))

messages = []

while True:
    # clear screen
    print ('\n'*100)
    # print all messages
    for message in messages:
        print (message.decode("utf-8"))

    # get message from user
    message = input()

    if message != ".":
        # send message to server
        s.send(message.encode())

    # get messages from server
    s.send(b'[$get]')
    data = s.recv(1024)

    # add messages to list
    messages = eval(data)

    # #if keyboard interrupt quit
    # if 





s.close()



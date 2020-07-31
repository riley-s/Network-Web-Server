from socket import *
#To terminate the program
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort = 12000
#Assign port number to the socket
serverSocket.bind(('', serverPort))
#Server awaits for TCP connection request from the client
serverSocket.listen(1)
#Fill in end

while True:
    # Establish a connection
    print("Ready to server...")
    # Fill in start
    # Accept method: new socket created in the server, unique to the client address
    connectionSocket, addr = serverSocket.accept()
    print("Connected to ", addr)
    # Fill in end
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Send one HTTP header line into socket
        # Fill in start
        status = "HTTP/1.1 200 Ok\r\n"
        header = "Connection: Closed\r\n"
        connectionSocket.send(status.encode())
        connectionSocket.send(header.encode())
        connectionSocket.send("\r\n".encode())
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        error = "HTTP/1.1 404 Not Found\r\n"
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.send(error.encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
        #Fill in end
serverSocket.close()
#Terminate the program after sending the corresponding data
sys.exit()


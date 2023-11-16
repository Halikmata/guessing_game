import socket

def client_initialization():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientHost = '192.168.1.7'
    clientPort = 6969

    clientSocket.connect((clientHost, clientPort))
    print("Connection to server is established")

    while True:
        guess = input("Guess the random from 1 to 100: ")
        clientSocket.send(guess.encode())

        response = clientSocket.recv(1024).decode()
        print(response)

        if "Great" in response:
            break

    clientSocket.close()


client_initialization()
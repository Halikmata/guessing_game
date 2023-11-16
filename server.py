import socket
import random

def server_initialization():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverHost = '192.168.1.7'
    serverPort = 6969
    serverSocket.bind((serverHost, serverPort))
    serverSocket.listen(1)

    secret_number = random.randint(1, 100)
    attempts = 0

    print(f"Server listening on {serverHost}:{serverPort}" "\nRandom number is", secret_number)

    conn, addr = serverSocket.accept()
    print(f"Connection from {addr}")



    while True:
        guess = int(conn.recv(1024).decode())
        attempts += 1

        if guess == secret_number:
            if attempts == 1:
                message = f"Great job! the random number is {secret_number} and you guesed it in a single try."
                conn.send(message.encode())
                break
            else:
                message = f"Great job! the random number is {secret_number} and you guesed it in {attempts} attempts."
                conn.send(message.encode())
                break
        elif guess < secret_number:
            conn.send(b"Higher")
        else:
            conn.send(b"Lower")

    conn.close()
    serverSocket.close()


server_initialization()
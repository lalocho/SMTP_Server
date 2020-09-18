from socket import *
import base64



def main():
    # Assigning values to all my variables such as server, credentials, message, subject etc.
    # prints every response received
    """Must fill in username,password, and destination: replace brackets with appropriate info"""

    server = ("smtp.utep.edu",25)
    subject = "Subject: Email from my email client\r\n\r\n"
    body = "\r\n This is a test email from my own email client. Hope it finds you well. Ochoa,Luis"
    end_string = "\r\n.\r\n"
    username = "<>"
    origin = "MAIL FROM:" + username + "\r\n"
    password = "<>"
    destination = "RCPT TO:<>\r\n"
    data_command = "DATA\r\n"
    quit = "QUIT\r\n"

    #initiating and connecting socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(server)
    print(clientSocket.recv(1024).decode())

    # sending hello command
    hello_command = 'EHLO test\r\n'
    clientSocket.send(hello_command.encode())
    print(clientSocket.recv(1024).decode())

    #encoding message to base64
    credentials = ("\x00" + username + "\x00" + password).encode()
    credentials = base64.b64encode(credentials)
    authentication = "AUTH PLAIN ".encode() + credentials + "\r\n".encode()
    clientSocket.send(authentication)
    print(clientSocket.recv(1024).decode())

    # sending origin email
    clientSocket.send(origin.encode())
    print(clientSocket.recv(1024).decode())

    # sending destination email
    clientSocket.send(destination.encode())
    print(clientSocket.recv(1024).decode())

    # sending data command to input subject and body
    clientSocket.send(data_command.encode())
    print(clientSocket.recv(1024).decode())

    # sending subject
    clientSocket.send(subject.encode())

    # sending message body
    clientSocket.send(body.encode())

    # sending end of line to signal end of message
    clientSocket.send(end_string.encode())
    print(clientSocket.recv(1024).decode())

    # quitting the socket
    clientSocket.send(quit.encode())
    print(clientSocket.recv(1024).decode())
    clientSocket.close()




main()
#!/usr/bin/python3
import socket
import base64
import re

# Define the host and port
HOST = 'chal.pctf.competitivecyber.club'
PORT = 9001

# Create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))
    decoded_data = ""

    while True:
        # Receive data from the server
        data = s.recv(1024)
        if not data:
            break  # Exit loop if no data is received
        decoded_data += data.decode('utf-8')

        # Break if the received data ends with '>>'
        if decoded_data.endswith(' >> '):
            print(decoded_data + "\n")
            match = re.search(r'Challenge:\s*(.*)', decoded_data)
            match2 = re.search(r"\((\d+)/1000\)", decoded_data)
            if match and match2:
                # print(match.group(1))
                challenge_iteration = match2.group(1)
                encoded_string = match.group(1)
                decoded_string = base64.b64decode(encoded_string).decode('utf-8')
                challenge, n = decoded_string.split("|")
                n = int(n)
                # print('decoded', decoded_string)
                # print('challenge', challenge)
                # print('n', n)
                decoded_string = challenge
                for i in range(n):
                    decoded_string = base64.b64decode(decoded_string).decode('utf-8')
                response = f"{decoded_string}|{challenge_iteration}\n"
                print('response => ', response, "\n")
                s.sendall(response.encode('utf-8'))
                print(decoded_data)
                decoded_data = ""
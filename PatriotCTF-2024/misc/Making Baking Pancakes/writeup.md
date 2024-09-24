# Pancake Shop Challenge

## Analysis
The challenge involves interacting with a server that requires a series of challenge-response pairs. Each challenge is encoded using Base64, and the solution requires multiple layers of decoding to reach the final response. The key steps include:

1. **Socket Communication**: Establishing a TCP connection to communicate with the server.
2. **Data Handling**: Continuously receiving data until the server indicates it’s time to respond.
3. **Regex Parsing**: Extracting the challenge string and the iteration count from the received messages.
4. **Base64 Decoding**: Understanding that the challenge must be decoded multiple times, which requires careful management of the decoding process based on the value of `n`.
5. **Response Formatting**: Ensuring the response is correctly formatted before sending it back to the server.

By following these steps, the code automates the process of solving the challenge efficiently.

## Question
Welcome to the pancake shop!  
Pancakes have layers; we need you to get through them all to get our secret pancake mix formula. This server will require you to complete 1000 challenge-responses. A response can be created by doing the following:

1. Base64 decoding the challenge once (will output `(encoded|n)`).
2. Decoding the challenge `n` more times.
3. Send `(decoded|current challenge iteration)`.

Example response for challenge 485/1000: `e9208047e544312e6eac685e4e1f7e20|485`.

Good luck!

## Implementation
```python
import socket
import base64
import re

# Define the host and port
HOST = 'chal.pctf.competitivecyber.club'
PORT = 9001
flag = False
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

        if flag:
              print("hello")
              print(decoded_data + "\n")

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
                if challenge_iteration == '999':
                  flag = True
                # print('decoded', decoded_string)
                # print('challenge', challenge)
                # print('n', n)
                decoded_string = challenge
                for i in range(n):
                    decoded_string = base64.b64decode(decoded_string).decode('utf-8')
                response = f"{decoded_string}|{challenge_iteration}\n"
                print('response => ', response, "\n")
                s.sendall(response.encode('utf-8'))
                decoded_data = ""
```
# flag  
pctf{store_bought_pancake_batter_fa82370}

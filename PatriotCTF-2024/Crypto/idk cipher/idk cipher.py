#In this problem we Have to reverse Decrypt The problem Nothing else

import base64

# Secret key (must match what was used in encryption)
srt_key = 'secretkey'

# Base64-encoded string (this is the output from your encryption)
b64_enc_val = ' QRVWUFdWEUpdXEVGCF8DVEoYEEIBBlEAE0dQAURFD1I='

# Step 1: Decode Base64 to get the XOR-ed string
decoded_val = base64.b64decode(b64_enc_val).decode()

# Step 2: Initialize an array to hold the decrypted characters
n = len(decoded_val) // 2  # Since we have 2 chars per original character pair
output_arr = [''] * (n * 2)  # Create an empty list for output

# Step 3: Decrypt the XOR-ed characters
for i in range(n):
    enc_p1 = decoded_val[2 * i]  # First character in the pair (original)
    enc_p2 = decoded_val[2 * i + 1]  # Second character in the pair (reversed)

    # XOR back with the secret key
    c1 = chr(ord(enc_p1) ^ ord(srt_key[i % len(srt_key)]))
    c2 = chr(ord(enc_p2) ^ ord(srt_key[i % len(srt_key)]))

    # Place characters in their correct positions
    output_arr[i] = c1  # From original part
    output_arr[n + i] = c2  # From reversed part

# Step 4: Combine the characters to form the original input
original_input = ''.join(output_arr)
# Reconstruct the original string
reconstructed_original = ''.join(output_arr[:n] + output_arr[n:][::-1])  # Join original and reversed correctly

print("Decoded original input:", reconstructed_original)

# Flag - pctf{234c81cf3cd2a50d91d5cc1a1429855f}



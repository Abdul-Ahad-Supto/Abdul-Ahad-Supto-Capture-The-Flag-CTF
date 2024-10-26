# ELF File XOR Decryption Challenge Writeup

## Challenge Summary

We were given a file named `root.d`, which appeared to be an ELF (Executable and Linkable Format) file based on initial inspection. However, it was encrypted, so we needed to determine the encryption scheme and decrypt it to extract any hidden information, such as a flag.

## Analysis

1. **Hex Dump Inspection**:
   - Upon examining the hex dump of `root.d`, we noticed a recurring pattern of the ASCII string **`rootkitd`** in the file.
   - The repetition suggested that this string could potentially be the key used to XOR-encrypt the file, as repeating keys are commonly used in simple XOR encryption schemes.

2. **XOR Encryption Scheme**:
   - XOR encryption is a reversible process where each byte of data is XORed with a corresponding byte of the key, cycling through the key repeatedly if it’s shorter than the data.
   - To decrypt this file, we could XOR each byte of `root.d` with the bytes of the key **`rootkitd`**.

3. **Key Selection**:
   - Based on the hex dump pattern, we decided to try **`rootkitd`** as the XOR key.

## Solution Code

Using the Python script below, we decrypted the file:

```python
def xor_decrypt(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    key_len = len(key)
    decrypted = bytearray()
    for i, byte in enumerate(data):
        decrypted.append(byte ^ key[i % key_len])
    return decrypted
key = bytes('rootkitd', 'utf-8')


decrypted_data = xor_decrypt('C:/Users/USER/Downloads/root.d', key)
with open('C:/Users/USER/Downloads/decrypted_file', 'wb') as f:
    f.write(decrypted_data)

```

#### Flag - EWU{7h15_1sn't_f1yL1nG_W1th_ONe_PunCh!}
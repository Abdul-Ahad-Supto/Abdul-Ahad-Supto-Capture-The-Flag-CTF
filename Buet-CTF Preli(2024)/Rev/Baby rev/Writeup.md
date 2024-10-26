# Baby Rev
## Points - 50
If we analyze the chal.c file we can see a secret list with ascii values in it. and it is iterating in a loop for 32 times and it is getting Xor operation everytime. We just have to reverse it

```python
secret = [66, 84, 71, 87, 71, 81, 64, 124, 98, 123, 100,
            125, 106, 75, 58, 64, 87, 35, 106, 106, 81, 38,
            84, 92, 42, 114, 74, 82, 75, 112, 109, 98]
for i in range(32):
    print(chr(secret[i]^i),end = '')
```

#### Flag - BUETCTF{jrnvfF4OG2xyE3BK2kPIWms}
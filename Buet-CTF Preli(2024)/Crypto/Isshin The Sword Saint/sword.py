import random

flag = b'BUETCTF{...}'
flag = flag.lstrip(b'BUETCTF{').rstrip(b'}')
assert all(65 < c < 125 for c in flag)

M = 10**9 + 7
e = 69420

seq = []
for c in flag:
  e = e + random.randint(69, 420)
  o = (c * pow(2, e, M)) % M
  seq.append(o)

random.shuffle(seq)
print(seq)

#[173941810, 858898665, 468848314, 635867560, 633540626, 16418674, 294931476, 461014, 350360176, 294627774, 552498858, 886470836, 828069064, 432658831, 341519287, 320474506, 598269374, 967937144, 418635091, 399599765, 983033996, 703488819, 58442600, 257836528, 241409305, 811247888, 442468084, 199395519, 579859752, 112962212, 816269013, 9496448, 249252133, 927028574]

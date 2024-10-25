# Baby RSA Writeup

## Challenge Summary

We are provided with a netcat (`nc`) server that first gives us values of `n`, `e`, and `c` in multiple rounds. Initially, we observe that the modulus `n` repeats with different values of `e` and `c`, which suggests the feasibility of a **Common Modulus Attack** to decrypt `m`. In the second stage, we are given lists of `d`, `e`, and `n` values, where the challenge shifts to factorizing `n` with limited information, knowing that `d * e - 1` is a multiple of Euler's totient `φ(n)`.

---

## Step 1: Analyzing the Common Modulus Attack (First Stage)

In the first stage, we received the following:
- **Repeated modulus** `n`,
- **Distinct public exponents** `e1, e2, ...`,
- **Encrypted messages** `c1, c2, ...`.

Given the setup of repeated `n` with different `e`, we can apply the **Common Modulus Attack**. This attack is effective when:
1. Two ciphertexts `c1 = m^e1 % n` and `c2 = m^e2 % n` are encrypted with different exponents `e1` and `e2`,
2. The exponents `e1` and `e2` are coprime.

Since `e1` and `e2` are coprime, there exist integers `x` and `y` (which we can find using the Extended Euclidean Algorithm) such that:

```plaintext
x * e1 + y * e2 = 1
```


Then, the message m can be recovered using:

```Python
from math import gcd
from sympy import mod_inverse
from Crypto.Util.number import long_to_bytes

def common_modulus_attack(c1, c2, e1, e2, n):  
   s1 = pow(e1, -1, e2)  
   s2 = int((gcd(e1,e2) - e1 * s1) // e2)  
   temp = pow(c2, -1, n)  
   m1 = pow(c1,s1,n)  
   m2 = pow(temp,-s2,n)  
   return int((m1 * m2) % n)

n = 89906750609138045378375422290157439325099258625792791539345784896310308668385935740486133392911325618918416002243436722693725319505136466478420361211138898094210093941243011676219210986906278275117254144968043448116692766469078638922965139357890672566192973305487001118556781788393193334291134025079195210063
e1, e2 = 30186100823484854094803676560347793119186565207453424228977044626547866724187, 7440623512584203804252565024472400278492826026316933575460676816538719242611
c1, c2 = 9933312215178988947975733554407776105658637920608179673951701892606995477875496575292885825708551650661645373672298258391221860135660717902806201265570855957509602414953626619395921388908783341522376629595234525709631127551549900975165812890273093951596656724861583802033180231413939802400588311091068420910, 13754158076997658030441182424594982920281613024786828217135467176469859048027502383147628290350155145985245011866489500793335370870074951525057896920737686368743090206184087486436421513073953767150085082285427793416534638825093358226728877385106865548034904414271482099365968103123143470610601241001295554745

recovered_message = common_modulus_attack(c1, c2, e1, e2, n)

plaintext = long_to_bytes(recovered_message).decode('utf-8')
print(plaintext)

#text - Reu5e_7he_S3cRe7_f0r_mee3_plzzZ
```
## Step 2: Factorizing n with Knowledge of d * e - 1 (Second Stage)
In the second stage, we were provided with:

Lists of d, e, and n
The condition that d * e - 1 is a multiple of φ(n) (Euler's Totient)
Approach Using d * e - 1 as a Multiple of φ(n)
Since d * e - 1 is a multiple of φ(n), we can express it as:

plaintext
Copy code
k * φ(n) = d * e - 1
where k is an integer.

We can leverage this relationship to factorize n using an approach similar to Pollard's p-1 factorization. Here’s how we do it:

Calculate k * φ(n): Start by setting kphi = d * e - 1.
Extract Factors of n:
Divide kphi by 2 repeatedly until it becomes odd, keeping track of the number of divisions.
Choose random values g and compute y = g^kphi % n.
Repeat the squaring process on y to find non-trivial factors of n using the greatest common divisor (GCD) approach.
Once p and q are identified such that n = p * q, we can verify the factorization.
Solution Code
Here is the Python code used for this factorization method:

```Python
import random
from gmpy2 import gcd

def factor_with_kphi(n, kphi):
    t = 0
    while kphi % 2 == 0:
        kphi >>= 1
        t += 1
    for i in range(1, 101):
        g = random.randint(0, n)
        y = pow(g, kphi, n)
        if y == 1 or y == n - 1:
            continue
        else:
            for j in range(1, t):
                x = pow(y, 2, n)
                if x == 1:
                    p = gcd(n, y - 1)
                    q = n // p
                    return p, q
                elif x == n - 1:
                    continue
                y = x

# Given values of d, e, n
n = 51530719538083190279776974218958853305394626286945059531596230850645827272684022474506736278743830196965568354998953670014176606573473153688450167112506894773054441833769696642734951992777429611688750087965941720336120687481099381901751943289663913925185282131080642343225359731975100835878739200401299846213
e = 13983866038877619230392768645864578139439187242413418243852720214797023914589
d = 50548649095644130305159590569000718356051191102138620584993911324906992584103930803240021195468735721281893120438900787413707875190849793794119414257256693997027973037808858553441901057049410576537896875435280288788118818206971184245876620789582535296709225018977774502056486555632252219826194591664254996789
kphi = d * e - 1

# Factor n using factor_with_kphi
p, q = factor_with_kphi(n, kphi)
print(f"Factors of n: p = {p}, q = {q}")

Values got -
p = 9456115732400167121050028233042696124853931768390933673172809954338020219059037494415397946496945054729006975588731024267801591112418375819558905158532031
q = 7180497332265716977883452973469671723796962853265635015661589616494164352029495164658093084166308397642201782968063334962872040670330165186632917283957797
phi = 67899613790095276463983395688850230579697617395217662723259767951421815773051728227969271588805292515986186245205707221832877209566431192740116181408752539380563680713736544404762881981593167107083912834329564567657191199324551290066950806700272657116805368050538044366580234761381178369770597821295834205880
```
For more information, refer to [Connor McCartney's RSA writeup](https://connor-mccartney.github.io/cryptography/rsa/Refactor-ASIS-quals-2023).

## Conclusion
After obtaining p and q, we verified that p * q = n, proving that our factorization was correct. With the factors of n, we successfully decrypted further messages in the challenge.

![Alt Text](/hi.png)

#### Flag - EWU{Bra!_4RenT_Y0u_th3_CommOn_RSA!_MMKa8bKRdMHvZUpGjl}



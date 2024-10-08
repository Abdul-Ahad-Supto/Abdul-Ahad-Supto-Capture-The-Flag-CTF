# Hard to Implement (Crypto)

## Objective:
The goal is to decrypt an RSA-encrypted message using **Wiener's Attack**. This attack works when the RSA private key `d` is small compared to `n`, specifically when `d < n^0.25`. Given the values of `e`, `n`, and `c` (in hexadecimal), we use the attack to recover `d` and decrypt the ciphertext.

## Approach:

1. **Wiener's Attack** is based on the observation that when `d` is small, the fraction `e/n` has a simple continued fraction expansion, and one of the convergents of this continued fraction gives the correct value of `d`.
   
2. **Step-by-Step Approach**:
    - First, we generate the continued fraction expansion of `e/n`.
    - We then compute the convergents of this continued fraction.
    - For each convergent `(k, d)`, we check if it satisfies the RSA equation `(e * d - 1) % k == 0`.
    - If this is true, we compute the value of `phi(n)` as `(e * d - 1) // k`.
    - We then solve the quadratic equation derived from `phi(n)` to check if it yields valid factors of `n`.
    - If the discriminant is a perfect square, we have found a valid `d` and can decrypt the message.

3. **Decryption**:
    - Once we have `d`, we use the RSA decryption formula `m = c^d % n` to decrypt the ciphertext.
    - The decrypted message is converted from bytes to a readable string format.

## Code:

```python
from sympy import Rational, continued_fraction_iterator
from sympy.ntheory.continued_fraction import continued_fraction_convergents
from Crypto.Util.number import long_to_bytes
import math


def wiener_attack(e, n):
    # Generate continued fraction expansion of e/n
    cf = list(continued_fraction_iterator(Rational(e, n)))
    convergents = continued_fraction_convergents(cf)

    for conv in convergents:
        k, d = conv.p, conv.q
        if k == 0 or d == 0:
            continue

        # Test if the current convergent (k, d) works
        if (e * d - 1) % k == 0:
            phi_n = (e * d - 1) // k
            b = n - phi_n + 1
            discriminant = b * b - 4 * n

            if discriminant >= 0:
                # Use math.isqrt() to compute integer square root
                sqrt_discriminant = math.isqrt(discriminant)
                if sqrt_discriminant * sqrt_discriminant == discriminant:
                    return d  # Found valid d

    return None


def decrypt_rsa(c, d, n):
    return long_to_bytes(pow(c, d, n))


n = 20305605772088142254079724960884486005748847015497427301575410293505817279910746556529376931600618579467120276350191887301067237559338164615341364063895698445198450602100622547416422520569435203138576780851363672762744455872440594076326813879006337922017621673305730465334708327073147244529163919113400850500409784670385009784210553996344093407282702258367726551292949276478302283365758654388095557202147107693063638232912598498439805960866571776128157562869249540687561326901969851229705248157494412716795536617485874928328884253043159166953971992309846319441730059436713807550503780907287938041242764808454486287023
e = 11482685017819657772146196533057795733473449629855289693100164822097723844966138177362511509772380353831218660693991845555704097147035306958570110974439828105301049643719991559075905686792619567403740919201379127416674307003242767236082047328240271052874236417166735391996411110944467555336448767975263755538261304581405836813138939268114431131030122076716110715178499142704121740475206968272546304252509000120167141777229963404829961350506433927568085505890377296146907922613025051900945495785850823000233847703348763563935446095561235796206511113603398775388472794084369294787467785140078624603886943660133858662073
c = 14531665134114167100979837826752342028891450735196995677636357769295865614666559933494564785156988282683425867538070343091701676024659802732068652721583634562927719841530261965002797455986557324485535150988712817607148213596012867495441913039874954586582711201328787601881545464712275113969203389652205083501245059792154793119468153650644663596094313386931963669611066891546631181901326785976138953854826637304180664070190483908587086086528278431012978756396240661945644492612350098787059899072364888105545382998691878881197718078741483487137826986723167593340766546454020829394951911243295040065262047943870970224586

d = wiener_attack(e, n)
if d:
    m = decrypt_rsa(c, d, n)
    print("Decrypted message:", m)
else:
    print("Wiener's attack failed.")
```

# flag 
pctf{fun_w1th_l4tt1c3s_f039ab9}





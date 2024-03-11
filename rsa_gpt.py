import secrets
from sympy import randprime,mod_inverse
bits = 1024
max_value = 1 << bits
while True:
    p = secrets.randbelow(max_value)
    if p > (1 << (bits - 1)) and sympy.isprime(p):
        break
while True:
    q = secrets.randbelow(max_value)
    if q > (1 << (bits - 1)) and sympy.isprime(q) and q != p:
        break

# 其他部分和之前一样
n = p * q
phi = (p - 1) * (q - 1)
e = 65537
d = mod_inverse(e, phi)
public_key = (e, n)
private_key = (d, n)
# 更改字符串为 'hello SecretRSA'
message = int.from_bytes('hello SecretRSA'.encode(), 'big')
cipher = pow(message, *public_key)
decrypted_message_int = pow(cipher, *private_key)
decrypted_message = decrypted_message_int.to_bytes((decrypted_message_int.bit_length() + 7) // 8, 'big').decode()
print(decrypted_message)  # Should print 'hello SecretRSA'
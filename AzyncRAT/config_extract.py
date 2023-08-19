import base64
from Crypto.Cipher import AES
from Crypto. Protocol import KDF
import hashlib
import hmac
:def unpad (s):
return s[:-ord(s[len(s)-1:])]
1 def decrypt (enc):
:
enc base64.b64decode(enc)
password= base64.b64decode("W1h0cU9mc@E3SVFcEt1Y3F4d1BkZTRMTk1vZ1A5aWY=");
salt b'\xbf\xeb\x1e\x56\xfb\xcd\x97\x3b\xb2\x19\x02\x24\x30\xa5\x78\x43\x00\x3d\x56\x44\xd2\x1e\x62\xb9\xd4\xf1\x80\xe7\xe6\xc3\x39\x41'
iteration 50000
stream hashlib.pbkdf2_hmac("shal", password, salt, iteration, dklen = 100)
aeskey stream[:32]
sha256key
HMACObject = hmac.new(sha256key, msg=enc [32:len (enc)-32], digestmod-hashlib.sha256)
memoryStream = HMACObject.hexdigest()
array2
memoryStream[:32]
iv memoryStream[32:48]
: enc = [
encrypted_text= bytes (memoryStream[48:], 'utf-8')
plain AES.new(aeskey, AES.MODE_CBC, bytes (iv, 'latin-1'))
plain_text= unpad (plain.decrypt (enc))
return plain_text[48:]
stream[:64]
"4a9ZqHKZkTfiFJw/8WmPBxdUb+nPksHtwUKTtgbelcOpOy4B6uq09NS0zJ/qypqsAddyxoVm5+iymVTT76eAKw==",
"Ejgp6w/dezOflunbQ5Lp5b7nWNs14WrOmQYkkfqX54SjnQVp+YgLe04AXNpVY1QjFgc+r84uBHUt CM4VUN90hs EXP9Q0HU1PpDFY3V9bpBU=",
"Ls0S8YGwH7/Hm+MEC16hdHRRUs511m7AFv4481zJ/nRYVWDdhUL1ZCWDphevd5b8PsDB5TsoPlqQVPubQVFZTKR/T5z8PyzqFMy69bYnrro=",
"d5Uxv4V5tZ6hAassIslkujm@oaj4crqcMEGJMYLHP1hLFKaO/1LMXyxLgBoB+ukRBvKFpEsN54PPa4hBBncGtQ==",
"W1h0cU9mc@E3SØVFcEt1Y3F4d1BkZTRMTk1vZ1A5aWY=",
"BaJ7AutgbpVXC7tjNS/XEzsoTCGUFXjoasdx3wuN4Bru3qJJWFUQmwGwL9WvJRuvrrcLO/q1jqnnbA6U9fhGgxJepIIx9BOUZwKjNay4TPA=",
"ytP6rvJbKfBoj5c6XP5z9i92r2FucWBBP/RL3aRPm6xdE4B1+EdE5yfEmj2qgAWqL0rBb1LgDTh7mmyTzUgDIw==",
"+8s138Ad3CuVaqULnzpyKf1N15E9VAT@a5NMAdTNTzXiDQ+gOvBgENQD1R8UxTRODZV1gIvtaXZWAN181Qh7dQ==",
"ArRiXtpKLLtizlaybLe8TYqov60K7Jlt/+xT@CrVXWN1TeyMVulad+A3y2i6w4s4EB8V3oc9MKCn5rdNMhUPCg==",
"bWQ5k1K+e7KXi3zd3rzTXyez5hqWo/t5J1VmmaS8seciN402TZLN7g4PMa7vliwAUL4q+tUenZQUofTn8iQEiA==",
"fndKvVmfc7NySO/mFUKB6Dtf9TPWDtV51hd00gSS24ZXiiTKUxHXalAs ESG65q9tC+nyIckUaIz1XstOBF6C1Q=="
]
for i in enc:
decrypted_text decrypt(i);
print (decrypted_text)
b'8808'
b'josemonila.ddnsfree.com'
b' Edit 3LOSH RAT'
b'false'
b'AsyncMutex_65180kPnk'
b'false'
b'true'
b'null'
b'false'
b'Default'

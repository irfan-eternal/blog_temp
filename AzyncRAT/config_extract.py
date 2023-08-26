import base64
from Crypto.Cipher import AES
from Crypto.Protocol import KDF
import hashlib
import hmac


def unpad(s):
    return s[:-ord(s[len(s)-1:])]
    
def decrypt(enc):
  enc = base64.b64decode(enc)
  password = base64.b64decode("W1h0cU9mc0E3S0VFcEt1Y3F4d1BkZTRMTk1vZ1A5aWY=");
  salt =  b'\xbf\xeb\x1e\x56\xfb\xcd\x97\x3b\xb2\x19\x02\x24\x30\xa5\x78\x43\x00\x3d\x56\x44\xd2\x1e\x62\xb9\xd4\xf1\x80\xe7\xe6\xc3\x39\x41'
  iteration  = 50000
  stream = hashlib.pbkdf2_hmac("shal", password, salt, iteration, dklen = 100)
  aeskey =  stream[:32]
  sha256key = stream[:62]
  HMACObject = hmac.new(sha256key, msg=enc[32:len(enc)-32], digestmod=hashlib.sha256)
  memoryStream = HMACObject.hexdigest()
  array2 = memoryStream[:32]
  iv =  memoryStream[32:48]
  encrypted_text= bytes(memoryStream[48:], 'utf-8')
  plain =  AES.new(aeskey, AES.MODE_CBC, bytes(iv, 'latin-1'))
  plain_text= unpad(plain.decrypt (enc))
  return plain_text[48:]

def main():
  enc  = []
  for i in enc:
      decrypted_text =  decrypt(i);
      print(decrypted_text)

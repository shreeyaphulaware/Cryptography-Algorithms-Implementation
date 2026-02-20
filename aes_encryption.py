from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)

data = b"Hello Cryptography"
ciphertext, tag = cipher.encrypt_and_digest(data)

print("Encrypted:", base64.b64encode(ciphertext))

cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
plaintext = cipher_dec.decrypt(ciphertext)

print("Decrypted:", plaintext.decode())
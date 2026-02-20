from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
public_key = key.publickey()

cipher = PKCS1_OAEP.new(public_key)
message = b"Secure Message"

ciphertext = cipher.encrypt(message)
print("Encrypted:", ciphertext)

decrypt_cipher = PKCS1_OAEP.new(key)
plaintext = decrypt_cipher.decrypt(ciphertext)

print("Decrypted:", plaintext.decode())
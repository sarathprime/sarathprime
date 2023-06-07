import rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import ARC2
from Crypto.Hash import MD2
import Crypto
from Crypto.PublicKey import RSA

publicKey, privateKey = rsa.newkeys(2048)
message = "hiii this is sarath"

    # message = ["mahesh", "ram","20000"]
encMessage = rsa.encrypt(message.encode(), publicKey)

print("original string: ", message)
print("encrypted string: ", encMessage)




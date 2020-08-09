print ('Welcome')
import random
for i in range(1):
  keygen = (random.randint(11111111111, 999999999999999))
print ("")
message=input ('Enter message you want to decrypt:')
alphabet="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "
key = input("Encryption Key:")
encrypt =''
for i in message:
  position=alphabet.find(i)
  newposition=(position+ -int(key) )%94
  encrypt+=alphabet [newposition]
output = (encrypt)
keyout = (keygen)
print ('Decrypted message: '+ (output) )

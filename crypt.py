#This is a program that helps the user to encrypt or decrypt a message by using the Cesar Cipher or the Vigenere Cipher.
ALPHABET="abcdefghijklmnopqrstuvwxyz"

def coder(message_to_code,offset_by_user):
  #print("----Welcome to Cesar Cipher encoder----")
  code=""
  for char in message_to_code:
    coder_alphabet_index=(ALPHABET.find(char)-offset_by_user)%26
    letter=ALPHABET[coder_alphabet_index]
    if char == "!":
      code=code+"!"
    elif char == ".":
      code=code+"."
    elif char == "?":
      code=code+"?"
    elif char == ",":
      code=code+","
    elif char == " ":
      code=code+" "
    else:
      code=code+letter
  return print(f" Your encrypted message is {code} ,with an offset of {offset_by_user}.")


def decoder(message,offset):
  pass
  decode=""
  for char in message:
    alphabet_index=(ALPHABET.find(char)-offset)%26
    letter=ALPHABET[alphabet_index]
    if char == "!":
      decode=decode+"!"
    elif char == ".":
      decode=decode+"."
    elif char == "?":
      decode=decode+"?"
    elif char == " ":
      decode=decode+" "
    elif char == ",":
      decode=decode+","
    else:
      decode=decode+letter
  print(f" Your encrypted message is {decode} ,with an offset of {offset}.")

def no_offset(message):
  for i in range(0,26):
    #print(i)
    code=""
    for char in message:
      code_index=(ALPHABET.find(char)+i)%len(ALPHABET)
      letter=ALPHABET[code_index]
      #code=code+letter
      if char == "!":
        code=code+"!"
      elif char == ".":
        code=code+"."
      elif char == "?":
        code=code+"?"
      elif char == " ":
        code=code+" "
      elif char == "'":
        code=code+"'"
      elif char == ",":
        code=code+","

      code=code+letter
    print(f"Offset:{i}\n{code}")

def vigenere_encryption(message,key):
  cipher=""
  counter=0
  for char in message:
    if char in ALPHABET:
      offset=ord(key[counter])-ord('a')
      #print(offset)
      alphabet_place_index=((ord(char)-ord('a')+offset)%26)
      #print(alphabet_place_index)
      encrypted=chr((alphabet_place_index)+ord('a'))
      #print(encrypted)
  
      cipher=cipher+encrypted
      
      counter=(counter + 1) % len(key)
    else:
      cipher=cipher+char
  print(f"PlainText: {message} Cipher: {cipher}")
 
def vigenere_decryption(cipher,keyword):
  plaintext=""
  length_cipher=0
  for i in cipher:
    if i in ALPHABET:
      shift=ord(keyword[length_cipher])-ord('a')
      #print(shift)
      positive_shift=len(ALPHABET)-shift
      #print(positive_shift)
      decrypted_cipher=chr((ord(i)-ord('a') + positive_shift)% len(ALPHABET)+ord('a'))
      #print(decrypted_cipher)
      plaintext=plaintext+decrypted_cipher
      #print(plaintext)
      length_cipher=(length_cipher+1)%len(keyword)
      #print(length_cipher)
    else:
      print()
  print(f"The cipher was:{cipher}, the decrypted cipher is:{plaintext} ")


def main():
  cipher=input("What cipher would you like to use (c)Caesar Ciper or (v)Vigenere Cipher: ")
  encrypt_decrypt=input("Would you like to (e)encrypt or (d)decrypt a message: ")
  offset=input("Do you have the offset of the message that you would like to decrypt (Yes/No) :")
  
    #code to Caesar Cipher
  if cipher == 'c' and encrypt_decrypt == 'e' and offset == 'Yes':
    print("----Welcome to Caesar Cipher encrypter----")
    message_to_code=input("Enter the message that you would like to code: ")
    offset_by_user=int(input("Offset: "))
    coder(message_to_code,offset_by_user)

    question=input("Would you like to try again? (Yes/No) ")
    if question == 'Yes':
       main()
    else:
       print("Try again soon!")
     
    #decoder Caesar Cipher
  if cipher == 'c' and encrypt_decrypt == 'd' and offset == 'Yes':
    print("----Welcome to Cesar Cipher decrypter----")
    message=input("Enter message:")
    offset=int(input("Offset:"))
    decoder(message,offset)

    question=input("Would you like to try again? (Yes/No) ")
    if question == 'Yes':
      main()
    else:
      print("Try again soon!")
    
    #Caesar cipher without offset
  elif cipher == 'c' and encrypt_decrypt == 'd' and offset == 'No':
    print("----Welcome to Caesar Cipher decrypter----")
    message=input("Enter the mensage that you would like to decrypt: ")
    no_offset(message)

    question=input("Would you like to try again? (Yes/No) ")
    if question == 'Yes':
      main()
    else:
      print("Try again soon!")
   
  #Vigenere encrypter
  elif cipher == 'v' and encrypt_decrypt == 'e' and offset == 'Yes':
    print("----Welcome to Vigenere Cipher encrypter----")
    message=input("Enter the mensage that you would like to encrypt: ")
    key=input("Enter the key: ")
    vigenere_encryption(message,key)

    question=input("Would you like to try again? (Yes/No) ")
    if question == 'Yes':
      main()
    else:
      print("Try again soon!")
    
    #Vigener decrypter
  elif cipher == 'v' and encrypt_decrypt == 'd' and offset == 'Yes':
    print("----Welcome to Vigenere Cipher decrypter----")
    cipher=input("Enter the cipher that you would like to decrypt: ")
    keyword=input("Enter the key: ")
    vigenere_decryption(cipher,keyword)
    question=input("Would you like to try again? (Yes/No) ")
    if question == 'Yes':
       main()
    else:
      print("Try again soon!")

if __name__ == "__main__":
  main()
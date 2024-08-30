print("This is the program for password generation of desired length:")
import random
import string

char= string.ascii_letters+ string.digits+ string.punctuation

def password_gen(length):
    password= " "
    for i in range(0,length):
        password +=random.choice(char)

    return password


length= int(input("Enter the length of your password:"))
password= password_gen(length)

print("The password of desired length is:", password)

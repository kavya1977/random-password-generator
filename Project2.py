
import random
import string
elements=string.ascii_letters+string.digits+string.punctuation
length=int(input("enter the length of the password: "))

password=""

for i in range(length):
    password+=random.choice(elements)
print("your random password is: ", password)
print("\n")

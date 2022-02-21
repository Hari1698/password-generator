import random
import string

print('Hello,welcome to the password generator')

length = int(input("\nEnter the lenght you want="))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower+upper+num+symbols

temp = random.sample(all,length)
password ="".join(temp)

print(password)

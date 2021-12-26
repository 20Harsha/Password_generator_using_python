#It is password generator
#Give input as the number of letters,symbols and numbers you want in your password
#Using that it randomly generates password for you
import random
letters = ['a','b','c','d','e','f','g','h',
           'i','j','k','l','m','n','o','p','q','r','s',
           't','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J',
           'K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['@','!','#','$','%','&','*','+',',']
print("Welcome to the Password Generator!")
a = int(input("How many letters would you like in your password?\n"))
b = int(input("How many symbols would you like?\n"))
c = int(input("How many numbers would you like?\n"))

l = []  #empty list
for i in range(0,a):
    c1=random.choice(letters)  #random selection
    l.append(c1)
for i in range(0,b):
    c2=random.choice(symbols)
    l.append(c2)
for i in range(0,c):
    c3=random.choice(numbers)
    l.append(c3)

random.shuffle(l) #shuffling the list
z = ""
for k in l:
  z+=k
print("Here is your password: ",z)


import random
import string

print('Password Generator!')

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
bothcase = lower + upper
numsym = num + symbols
all = lower + upper + num + symbols

passlen = int(input('\nEnter the length of password: '))
numAsym = input("Do you want to include Numbers & Special Symbols? Y/N or y/n? ")

if (numAsym=="Y" or numAsym=="y"):
    charlen = int(input('\nHow many Alphabetical characters: '))
    NandSpass = "".join(random.sample(numsym,(passlen-charlen)))

elif(numAsym=="N" or numAsym=="n"):
    charlen = passlen
    NandSpass=""

else:
    print("Invalid Input")
    exit()

chcase = input("Uppercase (U or u) Lowercase (L or l) Both (B or b) ")

if (chcase=='U' or chcase=='u'):
    charpass = "".join(random.sample(upper,charlen))

elif (chcase=='L' or chcase=='l'):
    charpass = "".join(random.sample(lower,charlen))

elif (chcase=='B' or chcase=='b'):
    charpass = "".join(random.sample(bothcase,charlen))

else:
    print("Invalid Input")
    exit()

password = charpass + NandSpass
password = "".join(random.sample(password,passlen ))

print("Password is ",password)
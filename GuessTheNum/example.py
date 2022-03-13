from random import randint as r
from time import sleep as s

print("Welcome to game 'Guess the number'!")
s(2)
print('''Thanks you to download this app!
My youtube(Ukranian): https://www.youtube.com/channel/UCxOjkAkRLXGiGs7o9zhyQ1g''')
s(2)
print("Ok, let's play!")
s(2)

# Difficulty choose

print('''
What difficulty are you choose?

1.>>Easy. 2.>>Medium. 3.>>Hard. 4.>>IMPOSSIBLE. 
''')

dif = int(input('Write there (only number) : '))

print("Difficulty choosed successfully!")
s(2)

# Score creating

sc = 0

# Game starting

if dif == 1:
    gn = r(1, 5)
    print("Now you can guess number!")
    n = int(input("Input there : "))
    while n != gn:
        sc = sc + 1
        print("Wrong! Try again!")
        n = int(input("Input there : "))
    print(f"Good job! You guess it after {sc} attempt!")
    s(4)

elif dif == 2:
    gn = r(1, 10)
    print("Now you can guess number!")
    n = int(input("Input there : "))
    while n != gn:
        sc = sc + 1
        print("Wrong! Try again!")
        n = int(input("Input there : "))
    print(f"Good job! You guess it after {sc} attempt!")
    s(4)

elif dif == 3:
    gn = r(1, 20)
    print("Now you can guess number!")
    n = int(input("Input there : "))
    while n != gn:
        sc = sc + 1
        print("Wrong! Try again!")
        n = int(input("Input there : "))
    print(f"Good job! You guess it after {sc} attempt!")
    s(4)

elif dif == 4:
    gn = r(1, 50)
    print("Now you can guess number!")
    n = int(input("Input there : "))
    while n != gn:
        sc = sc + 1
        print("Wrong! Try again!")
        n = int(input("Input there : "))
    print(f"Good job! You guess it after {sc} attempt!")
    s(4)

else:
    print("Error : 'Unknown option'")
    s(2)
    exit()

# Save record

csv = input("Do you want to save your score? (Y/n) : ").lower()
if csv == 'y':
    f = open('score.txt', "w", encoding='utf-8')
    f.write(str(sc))
    print('Score saved!')
    s(3)

else:
    print("Ok.")

# See record

crs = input("Do you want to see your SAVED record??? (Y/n) : ").lower()
if crs == 'y':
    f = open('score.txt', 'r', encoding='utf-8')
    c = f.read()
    print(f"Your SAVED record is : {c}")
    s(5)
    exit()

else:
    print('Ok, see you soon!')
    s(3)
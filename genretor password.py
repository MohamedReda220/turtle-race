import random
import string
print("wlcome to the genretor password")
length=int(input("pls enter the length of your password="))
num_latters=int(input("pls enter the num of the letter="))
num_numbers=int(input("pls enter the num of the numbers="))
num_symbols=int(input("pls enter the num of the symbols="))
if length!=num_latters+num_numbers+num_symbols:
    print("inviled length enter the wright length???")
else:
    latters=string.ascii_letters
    numbers=string.digits
    symbols=string.punctuation
    password_chars=(random.choices(latters,k=num_latters)+
    random.choices(numbers,k=num_numbers)+
    random.choices(symbols,k=num_symbols)
    )
    random.shuffle(password_chars)
    password="".join(password_chars)

    print("your genretor password=",{password})

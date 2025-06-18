<<<<<<< HEAD
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','&','%','(',')','*','+']

print("welcome to password generator")
nr_letters=int(input("how many letters\n"))
nr_symbols=int(input("how many symbols\n"))
nr_numbers=int(input("how many numbers\n"))

password=""

for char in range(1, nr_letters + 1):
    random_char=random.choice(letters)
    password += random_char
    print(random_char)
=======
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','&','%','(',')','*','+']

print("welcome to password generator")
nr_letters=int(input("how many letters\n"))
nr_symbols=int(input("how many symbols\n"))
nr_numbers=int(input("how many numbers\n"))

password=""

for char in range(1, nr_letters + 1):
    random_char=random.choice(letters)
    password += random_char
    print(random_char)
>>>>>>> e56ef0fc648dc8fb5bdafe83c9d09d6de2851db4
  
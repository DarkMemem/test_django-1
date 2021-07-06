from random import randint

lst = []
for _ in range(25):
    lst.append(randint(10, 80))
    
lst1 = [randint(10, 80) for _ in range(25)]

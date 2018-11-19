from trycelery import add

for num in range(3):
    add.delay(num, num*2)
    
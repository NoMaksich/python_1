S=int(input("Введите сумму чисел: "))
P=int(input("Введите произведение чисел: "))
for x in range(1, S+1):
    if P%x==0:
        y=P//x
    if x+y==S:
        break
print(x ,y)
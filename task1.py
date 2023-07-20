count=int(input("Введите количество монет: "))
reshka=int(input("Введите количество монет, лежащих вверх решкой: "))
gerb=int(input("Введите количество монет, лежащих вверх гербом: "))
if reshka+gerb==count:
    if reshka>=gerb:
        print(gerb)
    else:
        print(reshka)
else:
    print("Введите числа заново")
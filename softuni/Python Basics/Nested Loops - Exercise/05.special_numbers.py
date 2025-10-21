number = int(input())

for num in range(1111, 9999 + 1):
    parced_num = str(num)
    is_special = True

    for i in range(len(parced_num)):
        parced_num2 = int(parced_num[i])

        if parced_num2 == 0:
            is_special = False
        elif number % parced_num2 != 0:
            is_special = False
            break
    
    if is_special:
        print(num, end=' ')

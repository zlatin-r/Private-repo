n = int(input())
flag = True

for _ in range(n):
    num = int(input())

    if num % 2 != 0:
        print(f"{num} is odd!")
        flag = False
        break

if flag:
    print("All numbers are even.")
    
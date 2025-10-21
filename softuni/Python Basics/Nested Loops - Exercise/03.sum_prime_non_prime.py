prime_sum = 0
non_prime_sum = 0

while True:
    flag = True
    command = input()

    if command == "stop":
        break

    num = int(command)

    if num < 0:
        print("Number is negative.")
        continue

    if num < 2:
        flag = False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            flag = False
    
    if flag:
        prime_sum += num
    else:
        non_prime_sum += num

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")

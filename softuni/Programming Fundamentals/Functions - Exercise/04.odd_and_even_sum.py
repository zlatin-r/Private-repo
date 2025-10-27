number = input()

def solve(num):
    odd_sum = 0
    even_sum = 0

    for i in range(len(num)):
        curr_num = int(num[i])

        if curr_num % 2 != 0:
            odd_sum += curr_num
        else:
            even_sum += curr_num
            
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

print(solve(number))

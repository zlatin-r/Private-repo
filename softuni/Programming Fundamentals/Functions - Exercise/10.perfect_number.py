def perfect_number(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    
    if sum(divisors) == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_number(number))

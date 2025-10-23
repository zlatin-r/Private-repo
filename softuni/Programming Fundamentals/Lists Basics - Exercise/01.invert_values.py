data = input().split(" ")

int_list = list(map(int, data))
int_list = [x * -1 for x in int_list]

print(int_list)

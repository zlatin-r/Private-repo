string = input()
points = 0

for i in range(len(string)):
    if string[i] == "a":
        points +=1
    elif string[i] == "e":
        points += 2
    elif string[i] == "i":
        points += 3
    elif string[i] == "o":
        points += 4
    elif string[i] == "u":
        points += 5

print(points)

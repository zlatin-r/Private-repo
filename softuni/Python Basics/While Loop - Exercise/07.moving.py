width = int(input())
length = int(input())
heigth = int(input())

total_space = width * length * heigth
taken_space = 0

command = input()

while total_space:
    
    if command == "Done":
        print(f"{total_space} Cubic meters left.")
        break

    parced_command = int(command)
        
    if total_space < parced_command:
        print(f"No more free space! You need {abs(total_space - parced_command)} Cubic meters more.")
        break

    total_space -= parced_command

    command = input()

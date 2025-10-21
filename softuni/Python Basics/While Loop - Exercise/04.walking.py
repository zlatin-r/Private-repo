goal = 10000
curr_steps = 0
succsess = False

while True:

    command = input()

    if command == "Going home":
        curr_steps += int(input())
        if curr_steps >= goal:
            succsess = True
        break
    
    curr_steps += int(command)

    if curr_steps >= goal:
        succsess = True
        break

if succsess:
    print(f"Goal reached! Good job!\n{abs(curr_steps - goal)} steps over the goal!")
else:
    print(f"{goal - curr_steps} more steps to reach goal.")

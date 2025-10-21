floors = int(input())
rooms = int(input())

for f in range(floors, 0, -1):
    result = ""

    if f == floors:
        for r in range(rooms):
            result += f"L{f}{r} "
    elif f % 2 == 0:
        for r in range(rooms):
            result += f"O{f}{r} "
    elif f % 2 != 0:
        for r in range(rooms):
            result += f"A{f}{r} "
   
    print(result)

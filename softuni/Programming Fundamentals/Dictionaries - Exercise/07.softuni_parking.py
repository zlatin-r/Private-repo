n = int(input())
data = {}

for _ in range(n):
    tokens = input().split()
    action, username = tokens[0], tokens[1]

    if action == "register":
        plate_num = tokens[2]

        if username not in data:
            data[username] = plate_num
            print(f"{username} registered {plate_num} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_num}")
    
    elif action == "unregister":

        if username not in data:
            print(f"ERROR: user {username} not found")
        else:
            del data[username]
            print(f"{username} unregistered successfully")

for user, info in data.items():
    print(f"{user} => {info}")

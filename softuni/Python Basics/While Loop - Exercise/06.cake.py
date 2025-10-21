width = int(input())
length = int(input())

total_pices = width * length

while total_pices:

    pices_eaten = input()

    if pices_eaten == "STOP":
        print(f"{total_pices} pieces are left.")
        break

    pices_parced = int(pices_eaten)

    if total_pices - pices_parced <= 0:
        print(f"No more cake left! You need {abs(total_pices - pices_parced)} pieces more.")
        break

    total_pices -= pices_parced

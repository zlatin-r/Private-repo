def solve(tp, num):
    if tp == "int":
        print(f"{int(num) * 2}")
    elif tp == "real":
        print(f"{float(num) * 1.5:.2f}")
    elif tp == "string":
        print(f"${num}$")
        

a = input()
b = input()

solve(a, b)

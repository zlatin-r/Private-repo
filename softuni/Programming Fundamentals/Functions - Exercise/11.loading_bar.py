def loading_bar(num):
    string = ""
    string += "%" * (num // 10)
    string += "." * (10 - (num // 10))

    if num != 100:
        print(f"{num}% [{string}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print(f"[{string}]")

number = int(input())
loading_bar(number)

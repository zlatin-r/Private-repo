password = input()

def solve(data):
    valid = True

    if not 6 <= len(data) <= 10:
        valid = False
        print("Password must be between 6 and 10 characters")
    if not data.isalnum():
        valid = False
        print("Password must consist only of letters and digits")
    if not sum(ch.isdigit() for ch in data) >= 2:
        valid = False
        print("Password must have at least 2 digits")

    if valid:
        print("Password is valid")
        
solve(password)

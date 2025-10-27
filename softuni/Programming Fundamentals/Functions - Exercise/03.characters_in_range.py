char_a = input()
char_b = input()

def solve(a, b):
    result = []

    code_a = ord(a) + 1
    code_b = ord(b)

    for i in range(code_a, code_b):
        result.append(chr(i))
    
    return " ".join(result)

print(solve(char_a, char_b))

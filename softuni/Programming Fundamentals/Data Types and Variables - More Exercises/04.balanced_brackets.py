n = int(input())
balanced = True
open_bracket = False 

for _ in range(n):
    line = input().strip()

    if line == "(":
        if open_bracket: 
            balanced = False
            break
        open_bracket = True

    elif line == ")":
        if not open_bracket:  
            balanced = False
            break
        open_bracket = False  

if open_bracket:
    balanced = False

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
    
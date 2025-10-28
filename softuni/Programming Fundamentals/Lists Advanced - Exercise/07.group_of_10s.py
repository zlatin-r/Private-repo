numbers = list(map(int, input().split(", ")))

group_max = 10

while numbers:
    current_group = [x for x in numbers if x <= group_max]
    
    print(f"Group of {group_max}'s: {current_group}")
    
    numbers = [x for x in numbers if x > group_max]
    
    group_max += 10

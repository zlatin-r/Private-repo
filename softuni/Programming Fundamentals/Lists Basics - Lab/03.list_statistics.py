n = int(input())

positive_lst = []
negative_lst = []

for _ in range(n):
    number = int(input())

    if number >= 0:
        positive_lst.append(number)
    else:
        negative_lst.append(number)

print(positive_lst)
print(negative_lst)
print(f"Count of positives: {len(positive_lst)}")
print(f"Sum of negatives: {sum(negative_lst)}")

countries = input().split(", ")
capitals = input().split(", ")

result = dict(zip(countries, capitals))

for cou, cap in result.items():
    print(f"{cou} -> {cap}")

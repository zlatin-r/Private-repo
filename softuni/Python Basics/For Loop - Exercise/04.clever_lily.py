age = int(input())
washmashine_price = float(input())
toy_price = int(input())
toys_count = 0
money_saved = 0
money_gift = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        toys_count += 1
    else:
        money_gift += 10
        money_saved += money_gift
        money_saved -= 1

money_from_toys = toy_price * toys_count
total_money = money_from_toys + money_saved

if total_money >= washmashine_price:
    print(f"Yes! {total_money-washmashine_price:.2f}")
else:
    print(f"No! {washmashine_price - total_money:.2f}")
    
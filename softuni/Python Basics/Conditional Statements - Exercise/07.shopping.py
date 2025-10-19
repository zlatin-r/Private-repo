video_card_price = 250

budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_count = int(input())

video_cards_cost = video_cards_count * video_card_price
processors_cost = (video_cards_cost * 0.35) * processors_count
ram_cost = (video_cards_cost * 0.1) * ram_count

total_cost = video_cards_cost + processors_cost + ram_cost

if video_cards_count > processors_count:
    total_cost *= 0.85

if budget >= total_cost:
    rest_money = budget - total_cost
    print(f"You have {rest_money:.2f} leva left!")
else:
    needed_money = total_cost - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")

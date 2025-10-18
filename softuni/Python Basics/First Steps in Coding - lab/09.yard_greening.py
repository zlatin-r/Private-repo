area = float(input())

q_meter = 7.61

total_price = (area * q_meter)
discount = total_price * 0.18

message_one = f"The final price is: {total_price - discount} lv."
message_two = f"The discount is: {discount} lv."

print(message_one)
print(message_two)

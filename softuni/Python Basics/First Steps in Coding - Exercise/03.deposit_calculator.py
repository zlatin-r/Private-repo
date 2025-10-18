deposited_amount = float(input())
deposit_term = int(input())
annual_interest_rate = float(input()) / 100

accrued_interest = deposited_amount * annual_interest_rate
interest_per_month = accrued_interest / 12

total_sum = deposited_amount + deposit_term * interest_per_month

print(total_sum)

pages_in_book = int(input())
pages_per_hour = int(input())
days = int(input())

total_reading_time = pages_in_book // pages_per_hour
hours_per_day = total_reading_time / days

print(hours_per_day)

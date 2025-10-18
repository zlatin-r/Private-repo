length = int(input())
width = int(input())
height = int(input())
percentage = float(input()) / 100

total_volume = length * width * height
total_liters = total_volume / 1000

total_water = total_liters - (total_liters * percentage)

print(total_water)

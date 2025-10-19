from math import ceil

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration * 0.125
rest_time = break_duration * 0.25

total_free_time = break_duration - lunch_time - rest_time

if total_free_time >= episode_duration:
    rest_time = total_free_time - episode_duration
    print(f"You have enough time to watch {series_name} and left with {ceil(rest_time)} minutes free time.")
else:
    needed_time = episode_duration - total_free_time
    print(f"You don't have enough time to watch {series_name}, you need {ceil(needed_time)} more minutes.")

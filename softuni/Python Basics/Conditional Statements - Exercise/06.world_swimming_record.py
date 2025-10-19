curr_record = float(input())
distance = float(input())
sec_per_meter = float(input())

ivans_time = distance * sec_per_meter
extra_seconds = (distance // 15) * 12.5
total_time = ivans_time + extra_seconds

if total_time < curr_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    needed_seconds = total_time - curr_record
    print(f"No, he failed! He was {needed_seconds:.2f} seconds slower.")

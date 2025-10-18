nylon_price = 1.5      # per sq. meter
paint_price = 14.5     # per liter
thinner_price = 5      # per litter

extra_nylon = 2
baggs = 0.4

nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
work_hours = int(input())

extra_paint = paint_needed * 0.10

total_nylon_price = nylon_price * (nylon_needed + extra_nylon)
total_paint_price = paint_price * (paint_needed + extra_paint)
total_thiner_price = thinner_price * thinner_needed

total_material_price = total_nylon_price + total_paint_price + total_thiner_price + baggs

work_salary_per_hour = total_material_price * 0.30

total_salary = work_hours * work_salary_per_hour

total_price = total_material_price + total_salary

print(total_price)

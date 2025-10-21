movie_name = input()

count_student_tickets = 0
count_standard_tickets = 0
count_kids_tickets = 0
total_sold_tickets = 0

while movie_name != "Finish":

    free_seats = int(input())
    total_seats = free_seats
    sold_tickets = 0

    while free_seats:
        ticket_type = input()

        if ticket_type == "End":
            break
        elif ticket_type == "student":
            count_student_tickets += 1
        elif ticket_type == "standard":
            count_standard_tickets += 1
        elif ticket_type == "kid":
            count_kids_tickets += 1

        total_sold_tickets += 1
        sold_tickets += 1
        free_seats -= 1
    
    pecentage = (sold_tickets / total_seats) * 100

    print(f"{movie_name} - {pecentage:.2f}% full.")

    movie_name = input()

percentage_student_tickets = (count_student_tickets / total_sold_tickets) * 100
percentage_standard_tickets = (count_standard_tickets / total_sold_tickets) * 100
percentage_kids_tickets = (count_kids_tickets / total_sold_tickets) * 100

print(f"Total tickets: {total_sold_tickets}")
print(f"{percentage_student_tickets:.2f}% student tickets.")
print(f"{percentage_standard_tickets:.2f}% standard tickets.")
print(f"{percentage_kids_tickets:.2f}% kids tickets.")

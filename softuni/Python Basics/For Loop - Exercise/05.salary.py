tabs = int(input())
salary = int(input())

facebook_fine = 150
instagram_fine = 100
reddit_fine = 50

for _ in range(tabs):
    site = input()

    if site == "Facebook":
        salary -= facebook_fine
    elif site == "Instagram":
        salary -= instagram_fine
    elif site == "Reddit":
        salary -= reddit_fine

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)

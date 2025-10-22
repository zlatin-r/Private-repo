command = input()
coffees = 0

while command != "END":

    if command.isupper():
        if command == "CAT" or command == "DOG" or command == "CODING" or command == "MOVIE":
            coffees += 2
    elif command.islower():
          if command == "cat" or command == "dog" or command == "coding" or command == "movie":
            coffees += 1

    command = input()

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)

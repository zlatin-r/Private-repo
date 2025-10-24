deck = input().split(" ")
shuffles = int(input())
mid_index = int(len(deck) / 2)

for _ in range(shuffles):
    new_deck = []
    a_deck, b_deck = deck[:mid_index], deck[mid_index:]

    for i in range(mid_index):

        new_deck.append(a_deck[i])
        new_deck.append(b_deck[i])

    deck = new_deck

print(deck)

def pokemon_dont_go():
    sequence = list(map(int, input().split()))
    removed_sum = 0

    while len(sequence) > 0:
        index = int(input())

        if index < 0:
            removed = sequence[0]
            sequence[0] = sequence[-1]
        elif index >= len(sequence):
            removed = sequence[-1]
            sequence[-1] = sequence[0]
        else:
            removed = sequence.pop(index)

        removed_sum += removed

        sequence = [x + removed if x <= removed else x - removed for x in sequence]

    print(removed_sum)

pokemon_dont_go()

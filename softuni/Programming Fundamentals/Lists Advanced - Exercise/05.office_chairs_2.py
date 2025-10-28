n = int(input())
rooms = [input().split() for _ in range(n)]

diffs = [len(chairs) - int(visitors) for chairs, visitors in rooms]

total_free = sum(d for d in diffs if d > 0)
lacking = [(i + 1, abs(d)) for i, d in enumerate(diffs) if d < 0]

if lacking:
    [print(f"{need} more chairs needed in room {room}") for room, need in lacking]
else:
    print(f"Game On, {total_free} free chairs left")
    
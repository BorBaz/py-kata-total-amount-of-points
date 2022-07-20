
# My case
def points(games):
    result = 0
    for item in games:
        if item[0:1] > item[2:3]:
            result += 3
        elif item[0:1] == item[2:3]:
            result += 1
    return result

# Best case
def points_bc(a):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))

print(points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']))

def calc(input):
    sum = 0
    for i in range(4):
        sum += int(str(input) * (i + 1))
    return sum
    
def stringSplit(input):
    x = input.replace(" ", "")
    splitString = x.split(',')
    return sorted(splitString)

def joinTwo(input1, input2):
    both = ''
    for i in range(len(input1)):
        both += (''.join(input1[i]) + ''.join(input2[i]))
    return both
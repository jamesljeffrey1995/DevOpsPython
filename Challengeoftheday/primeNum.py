def primeNumber(input):
    if input >1:
        for i in range(2,input):
            if input%i==0:
                return False
            else:
                return True
    return False
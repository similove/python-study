if __name__ == '__main__':
    i = 10
    while i <= 10000000:
        n = len(str(i))
        j = 1
        sumValue = 0
        while j <= n:
            cell = (i % (10 ** j)) // (10 ** (j - 1))
            sumValue += cell ** n
            j += 1
        if sumValue == i:
            print(i)
        i += 1

if __name__ == '__main__':
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    print(a[:2])
    print(a[:])
    print(a[5:2:-1])
    print(a[::-2])
    # print(a)
    # del a[1]
    # print(a)
    # a[0:2] = 'HIJ'
    # print(a)
    print(str(a))
    a.sort(reverse=True)
    print(a)

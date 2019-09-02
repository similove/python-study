def mk_avg():
    numbers = []

    def avg(n):
        numbers.append(n)
        return sum(numbers) / len(numbers)

    return avg


if __name__ == '__main__':
    average = mk_avg()
    average(12)
    average(22)
    print(average(221))

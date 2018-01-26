# maxnum = [i for i in range(1000)]

# fibon = [i for i in range(3,maxnum)]


def fib2(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b


def fib(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


def evenCells(array):

    result = [i for i in array if i % 2 == 0]

    return result


maxnum = 4000000
fibseq = fib(maxnum)
fibsum = sum(evenCells(fibseq))
print(fibsum)

def primeFactors(n):

    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return factors


print(max(primeFactors(600851475143)))

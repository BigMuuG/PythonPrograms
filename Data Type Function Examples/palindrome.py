def palindrome(n):
    n1 = 10**(n)
    n2 = 10**(n)
    bounds = 10**(n - 1) * 10**(n - 1)
    prod = n1 * n2
    i = 0

    while prod > 1:
        k = 0

        while prod > bounds:
            palin = str(prod)
            print(palin)
            rpalin = palin[::-1]
            if palin == rpalin:
                return prod
            prod = (n1 - i) * (n2 - k)
            k += 1

        i += 1


print(palindrome(2))

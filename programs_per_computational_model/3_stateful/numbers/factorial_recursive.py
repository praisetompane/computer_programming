def recursive_factorial(n):
    def _factorial(n, product):
        if n == 1:
            return product
        else:
            return _factorial(n - 1, product * n)

    return _factorial(n, 1)


print(recursive_factorial(3))
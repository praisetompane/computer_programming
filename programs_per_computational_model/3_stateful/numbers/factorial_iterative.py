def iterative_factorial(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result


print(iterative_factorial(3))


def iterative_stack_factorial(n):
    result = []
    result.append(1)

    for num in range(1, n + 1):
        result.append(result.pop() * num)
    return result.pop()


print(iterative_stack_factorial(3))

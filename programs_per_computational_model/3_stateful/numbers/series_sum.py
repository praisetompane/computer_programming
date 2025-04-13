def summingSeries(n):
    """
    O(N) solution.
    This is not good enough, because n can be 10^16, which is too large for a linear time algorith.
    """
    series_sum = 0
    for i in range(1, n + 1):
        series_sum += i**2 - (i - 1) ** 2
        print(series_sum)
    return series_sum % (10**9 + 7)


if __name__ == "__main__":
    print(summingSeries(3))

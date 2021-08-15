def f(n):
    if n == 0:
        return 0, 0, 0

    total_sum, even_sum, odd_sum = f(n - 1)
    total_sum += n
    if n % 2 == 0:
        even_sum += n
    else:
        odd_sum += n

    return total_sum, even_sum, odd_sum


print(f(4))

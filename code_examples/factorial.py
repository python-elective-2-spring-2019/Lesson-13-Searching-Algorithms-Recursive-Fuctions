def factorial(n):
    # Base case
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

        # 5 * 4 * 3 * 2 * 1 * 1


def factorial_loop(n):
    sum = n
    for i in range(1, n):
        sum = sum * i
        
    return sum    


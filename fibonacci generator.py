def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

# Example usage:
limit = 1000
fib_sequence = list(fibonacci_generator(limit))
print(fib_sequence)

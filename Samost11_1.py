def fib(n):
    a = 1
    b = 1
    for i in range(n):
        result = a
        a, b = b, a + b
        yield result
for value in fib(200):
    print(value)
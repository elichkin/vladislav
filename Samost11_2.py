def fib(n):
    a = 1
    b = 1
    for i in range(n):
        result = a
        a, b = b, a + b
        yield result
with open('./txtfiles/fib.txt', 'a') as file:
    for value in fib(200):
        file.write(f'{value}\n')
        print(value)
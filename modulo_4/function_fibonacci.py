""" 
fib_1 = 1 
fib_2 = 1 
fib_3 = 1 + 1 = 2 
fib_4 = 1 + 2 = 3 
fib_5 = 2 + 3 = 5 
fib_6 = 3 + 5 = 8 
fib_7 = 5 + 8 = 13 """
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
 
for n in range(1, 10):  # testando
    print(n, "->", fib(n))

print(fib(0))  # Saída esperada: None
print(fib(1))  # Saída esperada: 1
print(fib(2))  # Saída esperada: 1
print(fib(3))  # Saída esperada: 2

# O código com yield
def fib_generator(n):
    elem_1 = elem_2 = 1
    for i in range(n):
        if i < 2:
            yield 1
        else:
            the_sum = elem_1 + elem_2
            elem_1, elem_2 = elem_2, the_sum
            yield the_sum

# Como usar:
for num in fib_generator(10):
    print(num)
    
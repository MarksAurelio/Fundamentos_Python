# A recursão é uma técnica em que uma função se chama.
# A definição dos números de Fibonacci é um exemplo claro de recursão. Já falamos a você que:

# Fib i = Fib i-1 + Fib i-2
# A definição do i-ésimo número refere-se ao número i-1, e assim por diante, até que você atinja os dois primeiros.
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
 
for n in range(1, 10):  # testando
    print(n, "->", fib(n)) # saída esperada: 1, 1, 2, 3, 5, 8, 13, 21, 34

# Agora a própria função vai se chamar:
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)
 
for n in range(1, 6):  # testando
    print(n, factorial_function(n))  # saída esperada: 1, 2, 6, 24, 120 

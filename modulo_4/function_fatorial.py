""" 
0! = 1 (sim! É verdade)
1! = 1
2! = 1 * 2
3! = 1 * 2 * 3
4! = 1 * 2 * 3 * 4
:
:
n! = 1 * 2 * 3 * 4 * ... * n-1 * n """
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
 
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
 
for n in range(1, 6):  # testando
    print(n, factorial_function(n))

print(factorial_function(-1))  # Saída esperada: None
print(factorial_function(0))   # Saída esperada: 1
print(factorial_function(1))   # Saída esperada: 1

# Outra forma de escrever com a saída decrescente
# Implementação recursiva da função fatorial.
 
def factorial(n):
    if n == 1:    # O caso base (condição de rescisão).
        return 1
    else:
        return n * factorial(n - 1)
 
print(factorial(4)) # 4 * 3 * 2 * 1 = 24

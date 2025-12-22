def is_a_triangle(a, b, c):
 if a + b <= c:
    return False
 if b + c <= a:
    return False
 if c + a <= b:
    return False
 return True

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

# Uma versão mais compacta da função acima seria:
def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True
 
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

# Ou ainda mais compacta:
def is_a_triangle(a, b, c):
    return not (a + b <= c or b + c <= a or c + a <= b)

print(is_a_triangle(1, 1, 1))

# Outra forma de escrever a função é:
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(is_a_triangle(1, 1, 1))

# Triângulos e o teorema de Pitágoras c2 = a2 + b2
def is_a_triangle(a, b, c):
 return a + b > c and b + c > a and c + a > b

a = float(input('Digite o primeiro lado\'s comprimento: '))
b = float(input('Entre no segundo lado\'s comprimento: '))
c = float(input('Entre no terceiro lado\'s comprimento: '))

if is_a_triangle(a, b, c):
    print('Sim, pode ser um triângulo.')
else:
    print('Não, não pode ser um triângulo.')

# Verificar qual dos três lados é o maior (hipotenusa)   
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))

# Avaliando a área de um triângulo
# Também podemos avaliar a área de um triângulo. A fórmula da Heron será útil aqui
# Vamos usar o operador de exponenciação para encontrar a raiz quadrada - pode parecer estranho, mas funciona:
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
 
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
 
def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)
 
print(area_of_triangle(1., 1., 2. ** .5)) # saída esperada: 0.49999999999999994 É muito próximo de 0,5, mas não é exatamente 0,5. O que isso significa? É um erro?
# Não, não é. Essas são as especificidades dos cálculos de ponto flutuante.
 
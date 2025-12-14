# Exemplo 1
word = "Python"
for letter in word:
    print(letter, end="*")
print()  # Para pular uma linha após o loop

# Exemplo 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

# Exemplo 3
while True:
    print("Preso em um loop infinito.")
    break
 
 # Exemplo 3
counter = 5
while counter > 2:
    print(counter)
    counter -= 1

# Exemplo 4
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")
print()  # Para pular uma linha após o loop

# Exemplo 5
text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")
print()  # Para pular uma linha após o loop
# Exemplo 6
n = 0
 
while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")
 
print()
 
for i in range(0, 3):
    print(i)
else:
    print(i, "else")

# Exemplo 7
for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2
print()
for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2
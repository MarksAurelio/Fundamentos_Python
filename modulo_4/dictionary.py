dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
phone_numbers = {'chefe' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

# Imprima os valores aqui.
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

# Programa com adição de alunos e suas notas, apos a digitação, o programa imprime a média das notas.
school_class = {}

while True:
 name = input("Digite o nome do aluno: ")
 if name == '':
    break
 
 score = int(input("Insira a pontuação do aluno (0-10): "))
 if score not in range(0, 11):
    break
 
 if name in school_class:
    school_class[name] += (score,)
 else:
    school_class[name] = (score,)
 
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

# Tarefa realizar uma função que calcula o Índice de Massa Corporal (IMC)
def bmi(weight, height):
    return weight / height ** 2
 
 
print(bmi(52.5, 1.65))

# Avaliação do IMC e conversão de unidades imperiais em unidades métricas
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2

print(bmi(352.5, 1.65))

# Podemos escrever duas funções simples para converter unidades imperiais em unidades métricas. Vamos começar com libras.

# É um fato bem conhecido que 1 lb = 0.45359237 kg. Usaremos isso em nossa nova função.
def lb_to_kg(lb):
    return lb * 0.45359237
 
print(lb_to_kg(1))
 
# Agora é hora de pés e polegadas: 1 pé = 0.3048 m, e 1 in = 2.54 cm = 0.0254 m.
def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254
 
print(ft_and_inch_to_m(1, 1))
print(ft_and_inch_to_m(6, 0))

# É bem possível que às vezes você queira usar apenas pés sem polegadas.
def ft_and_inch_to_m(ft, inch = 0.0): # Agora, o parâmetro inch tem seu valor padrão igual a 0.0.
    return ft * 0.3048 + inch * 0.0254
 
print(ft_and_inch_to_m(6))
 
# Por fim, o código é capaz de responder à pergunta: qual é o IMC de uma pessoa de 5'7" de altura e pesando 176 libras?
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
 
def lb_to_kg(lb):
    return lb * 0.4535923
  
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
 
    return weight / height ** 2
 
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

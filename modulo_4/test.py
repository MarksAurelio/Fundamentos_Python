temperature = float(input('Digite a temperatura atual:'))

if temperature > 0:
 print("Acima de zero")
elif temperature < 0:
 print("Abaixo de zero")
else:
 print("Zero")

while True:
    try:
        number = int(input("Digite um número int: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError):
        print("Valor errado ou nenhuma divisão por regra de zero quebrada.")
    except:
        print("Desculpe, algo deu errado...")
 
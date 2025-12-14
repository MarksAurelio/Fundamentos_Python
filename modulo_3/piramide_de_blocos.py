""" Sua tarefa é escrever um programa que lê o número de blocos que os construtores têm e gera a altura da pirâmide que pode ser construída usando esses blocos.

Nota: a altura é medida pelo número de camadas totalmente concluídas; se os construtores não tiverem um número suficiente de blocos e não puderem concluir a próxima camada, eles terminarão seu trabalho imediatamente. """
blocks = int(input("Digite o número de blocos disponíveis: "))
height = 0
layer = 1
while blocks >= layer:
    blocks -= layer
    height += 1
    layer += 1
print("A altura máxima da pirâmide é:", height)

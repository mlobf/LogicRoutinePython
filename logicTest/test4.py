"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
notas = []
max_notas = 5

pergunta = "Primeira nota "

for x in range(4):
    print("Sua nota no bimestre pls ")
    try:
        notas.append(int(input()))
    except:
        notas.append(0)



def calcular_media(*args):
    media = sum(notas) / len(notas)
    return print(media)


calcular_media()

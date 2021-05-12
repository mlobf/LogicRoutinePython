"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""


class Teste:
    def __init__(self, notas):
        self.notas = notas

    @property
    def pergunta(self):
        for x in range(4):
            print("Sua nota no bimestre pls ")
            self.notas.append(int(input()))
        return notas

    @property
    def calcular_media(self):
        self.pergunta
        media = sum(self.notas) / len(self.notas)
        return print(media)


notas = []
new_teste = Teste([])

new_teste.calcular_media

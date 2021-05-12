'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
 trabalhadas no mês. Calcule e mostre o total do seu salário no
 referido mês.
'''

ganha_por_hora = 100
numero_de_horas = 160


def salario_mes(ganha_por_hora, numero_de_horas):
    salario_mes = (ganha_por_hora * numero_de_horas)
    return salario_mes


print(salario_mes(100, 160))


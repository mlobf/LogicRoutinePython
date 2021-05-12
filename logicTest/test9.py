'''
Faça um Programa que peça a temperatura em graus Farenheit, 
transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
'''

temperatura_celsus = 0


def convert_celsus(temperatura_celsus):
    celsus = ((temperatura_celsus - 32) / 1.8)
    return celsus


print(convert_celsus(100))


temperatura_celsus = 0


def convert_celsus(temperatura_celsus):
    celsus = ((temperatura_celsus - 32) / 1.8)
    return celsus


print(convert_celsus(100))

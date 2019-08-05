import random

class RandomGenerator():
        
    def random_number():
        randon_numbers = set()
        cantidad_de_numeros = 4
        rango_del_numero_aleatorio = 9

        while len(randon_numbers) < cantidad_de_numeros:
            n_aleatorio = random.randrange(rango_del_numero_aleatorio + 1)
            randon_numbers.add(n_aleatorio)

        return randon_numbers

# if __name__ == '__main__':
#     random_returned = RandomGenerator.random_number()
#     print("El numero fue: {}".format(random_returned))
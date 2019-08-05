from ran_gen.random_generator import RandomGenerator
from user_input.input_number import InputPerson

class Comparision_numbers:

    def possibilities():
        loop = 1
        number_random = list(RandomGenerator.random_number())
        while loop == 1:
            person_number = InputPerson.number_input()        
            print("el numero es: {}".format(number_random))
            position_list = 4
            count = 0
            count_coincidences = 0
            for i in range(position_list):
                int_person_number = int (person_number[i])
                #print(type(person_number[i]))
                #print(type(number_random[i]))
                if int_person_number == number_random[i]:
                    count = count + 1
            
                if number_random[0] == int_person_number and i != 0:
                    count_coincidences = count_coincidences + 1
                if number_random[1] == int_person_number and i != 1:
                    count_coincidences = count_coincidences + 1
                if number_random[2] == int_person_number and i != 2:
                    count_coincidences = count_coincidences + 1
                if number_random[3] == int_person_number and i != 3:
                    count_coincidences = count_coincidences + 1

            print("Su cantidad de aciertos es: {}, y coincidencias es de: {}".format(count, count_coincidences))

            if count == 4:
                loop = loop + 1
            
        return count, count_coincidences   
        
        
if __name__ == '__main__':
    contador_aciertos, contador_coindidencias = Comparision_numbers.possibilities()
    print("Felicitaciones lograste adivinar el numero")
    

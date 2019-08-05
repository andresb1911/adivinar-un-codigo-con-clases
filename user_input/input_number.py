
class InputPerson():

    def number_input():
        var_loop= 1
        while var_loop == 1:
            number = input("Digite un numero de cuatro cifras no repetidas: ")
            number_list = list(number)
            number_quantity = 4
            
            if len(number_list) == number_quantity:
                if number_list[0] != number_list[1] and number_list[0] != number_list[2] and number_list[0] != number_list[3] and number_list[1] != number_list[2] and number_list[1] != number_list[3] and number_list[2] != number_list[3]:
                    print (number)
                    var_loop= var_loop + 1
                    return number
        
                else:
                    print ("El numero tiene cifras repetidas, digite un nuevo numero")

            else:
                print ("El numero tiene que ser de 4 cifras, digite un nuevo numero")

# if __name__ == '__main__':
#     input_returned = Inputerson.number_input()
#     print("El numero fue: {}".format(input_returned))



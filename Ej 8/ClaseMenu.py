from ClaseConjunto import Conjunto
class Menu:
    __opcion = 0
    def __init__(self):
        __opcion = 0
    def seleccionar(self,c1,c2):
        c = []
        print("----MENU DE OPCIONES----")
        print("Opcion 1: Sumar los conjuntos")
        print("Opcion 2: Restar los conjuntos")
        print("Opcion 3: Ver si los conjuntos son iguales")
        print("Opcion 4: Salir")
        while self.__opcion != 4:
            self.__opcion = int(input("Seleccione una opcion. "))
            if self.__opcion == 1:
                 c=c1+c2
                 print("La suma de los conjuntos es: {}".format(c))
            elif self.__opcion == 2:
                c=c1-c2 
                print("La resta de los conjuntos es: {}".format(c))
            elif self.__opcion == 3:
                if (c1 == c2) == True:
                    print("Los conjuntos son iguales")
                else:
                    print("Los conjuntos no son iguales")
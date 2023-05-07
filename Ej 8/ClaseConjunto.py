class Conjunto:
    __numeros = []
    def __init__(self):
        self.__numeros = []
    def agregar(self):
        tamaño = int(input("Ingrese el tamaño del conjunto "))
        for i in range (tamaño):
            elem = int(input("Ingrese el numero entero a agregar al conjunto "))
            self.__numeros.append(elem)
        
    def mostrarConj(self):
        for elem in range(len(self.__numeros)):
            print("Elemento N°{}: {}".format(elem+1,self.__numeros[elem]))
    def __add__(self, conj2):
        suma = Conjunto()
        for elemento in self.__numeros:
            suma.__numeros.append(elemento)
        for elem in conj2.__numeros:
            if(elem not in suma.__numeros):
                suma.__numeros.append(elem) 
        return  suma.__numeros
    def __sub__(self, conj2):
        resta = Conjunto()
        for elem in self.__numeros:
            if elem not in conj2.__numeros:
                resta.__numeros.append(elem)
        return resta.__numeros
    def __eq__(self, conj2):
        b = False
        if (len(self.__numeros)== len(conj2.__numeros)):
            for i in range(len(self.__numeros)):
                if self.__numeros[i] == conj2.__numeros[i]:
                    b = True
            for i in range(len(conj2.__numeros)):
                if conj2.__numeros[i] == self.__numeros[i]:
                    b = True
        else:
            b = False
        return b
from ClaseConjunto import Conjunto
from ClaseMenu import Menu
if __name__ == "__main__":
    conjunto_1= Conjunto()
    conjunto_2= Conjunto()
    conjunto_1.agregar()
    conjunto_1.mostrarConj()
    conjunto_2.agregar()
    conjunto_2.mostrarConj()
    m = Menu()
    m.seleccionar(conjunto_1, conjunto_2)
        
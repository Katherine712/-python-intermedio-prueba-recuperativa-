#clase 
class Telefono:
    def __init__(self, num):
        self.num = num

#metodos
    def imprimir(self):
        cadena = self.num
        cadena[4:-3]
        with open("ejercicio_1.txt", "w") as archivo:
            archivo.write(f"El número sin prefijo ni extensión es : {cadena[4:-3]}")

        
def main(): 
    num = input("Introduce un número de teléfono con el formato +xx-xxxxxxxx-xx: ")
    telefono = Telefono(num)
    telefono.imprimir()
    print('El número de teléfono es ', num[4:-3])

if __name__ == '_main_':
    main()

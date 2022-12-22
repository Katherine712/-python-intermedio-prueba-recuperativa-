#Clase
class Rent:

    def __init__(self, nombre , renta):
        self.nombre = nombre
        self.renta = renta
      
        if self.renta < 10000 :
            self.tipo = 0.05 
        elif self.renta < 20000:
            self.tipo= 0.15
        elif self.renta < 35000:
            self.tipo = 0.20
        elif self.renta < 60000:
            self.tipo = 0.30
        else:
            self.tipo = 0.45

#Métodos
    def imprimir_impuesto(self):
        impuesto = self.tipo * self.renta
        with open("w", "ejercicio_2.txt") as archivo:
         archivo.write(f"La renta a pagar por {self.nombre} es {impuesto}")
        

         
def main(): 
    renta = int(input("Ingrese la renta: "))
    usuario = Rent("Usuario", renta)
    usuario.imprimir_impuesto()

if __name__ == '_main_':
    main()

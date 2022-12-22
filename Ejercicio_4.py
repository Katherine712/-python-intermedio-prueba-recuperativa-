# Clase
class valorsiniva:

    def __init__(self, neto, tasa = 0.19):
        self.neto = n
        self.tasa = tasa
# Método
    def imprimir(self):
        iva = self.tasa * self.neto
        with open("w","ejercicio_4.txt") as archivo:
            archivo.write(
            "El total es:\n" + 
            "Neto( excluyendo el IVA): " + str(self.neto) + "\n" + 
            "I.V.A.: " + str(iva) + "\n" + 
            "valor(n más I.V.A.): " + str(iva + self.neto) )
        
def main(): 
    usuarios = valorsiniva(100)
   usuarios.imprimir()

if __name__ == '__main__':
    main()

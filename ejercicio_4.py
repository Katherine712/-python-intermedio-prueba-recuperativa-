# Clase
class valorsiniva:

    def __init__(self, net, neto, tasa = 0.19):
        self.tasa = tasa
        self.net = neto
# Método
    def imprimir(self):
        iva = self.tasa * self.net
        with open("w","ejercicio_4.txt") as archivo:
            archivo.write(
            "El total es:\n" + "Neto: " + str(self.neto) + "\n" +  "IVA: " + str(iva) + "\n" + "valor: " + str(iva + self.net) )
        
def main(): 
    usuarios = valorsiniva(100)
   usuarios.imprimir()

if __name__ == '__main__':
    main()
Footer
© 2022 GitHub, Inc.

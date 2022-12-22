#Ejercicio 3_ Asignaturas
#Clase
class Asignaturas:

    def __init__(self):
        self.libr = {"matematica": 0.0, "fisica": 0.0, "quimica": 0.0, "historia": 0.0, "lengua": 0.0}
        
# Método
    def pregunta_notas(self):
        self.libr["matematica"] = float(input("Ingrese nota de Matemáticas: "))
        self.libr["fisica"] = float(input("Ingrese nota de Fisica : "))
        self.libr["quimica"] = float(input("Ingrese nota de Quimica : "))
        self.libr["historia"] = float(input("Ingrese nota de Historia: "))
        self.libr["lengua"] = float(input("Ingrese nota de Lengua : "))
    
    def imprimir_notas(self):
        with open("ejercicio_3.txt", "w") as archivo:
            archivo.write(
                f"Tienes que repetir {list(self.libr.keys())}"  )
    def elimina_aprobados(self):
        lista_aprobados = []

        for contador in self.libr:
            if self.libr[contador] >= 4.0:
                lista_aprobados.append(contador)

        for contador in  range(len(lista_de_aprobados)):
            posicicion_a_eliminar = lista_aprobados[contador]
            del self.libr[posicicion_a_eliminar] 
       
def main(): 
    usuario = Asignaturas()
    usuario.pregunta_notas()
    usuario.elimina_aprobados()
    usuario.imprimir_notas()

if __name__ == '__main__':
    main()

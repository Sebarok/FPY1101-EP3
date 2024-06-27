import os

libros = []
caracteristicas = ['libro', 'autor', 'año'] # , 'sku'
prestamos= []

#1
def registrar_libro():
    
    nombre_del_libro = input("Indique el nombre del libro : ").lower
    autor = input("Indique el nombre del autor del libro : ").lower
    año_del_libro = input("indique el año de publicación del libro : ").lower
    # pendiente  sku = 
    
    if nombre_del_libro == "" or autor == "" or año_del_libro == "": # sku == ""
        print("Faltan datos, por fabor ingrese todos los datos solicitados")
     
    else:
        libro = {
            'libro' : nombre_del_libro, 
            'autor': autor, 
            'año' : año_del_libro
        }

        
        libros.append(libro)

#2

def prestar_libro():

    print("ingrese los datos del libro que busca")
    nombre_del_libro = input("Indique el nombre del libro : ").lower
    autor = input("Indique el nombre del autor del libro : ").lower
    año_del_libro = input("indique el año de publicación del libro : ").lower
    # pendiente  sku = 
    
    if nombre_del_libro == "" or autor == "" or año_del_libro == "": # sku == ""
        print("Faltan datos, por fabor ingrese todos los datos solicitados")
     
    else:
        prestar = {
            'libro' : nombre_del_libro, 
            'autor': autor, 
            'año' : año_del_libro
        }

        
        prestamos.append(prestar)
    
    


#3
def lista_libro():
    print("libro\t\tautor\t\taño\t\t""\n") # agregar sku
    
    for libro in libros:
        print(f"{libro['libro']}\t\t{libro['autor']}\t\t{libro['año']}\n") # agregar cuando tengas el sku \t\t{libro[sku]}

4#
def imprimir_reporte_prestamos():
    try:
        op = int(input("Ingrese la opcion que necesita\n1. Todo\n2. Libro en especifico\n Opcion a elegir : "))

        if op == 1:
            with open('planilla_de_libros_prestados.txt', 'w') as prestamos:
                prestamos.write("libro\t\tautor\t\taño") #agregar \t\tsku

                for libro in prestamos:
                    prestamos.write(f"{libro['libro']}\t\t{libro['autor']}\t\t{libro['año']}\n") # agregar cuando tengas el sku \t\t{libro[sku]}

            print("Planilla generada exitosamente en : ", os.getcwd()) 


    except ValueError:
        print("Error elija la opcion correcta")



def menu():
    while True:
        try:
            print("========== MENU ==========")
            print("1. Registrar libro\n2. Prestar libro\n3. Listar todos los libros\n4. Imprimir Reporte de Prestamos\n5. Salir")

            opc = int(input("Elija la opcion que desea : "))

        except ValueError:
            print("Error, elija dentro de las opciones dadas")

        if opc == 1:
            registrar_libro()

        elif opc == 2:
            prestar_libro()
        
        elif opc ==3:
            lista_libro()

        elif opc == 4:
            imprimir_reporte_prestamos()

        elif opc == 5:
            print("Finalizando programa")
            break
        else:
            print("Error, elija una de las opciones dadas en el menú")




def functions_tarea():
    menu = 1
    
    while menu != 3:
        print("\nMenu: \n1. Default parameters  \n2. Keywords arguments  \n3. Salir")
        menu = int(input("Elige un número: "))

        if menu == 1:
            functions_default_parameters()
        elif menu == 2:
            functions_keywords_arguments()
        elif menu == 3:
            print("Gracias por utilizar el programa")
            menu == 3
        else:
            print("Elegiste un número incorrecto")

def functions_default_parameters():
    menu_dp = 1
    
    while menu_dp != 4:
        print("\n\tMenu: \n\t1. Hola  \n\t2. Operación \n\t3. fav_lenguaje  \n\t4. Salir")
        menu_dp= int(input("\tElige un número: "))

        if menu_dp == 1:
            print("\n\tHola")
            Hola()
        elif menu_dp == 2:
            print("\n\tOperación")
            Operacion()
        elif menu_dp== 3:
            print("\n\tfav_lenguaje")
            fav_lenguaje()
        elif menu_dp== 4:
            print("\tGracias por utilizar el programa")
            menu_dp == 4
        else:
            print("\tElegiste un número incorrecto")

def functions_keywords_arguments():
    menu_ka = 1
    
    while menu_ka != 4:
        print("\n\tMenu: \n\t1. Elegir carrera  \n\t2. Imprimir arreglo  \n\t3. Saludame   \n\t4. Salir")
        menu_ka= int(input("\tElige un número: "))

        if menu_ka == 1:
             print("\n\tElegir carrera")
             alumno= input("\tElige una carrera (ISC O IIF): ")
             Elegir_carrera(alumno = alumno)
        elif menu_ka == 2:
             print("\n\tImprimir arreglo")
             Imprimir_arreglo("Jose","Fer","Pablo","Alan","Liss")
        elif menu_ka== 3:
             print("\n\tSaludame")
             nombre= input("\tIngresa tu nombre: ")
             saludame(nombre = nombre)
        elif menu_ka== 4:
             print("\tGracias por utilizar el programa")
             menu_ka == 4
        else:
             print("\tElegiste un número incorrecto")

def Hola(firstname = 'José'):
     print(f"\tHola {firstname}, Como estas?")

def Operacion(valor = 10):
     print(f"\tEl resultado de la operación 10 * 10 = {valor*10}")

def fav_lenguaje(lenguaje="Python"):
    print(f"\tMi lenguaje favorito de programación es {lenguaje}!")

def Elegir_carrera(**kwargs):
    if kwargs.get('alumno') == "ISC":
        print("\tElegiste la carrera de Sistemas computacionales")
    else:
        print("\tElegiste la carrera de Informática")

def Imprimir_arreglo(*args):
     nombre_1 = args[0]
     nombre_2 = args[1]
     nombre_3 = args[2]
     nombre_4 = args[3]
     nombre_5 = args[4]

     print(f"\t1: {nombre_1}")
     print(f"\t2: {nombre_2}")
     print(f"\t3: {nombre_3}")
     print(f"\t4: {nombre_4}")
     print(f"\t5: {nombre_5}")

def saludame(**kwargs):
    for key, value in kwargs.items():
        print("\tHola","{1}".format(key, value))

functions_tarea()
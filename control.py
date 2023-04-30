
def control():
    menu = 1
    
    while menu != 5:
        print("\nMenu: \n1. if-else    \n2. Operadores ternarios  \n3. For   \n4. While     \n5. Salir")
        menu = int(input("Elige un número: "))

        if menu == 1:
            control_if_else()
        elif menu == 2:
             control_operadores_ternarios()
        elif menu == 3:
             control_for()
        elif menu == 4:
             control_while()
        elif menu == 5:
             print("Gracias por utilizar el programa")
             menu == 5
        else:
             print("Elegiste un número incorrecto")
        
def control_if_else():
    print("\n\tElegiste if-else")
    menu_if = 1
    
    while menu_if != 4:
        print("\n\tMenu: \n\t1. Número par o impar    \n\t2. Número mayor   \n\t3. Calificaciones   \n\t4. Salir")
        menu_if = int(input("\tElige un número: "))   

        if menu_if == 1:
            print("\n\tNúmero par o impar")
            valor = int(input("\tAgrega un número: "))
            if valor%2 == 0 :
                print("\tEl número es par")
            else: 
                print("\tEl número es impar")

        elif menu_if == 2:
            print("\n\tNúmero mayor")
            valor1 = int(input("\tAgrega un número: "))
            valor2 = int(input("\tAgrega un segundo número: "))

            if valor1 > valor2 :
                print("\tEl primer número es mayor")
            elif valor1 == valor2:
                print("\tLos números son iguales")
            else: 
                print("\tEl segundo número es menor")

        elif menu_if == 3:
            print("\n\tCalificaciones")
            valor = int(input("\tAgrega la calificación del 1 al 10: "))

            if valor >= 7 :
                print("\tCalifiación aprobatoria")
            else: 
                print("\tCalifiación reprobatoria")

        elif menu_if == 4:
             print("\tGracias por utilizar if-else")
             menu_if == 4
        else:
             print("\tElegiste un número incorrecto")

def control_operadores_ternarios(): 
    print("\n\tElegiste operadores ternarios")
    menu = 1
    
    while menu != 4:
        print("\n\tMenu: \n\t1. Número positivo o negativo  \n\t2. Calificación   \n\t3. Atinale al valor  \n\t4. Salir")
        menu = int(input("\tElige un número: "))

        if menu == 1:
            print("\n\tNúmero positivo o negativo")
            num = float(input("\tIntroduce un número: "))
            es_positivo = True if num > 0 else False
            print("\tEl número es positivo:", es_positivo)
        elif menu == 2:
             print("\n\tCalificación")
             num = float(input("\tIntroduce la calificación: "))
             cali = 'aprovatoria' if num > 7   else 'reprobatoria'
             print("\tLa calificación es:", cali)
        elif menu == 3:
             print("\n\tAtinale al valor")
             num = float(input("\tIntroduce un número: "))
             cali = 'Le atinaste' if num == 24   else 'Fallaste'
             print(f"\t{cali}")
        elif menu == 4:
             print("\tGracias por utilizar operadores ternarios")
             menu == 4
        else:
             print("\tElegiste un número incorrecto")
        
def control_for():
    print("\n\tElegiste ciclo for")
    menu_for = 1
    
    while menu_for != 4:
        print("\n\tMenu: \n\t1. Contador de números    \n\t2. Mostrar un arreglo   \n\t3. Factorial    \n\t4. Salir")
        menu_for= int(input("\tElige un número: "))   

        if menu_for == 1:
            print("\n\tContador de números")
            for i in range(1,11,1):
                print(f"\t{i}")
                
        elif menu_for == 2:
             print("\n\tMostrar un arreglo")
             lista = ['José', 'Pablo', 'Fer', 'Alan', 'Omar']
             for i in range(0,5,1):
                print(f"\t{lista[i]}")
                
        elif menu_for == 3:
             print("\n\tFactorial ")
             fac = 1
             num= int(input("\tElige un número: "))   
             for i in range(1,num+1,1):
                fac *=i 
             print(f"\tEl factorial de {num} es igual a {fac}")

        elif menu_for == 4:
             print("\tGracias por utilizar For")
             menu_for == 4
        else:
             print("\n\tElegiste un número incorrecto")

def control_while():
    print("Elegiste ciclo while")
    menu_for = 1
    
    while menu_for != 4:
        print("\n\tMenu: \n\t1. N  \n\t2. Recorrer arreglo   \n\t3. Resuelve la operación     \n\t4. Salir")
        menu_for= int(input("\tElige un número: "))   

        if menu_for == 1:
            print("\n\tN")
            letra = 'A'
            while letra != 'N':
                letra= input("\tIngresa una letra 'N': ")   
            
        elif menu_for == 2:
             print("\n\tRecorrer arreglo")
             aux = 0
             lista = ['Alex', 'Oku', 'Marvin', 'Isaac', 'Cesar']
             while aux != 4:
                print(f"\t{lista[aux]}")
                aux += 1
             
        elif menu_for == 3:
             print("\n\tResuelve la operación ")
             operacion = 0
             while operacion != 36:
                operacion= int(input("\tIngresa el resultado de '((4+5)*2/3)*6' = "))

        elif menu_for == 4:
             print("\tGracias por utilizar While")
             menu_for == 4
        else:
             print("\n\tElegiste un número incorrecto")
    

control()
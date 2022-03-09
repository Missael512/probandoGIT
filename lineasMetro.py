linea2=["Cuatro caminos","Panteones","Tacuba","Cuitlahuac","Popotla","Colegio militar","Normal","San cosme","Revolucion","Hidalgo","Bellas artes","Allende","Zocalo","Pino suares","San antonio abad","Chabacano","Viaducto","Xola","Villa de cortes","Nativitas","Portales","Ermita","General anaya","Tasquena"]

print("Linea disponible: Linea [2]")
while True:
    print("""
    [1] Iniciar recorrido
    [2] Salir
    """)
    op=int(input("Su opcion--> "))
    if op==1:
        print("Inicie el recorrido deseado:")
        inicio = input("Dame el inicio->> ")
        fin = input("Dame el fin->> ")

        if inicio and fin in linea2:
            a = linea2.index(inicio)
            b = linea2.index(fin)
            b += 1
            print(" Inicio y fin validos \n Recorrido:\n")
            if a < b:

                print(linea2[a:b])
            else:
                a += 1
                b -= 1

                l = linea2[b:a]

                print(l[::-1])
        else:
            print("Inicio o fin no encontrado")
    elif op==2:
        print("Out")
        break

    else:
        print("Opcion incorrecta")

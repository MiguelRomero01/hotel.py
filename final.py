
import sqlite3
import os
from os import remove
from random import*

os.mkdir("database") #creacion de la carpeta donde se alamcenarán las bases de datos (comentarear cuando se cree la base de datos)
con = sqlite3.connect("database/hotel.db")   #creacion de base de datos
cur = con.cursor()  

print("""
1.Crear reserva
2.Cancelar reserva
3.Ver reserva""")
dsc_num = int(input("Ingresa un numero del menu:  "))

#crea la tabla donde se alamcenará la base de datos
cur.execute("CREATE TABLE IF NOT EXISTS hotel(persona, adultos, niños, numerodehabitaciones, dia_entrada, mes_entrada, año_entrada, dia_salida, mes_salida)")
con.commit()

if dsc_num == 1:
    DI = int(input("Ingrese su documento de identidad: "))
    print("--------------------------FECHA------------------------")
    print("1.2022 \n2.2023\n3.2024\n")
    año= int(input("ESCOJA EL AÑO EN QUE QUIERE RESERVAR: "))


    # usamos while para especificar la opcion que esta habilitada
    while año!=2:
        año=int(input("la opcion escogida esta inhabilitada. Escoja nuevamente: "))
    if año==2:
        mes=int(input("|escriba mes de entrada (1-12)|: "))
        while mes>12 or mes<1:
            mes=int(input("el mes digitado no exite. Ingresa otro mes: "))
           
        mes2=int(input("|escriba mes de salida (1-12)|: "))
        while mes2>12 or mes2<1:
            mes2=int(input("el mes digitado no exite. Ingresa otro mes: "))
   
    dia=int(input("|digite el dia de ingreso|: "))  
    dia2=int(input( "|escriba cuantos dias desea reservar|: "))
   
    #constantes de precios
    h1= 100;
    h2= 200;
    h3 = 400;
    h4 = 500;
    kid = 50;
    adult = 80;

    print("-----------------------HABITACIONES-----------------------")
    print( f"1.cuartico (basico): ${h1} dia y noche ")
    print( f"2.suit doble cama ${h2} dia y noche")
    print( f"3.suit presidencial (premium) ${h3} dia y noche")
    print( f"4.suit diplomatica (megapremium) ${h4} dia y noche")
    type_room=int(input("¿Qué tipo de habitacion desea ?"))
   
    while type_room < 1 or type_room > 4:
        type_room=int(input("Los numeros no son validos intente de nuevo"))

    reserve=int(input("Cuantas habitaciones desea?(Maximo permitido: 5)\n"))
    #mientras el numero de habitaciones no esté entre 1 y 5, Dirá que lo intente nuevamente.
    while reserve < 1 or reserve > 5:
        reserve=int(input("Lo sentimos, el numero de habitaciones no puede ser apartado. Intentalo nuevamente"))
   
    print("--------------------------PERSONAS------------------------")  
    print( "Para cuantos adultos es la habitacion?")
    N_Adultos=int(input("N_Adultos: ")) #ingresamos cuantos adultos van a entrar en la habitacion))
    while(N_Adultos>4 or N_Adultos<=0):
        if(N_Adultos<=0):
            N_Adultos = int(input("No se puede reservar la habitacion sin adultos, Intente de nuevo:"))
        else:
            N_Adultos = int(input("Son muchos adultos para una habitacion intente de nuevo"))
       
        if(N_Adultos<=4):
            print(N_Adultos," Adultos pueden entrar perfectamente en la habitacion") #si son muhos adultos pondremos que no caben en una sola habitacion
        else:
            print("El numero no es valido") #en caso de que sea decimal o una letra dara que no es un nuero valido
       
       
    N_Niños=int(input("Para cuantos niños es la habitacion?"))
       
    while(N_Niños>4 or N_Niños<0):
        if(N_Niños<0):
            N_Niños=int(input("No puedes poner un numero inferior a 0. Intentalo nuevamente"))
        else:
            N_Niños = int(input("Son muchos niños para una habitacion intente de nuevo"))#si son muchos niños tampoco entraran en la habitacion)
           
        if(N_Niños==0):
            print("Entendemos que ningun niño va a entra a la habitacion")#si no hay niños no hay problema
        elif (N_Niños<=4):
            print(f"{N_Niños} Niños pueden entrar perfectamente en la habitacion")
        else:
            print("El numero no es valido") #en caso de que sea decimal o una letra dara que no es un número valido
       
       
    """---------------OPERACIONES DE LA FACTURA-----------------------------"""
    if type_room== 1:
        price = h1*reserve*dia2*((kid*N_Niños)+(adult*N_Adultos))
       
    elif type_room== 2:
        price = h2*reserve*dia2*((kid*N_Niños)+(adult*N_Adultos))
       
    elif type_room== 3:
        price = h3*reserve*dia2*((kid*N_Niños)+(adult*N_Adultos))
       
    elif type_room== 4:
        price = h4*reserve*dia2*((kid*N_Niños)+(adult*N_Adultos))
   
   
    print("------------------DESCUENTO Y CANCELACION------------------")
    print( "Si tienes un codigo de descuento, ingresalo")
    code=input("code: ")
   
    dsc = str(input("¿Deseas cancelar tu reserva?(si/no)")).lower()
   
        #si el usuario pone "no", genera la factura, de lo contrario cancela todo
    if dsc=="no":
        print("---------------------FACTURA---------------------------")
        salida=dia2+dia #formula para hallar el dia de salida
        print("...tu reservacion ha sido exitosa...\n")
    if  code == "elmejorequipo": #puso el codigo de descuento
        final_dto = (price * 15) / 100; #descuento fijo del 15%
        final_value = price - final_dto


        #ciclo para generar el numero de habitacion
        print("|-------FECHA--------|")
        print(f"|      ingreso      |: {dia}/{mes}/2023\n")
        print(f"|      salida       |: {salida}/{mes2}/2023\n")
        print(f"|  dias de estancia |: {dia2}")
        print("|                    |")
        print("|-----HABITACION-----|")


        for i in range(reserve):
            room = randint(1,250)
            print(f"|    Habitacion {i}     |: {room}")    
        print("|                    |")
        print("|------PERSONAS------|")
        print(f"|       Niños        |: {N_Niños}")
        print(f"|      Adultos       |: {N_Adultos}")
        print(f"|   Total personas   |: {N_Niños+N_Adultos}")
        print(f"|                    |")
        print(f"|-------TOTAL--------|")
        print(f"|      Descuento     |: 15%")
        print(f"|    valor final:    |: ${price}")
        print(f"|--------------------|")
    else: #no tenia el codigo de descuento
        print("|-------FECHA--------|")
        print(f"|      ingreso       |: {dia}/{mes}/2023")
        print(f"|      salida        |: {salida}/{mes2}/2023")
        print(f"|  dias de estancia  |: {dia2}")
        print("|                    |")
        for i in range(reserve):
            room = randint(1,250)
            print(f"|    Habitacion {i}    |: {room}")        
        print("|                    |")
        print("|------PERSONAS------|")
        print(f"|      Adultos       |: {N_Adultos}")
        print(f"|   Total personas   |: {N_Niños+N_Adultos}")
        print("|                    |")
        print("|-------TOTAL--------|")
        print(f"|    valor final:    |:${price}")
        print("|--------------------|")
   
    print("...!GRACIAS POR TU RESERVACION!, TE ESPERAMOS PRONTO...")
   
    #añade los datos de la reserva a la base de datos
    res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
    res.fetchone() is None #está verificando las filas de sql y cuando llegue a la ultima devolverá false y acabará ahi
    cur.execute("INSERT INTO hotel VALUES (?,?,?,?,?,?,?,?,?)", (DI,N_Adultos,N_Niños, reserve,dia, mes, año, salida, mes2))
    con.commit()
   
    filedb = open("database/database_export.txt", 'a') #crea el archivo o lo sobreescribe
    filedb.write(f"""**********************\n
Numero de D.I: {DI}\nNumero de adultos: {N_Adultos}\nNumero de niños: {N_Niños}\nNumero de habitaciones: {reserve}\ndia de entrada: {dia}\ndia de entrada: {mes}\naño de entrada: {año}\ndia de salida: {salida}\nmes de salida:{mes2}\naño de salida: 2023\nPrecio total: {price}""")
    filedb.close()
    if dsc=="si":
        print("\nLo comprendemos, gracias por visitarnos")
    con.close()

if dsc_num == 2:
    DI = int(input("Ingrese su documento de identidad: "))
    cur.execute(f"DELETE FROM hotel WHERE persona = {DI}")
    con.commit()
    print("Su reserva se eliminó exitosamente")
    remove_file = input("Si tiene un archivo .txt lo puede eliminar (si/no): ")
    remove('database/database_export.txt') #elimina el archivo .txt si lo habia creado anteriormente
    con.close()
   
if dsc_num == 3:
    #bucle que imprime toda la db
    for row in cur.execute("SELECT persona, adultos, niños, numerodehabitaciones, dia_entrada, mes_entrada, año_entrada, dia_salida, mes_salida  FROM hotel ORDER BY persona"):
        print(row)
       
    exportdb = str(input("Desea ver la base de datos desde la consola? (si/no) ")).lower()
    if exportdb == "si":
        filedb = open('database/database_export.txt', 'r')
        print(filedb.read())
        filedb.close()
    else:
        print()
    con.close()

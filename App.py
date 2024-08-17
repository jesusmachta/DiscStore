import random
import requests
import copy
import pickle
from Disco import Disco
from Cliente import Cliente
from Staff import Staff
from collections import Counter

class App():
    #metodo construtor, CONTIENE LAS LISTAS DE CLIENTES, DISCOS Y STAFF que estan vacias y se guardan en el txt
    def __init__(self):
        self.discos = []
        self.clientes = []
        self.staff = []
        self.carrito = []
        self.ids = []
        self.ids_carrito = []
        self.veces_regalos = []
        self.discos_comprados = []
    
    #Menu principal que aparecerá al ejecutar el programa y que permite elegir entre cliente o staff 
    def menu_prin(self):
        print("""
        --- ¡Bienvenido a Saman Musica! ---
        """)
        while True:
            s = (input("""
                    ¿Qué desea hacer?
                    Introduzca el número de su elección:
                        ------------------------------
                        1. Staff
                        2. Clientes
                        3. Mostrar Discos Disponibles
                        4. Mostrar Productos Ordenados
                        5. Estadisticas
                        6. Salir
                        ------------------------------
                        Introduzca el número de su elección:
                        
                        """))
            if s != "1" and s != "2" and s != "3" and s != "4" and s != "5" and s != "6":
                print("Error, intente de nuevo: ")
            elif s == "1":
                self.menu_staff()
            elif s == "2":
                self.menu_clientes()
            elif s == "3":
                self.show_discos()
            elif s == "4":
                self.menu_ordenados()
            elif s == "5":
                self.estadisticas()
            elif s == "6":
                print("Gracias por visitarnos! Vuelva Pronto!")
                break

    #Menu que se despliega al ingresar como cliente, aqui el cliente se tiene que registrar o loguear, y puede ver los discos disponibles, agregarlos al carrito, ver el carrito, pagar y salir       
    def menu_clientes(self):
        print("""
        --- ¡Bienvenido Estimado Cliente! ---
        --- De no tener una cuenta, por favor registrece ---
        --- De ya tener una cuenta, puede agregar al carrito ---
        """)
        while True:
            s = (input("""
                    ¿Qué desea hacer?
                    Introduzca el número de su elección:

                        ------------------------------
                        1. Registrar Cliente
                        2. Mostar Productos Ordenados
                        3. Agregar al Carrito de Compras
                        4. Elimnar del Carrito de Compras
                        5. Ver Carrito
                        6. CheckOut
                        7. Regalo
                        8. Atras
                        ------------------------------
                        Introduzca el número de su elección:
                        
                        """))
            if s != "1" and s != "2" and s != "3" and s != "4" and s != "5" and s != "6" and s != "7" and s != "8":
                print("Error, intente de nuevo: ")
            elif s == "1":
                self.agregar_cliente()
                self.escribir_clientes()
            elif s == "3":
                self.agregar_carrito()
                self.escribir_carrito()
                self.escribir_discos()
            elif s == "4":
                self.eliminar_carrito() 
                self.escribir_carrito()
                self.escribir_discos() 
            elif s == "5":
                self.show_carrito()
            elif s == "6":
                self.checkout()
                self.escribir_clientes()
                self.escribir_carrito()
                self.escribir_discos_comprados()
            elif s == "7":
                self.regalo()
            elif s == "2":
                self.menu_ordenados()
            else:
                print("Gracias por visitarnos!")
                break
    
    #Menu que se despliega al ingresar como staff, puede registrarse o loguear, aqui el staff puede ver los discos disponibles, agregarlos al inventario, eliminarlos del inventario y salir
    def menu_staff(self):
        print("""
        --- ¡Bienvenido Estimado Staff! ---
        """)
        while True:
            s = (input("""
                    ¿Qué desea hacer?
                    Introduzca el número de su elección:

                        ------------------------------
                        1. Agregar Staff
                        2. Inventario
                        3. Atras
                        ------------------------------
                        Introduzca el número de su elección:
                        
                        """))
            if s != "1" and s != "2" and s != "3":
                print("Error, intente de nuevo: ")
            elif s == "1":
                self.agregar_staff()
                self.escribir_staff()
            elif s == "2":
                self.inventario()           
            else:
                break
    
    #Funcion que permite al staff entrar en el area de inventario
    def inventario(self):
        cedula = input("Por favor ingrese su cedula asociada al registro del staff: ")
        while not cedula.isnumeric():
            print("Error")
            cedula = input("Por favor ingrese su cedula asociada al registro del staff: ")
        cedula = int(cedula)

        #Aqui valida que la cedula ingresada sea la misma que la del staff que se registro
        for s in self.staff:
            if s.cedula == cedula:
                print("""
                --- ¡Bienvenido Estimado Staff! ---
                """)
                while True:
                    s = (input("""
                            ¿Qué desea hacer?
                            Introduzca el número de su elección:

                                ------------------------------

                                1. Agregar al Inventario
                                2. Eliminar del Inventario
                                3. Mostrar Productos Disponibles
                                4. Atras

                                ------------------------------
                                Introduzca el número de su elección:

                                """))
                    if s != "1" and s != "2" and s != "3" and s != "4":
                        print("Error, intente de nuevo: ")
                    elif s == "1":
                        self.agregar_disco()
                        self.escribir_discos()
                    elif s == "2":
                        self.eliminar_disco()
                        self.escribir_discos()
                    elif s == "3":
                       self.show_discos()
                    else:
                        break

    #Funcion que permite al staff ver la estadia de los clientes y de los discos al final del dia
    def estadisticas(self):
        cedula = input("Por favor ingrese su cedula asociada al registro del staff: ")
        while not cedula.isnumeric():
            print("Error")
            cedula = input("Por favor ingrese su cedula asociada al registro del staff: ")
        cedula = int(cedula)

        #Aqui valida que la cedula ingresada sea la misma que la del staff que se registro
        for s in self.staff:
            if s.cedula == cedula:
                print("""
                --- ¡Bienvenido Estimado Staff! ---
                --- ¡Aqui estan las Estadisticas de la Tienda! ---
                """)
                while True:
                    s = (input("""
                            ¿Qué desea hacer?
                            Introduzca el número de su elección:

                                ------------------------------
        
                                1. Clientes mas Fieles
                                2. Clientes que mas han Gastado
                                3. Géneros mas Vendido
                                4. Artistas mas Vendidos
                                5. Clientes Sin finiquitar compra
                                6. Ingreso Bruto
                                7. Ganancia Neta
                                8. Discos Regalados
                                9. Atras

                                ------------------------------
                                Introduzca el número de su elección:
                                
                                """))
                    if s != "1" and s != "2" and s != "3" and s != "4" and s != "5" and s != "6" and s != "7" and s != "8" and s != "9":
                        print("Error, intente de nuevo: ")
                    elif s == "1":
                        self.clientes_fieles()
                    elif s == "2":
                        self.clientes_gastadores()
                    elif s == "3":
                        self.generos_populares()
                    elif s == "4":
                        self.artistas_populares()           
                    elif s == "5":
                        self.porcentaje_clientes_sin_compras()
                    elif s == "6":
                        self.ingresos_brutos()           
                    elif s == "7":
                        self.ganancias()
                    elif s == "8":
                        self.ordenes_reg()
                    else:
                        break

    #Funcion que despliega el menu para ver el menu ordenado por genero, por artista o por año, por precio o por nombre
    def menu_ordenados(self):
        print("""
               
                """)
        while True:
            s = (input("""

                            ------------------------------------

                            ¿Qué desea hacer?
                            Introduzca el número de su elección:
                            1. Ordenar por Artista
                            2. Ordenar por Precio
                            3. Ordenar por Rock
                            4. Ordenar por Pop
                            5. Ordenar por Rap
                            6. Ordenar por Jazz
                            7. Ordenar por Genero
                            8. Atras

                            ------------------------------------
                            Introduzca el número de su elección:

                                """))
            if s != "1" and s != "2" and s != "3" and s != "4" and s != "5" and s != "6" and s != "7" and s != "8":
                print("Error, intente de nuevo: ")
            elif s == "1":
                self.ordenar_artista()
            elif s == "2":
                self.ordenar__precio()
            elif s == "3":
                self.ordenar_rock()
            elif s == "4":
                self.ordenar_pop()
            elif s == "5":
                self.ordenar_rap()
            elif s == "6":
                self.ordenar_jazz()
            elif s == "7":
                self.ordenar_genero()
            elif s == "8":
                break

    #Funcion que agrega al cliente como objeto a la lista de clientes
    def agregar_cliente(self):

        cedula = input("Por favor ingrese su cedula: ")
        while not cedula.isnumeric():
            print("Error")
            cedula = input("Por favor ingrese su cedula: ")
        cedula = int(cedula)

        discos_comprados = 0
        discos_comprados = int(discos_comprados)
        
        clientes = Cliente(cedula, discos_comprados)
        self.clientes.append(clientes)
        print("Cliente Agregado!")
        self.show_clientes()
    
    #Funcion que muestra los clientes registrados
    def show_clientes(self):
        for c in self.clientes:
            c.show_attr()
    
    #Funcion que agrega al staff como objeto a la lista de staff
    def agregar_staff(self):
        cedula = input("Por favor ingrese su cedula: ")
        while not cedula.isnumeric():
            print("Error")
            cedula = input("Por favor ingrese su cedula: ")
        cedula = int(cedula)

        staffs = Staff(cedula)
        self.staff.append(staffs)
        print("Staff Agregado")
        self.show_staff()
    
    #Funcion que muestra los staff registrados
    def show_staff(self):
        for s in self.staff:
            s.show_attr()

    #Funcion que agrega al disco como objeto a la lista de discos. En esta parte solo puede acceder el staff
    def agregar_disco(self):
        cedula = input("Por favor ingrese su cedula asociada al registro del staff: ")
        while not cedula.isnumeric():
            print("Error")
            cedula = input("Por favor ingrese su cedula asociada al registro del staff: ")
        cedula = int(cedula)

        #Aqui valida que la cedula ingresada sea la misma que la del staff que se registro
        for s in self.staff:
            if s.cedula == cedula:
                
                #Aqui ingresa el id utilizando la libreria random, y verifica que este id sea unico
                ids = random.randint(0,999)
                if ids in self.ids:
                    print("Error el id ya esta registrado")
                    ids = random.randint(0,999)
                    self.ids.append(ids)
                else:
                    self.ids.append(ids)
                print(self.ids)


                titulo = input("Por favor ingrese el titulo del album: ")
                titulo = titulo.title()

                artista = input("Por favor ingrese el artista: ")
                artista = artista.title()

                ano_publicacion = input("Por favor ingrese el año de publiación: ")
                while not ano_publicacion.isnumeric():
                    print("Error")
                    ano_publicacion = input("Por favor ingrese el año de publiación: ")
                ano_publicacion = int(ano_publicacion)

                genero = input("""
                            Por favor ingrese el genero al que pertenece el disco: 
                            1. Rock
                            2. Pop
                            3. Rap
                            4. Jazz
                """)

                while not genero.isnumeric():
                    print("Error")
                    genero = input("Por favor ingrese un numero valido: ")
                if genero == '1':
                    genero = 'Rock'
                elif genero == '2':
                    genero = 'Pop'
                elif genero == '3':
                    genero = 'Rap'
                else:
                    genero = 'Jazz'

                costo = input("Por favor ingrese el costo: ")
                while not costo.isnumeric():
                    print("Error")
                    costo = input("Por favor ingrese el costo: ")
                costo = int(costo)

                precio_venta = input("Por favor ingrese el precio de venta: ")
                while not precio_venta.isnumeric():
                    print("Error")
                    precio_venta = input("Por favor ingrese el precio de venta: ")
                precio_venta = int(precio_venta)

                stock = Disco(ids, titulo, artista, ano_publicacion, genero, costo, precio_venta)
                self.discos.append(stock)
                self.show_discos()
                print("Disco Agregado!")

    #Funcion que muestra los discos registrados
    def show_discos(self):
        for d in self.discos:
            d.show_attr()

    #Función que elimina los discos agregados al inventario
    def eliminar_disco(self):

        cedula = input("Por favor ingrese su cedula asociada al registro del staff: ")
        while not cedula.isnumeric():
            print("Error")
            cedula = input("Por favor ingrese su cedula asociada al registro del staff: ")
        cedula = int(cedula)

        #Aqui valida que la cedula ingresada sea la misma que la del staff que se registro
        for s in self.staff:
            if s.cedula == cedula:    
                self.show_discos()
                ids = input("Por favor ingrese el id del disco: ")
                while not ids.isnumeric():
                    print("Error el id no esta en el inventario o es incorrecto")
                    ids = input("Por favor ingrese el id del disco: ")
                ids = int(ids)

                #Verifica que el id ingresado este en el inventario
                for i, stock in enumerate(self.discos):
                    if stock.ids == ids:
                        self.discos.pop(i)
                        print("Disco Eliminado del Stock!")
                        self.show_discos()

    #Funcion que permite comprar discos, agregarlos al carrito
    def agregar_carrito(self):
        cedula = input("Por favor ingrese su cedula asociada al registro de clientes: ")
        while not cedula.isnumeric():
            print("Error")
            cedula = input("Por favor ingrese su cedula asociada al registro de clientes: ")
        cedula = int(cedula)

        #Aqui valida que la cedula ingresada sea la misma que la del cliente que se registro
        for c in self.clientes:
            if c.cedula == cedula:
                self.show_discos()
                ids = input("Por favor ingrese el id del disco: ")
                while not ids.isnumeric():
                    print("Error el id no esta en el inventario o es incorrecto")
                    ids = input("Por favor ingrese el id del disco: ")
                ids = int(ids)

                #Verifica que el id ingresado este en el inventario, lo agrega a la lista de carrito y lo elimina del inventario
                for i, stock in enumerate(self.discos):
                        if stock.ids == ids:
                            self.carrito.append(stock)
                            self.discos.pop(i)
                            self.ids_carrito.append(stock.ids)
                print("Disco Agregado a su Carrito!")
                print("""

                    A continuación se le muestran los discos que todavian estan en Stock

                """)
                self.show_discos()
                print("""
                    A continuación se le muestra su Carrito!
                    """)
                self.show_carrito()
    
    #Funcion que muestra los discos que estan en el carrito
    def show_ids_carrito(self):
        for i in self.ids_carrito:
            print(i)

    #Funcion que muestra los discos que estan en el carrito para despues eliminarlos del cliente no desearlos
    def eliminar_carrito(self):
        self.show_carrito()
        ids = input("Por favor ingrese el id del disco: ")
        while not ids.isnumeric():
            print("Error el id no esta en el inventario o es incorrecto")
            ids = input("Por favor ingrese el id del disco: ")
        ids = int(ids) 
        for i, stock in enumerate(self.carrito):
            if stock.ids == ids:
                self.discos.append(stock)
                self.carrito.pop(i)
                self.ids_carrito.remove(stock.ids)
                self.show_ids_carrito()
        print("""
            -----------------------------------------------------------------
            Disco Eliminado del Carrito y Agregado nuevamente al Inventario!
            -----------------------------------------------------------------
            """)
        print("""
        -------------------------------------------------------
            A continuación, se le muestran los discos en Stock
        -------------------------------------------------------
        """)
        self.show_discos()
        print("""
        -----------------------------------------------------------------
            A continuación, se le muestran los discos en su Carrito
        -----------------------------------------------------------------
        """)
        self.show_carrito()

    #Funcion que muestra los discos que estan en el carrito
    def show_carrito(self):
        for o in self.carrito:
            o.show_attr()
    
    #Funcion que permite pagar los discos que estan en el carrito
    def checkout(self):
        cedula = input("Por favor ingrese su cedula asociada a su registro como cliente: ")
        while not cedula.isnumeric():
            print("Error")
            cedula = input("Por favor ingrese su cedula asociada a su registro como cliente: ")
        cedula = int(cedula)
        
        for c in self.clientes:
            for o in self.carrito:
                if c.cedula == cedula:
                    self.show_carrito()

                    self.discos_comprados = self.carrito.copy()

                    costo_compra_cliente = sum(i.precio_venta for i in self.carrito)
                    costo_con_iva = costo_compra_cliente + costo_compra_cliente * 0.03
                    for s in self.clientes:
                        s.discos_comprados += 1
                        self.show_clientes()

                    self.regalo()
                    print(f"El costo de su compra es de {costo_compra_cliente} y el costo con IVA es de {costo_con_iva}")
                    print(f'El cliente {c.cedula} debe cancelar {costo_con_iva} por su compra de sus discos')
                    self.carrito.clear()
                    self.ids_carrito.clear()
    
    #Funcion que permite regalar un disco a un cliente que haya la suma del id de su disco sea igual a 7
    def regalo(self):
        res = []
        con_regalos = 0
        for ele in self.ids_carrito:
            sum = 0
            for digit in str(ele):
                sum += int(digit)
            res.append(sum)
        print ("La Suma de los digitos del id es: " + str(res))    
        for num in res:
            if num == 7:
                con_regalos += 1
                self.veces_regalos.append(con_regalos)
                print("Querido cliente, su pedido es un regalo por parte de la Tienda")
                print(f'Se han regalado {con_regalos} ordenes')
            else:
                print("No se aplica la oferta del regalo")

    #Funcion que permite mostrar los clientes fieles, es decir los que mas discos han comprado, haciendo uso de la funcion list, filter y la palabra reservada lambda
    def clientes_fieles(self):
        fieles = list(filter(lambda x: not x.discos_comprados > 1, self.clientes))
        print("Los clientes fieles son: ")
        for f in fieles:
            f.show_attr()

    #Funcion que permite mostrar los clientes que han gastado mas dinero en la tienda
    def clientes_gastadores(self):
        gastadores = list(filter(lambda x: not x.discos_comprados > 1, self.clientes))
        print("Los clientes gastadores son: ")
        for g in gastadores:
            g.show_attr()

    #Funcion que permite mostrar los generos mas populares, haciendo uso de la funcion list, filter y la palabra reservada lambda
    def generos_populares(self):
        generos = list(filter(lambda x: not x.precio_venta > 3, self.discos))
        print("Los generos mas populares son: ")
        for g in generos:
            g.show_attr()

    #Funcion que permite mostrar los artistas mas vendidos, haciendo uso de la funcion list, filter y la palabra reservada lambda
    def artistas_populares(self):
        artistas = list(filter(lambda x: not x.precio_venta > 5, self.discos))
        print("Los artistas mas populares son: ")
        for a in artistas:
            a.show_attr()
    
    #Funcion que muestra el porcentaje de clientes que estan registrados en la tienda mas no han realizado todavia una compra
    def porcentaje_clientes_sin_compras(self):
        clientes_sin_compras = list(filter(lambda x: not x.discos_comprados == 0, self.clientes))
        porcentaje = len(clientes_sin_compras) / len(self.clientes) * 100
        print(f'El porcentaje de clientes sin compras es de {porcentaje}%')

    #Funcion que muestra el ingreso bruto de la tienda haciendo uso de la funcion sum que suma los precios de venta del carrito de los clientes
    def ingresos_brutos(self):
        vendido = sum(i.precio_venta for i in self.discos_comprados)
        print(f'El ingreso bruto de la tienda es de {vendido}$')
    
    #Funcion que muestra las ganancias de la tienda, sumando el ingreso bruto menos el costo de los discos
    def ganancias(self):
        ventas = sum(i.precio_venta for i in self.discos_comprados)
        costo_ventas = sum(i.costo for i in self.discos)
        invertido = sum(i.costo for i in self.discos)
        costos = invertido + costo_ventas
        neta = costos - ventas
        print(f'La ganancia neta es de: {neta}$')

    #Funcion que muestra cuantas ordenes se han regalado
    def ordenes_reg(self):
        ordenes_regaladas = len(self.veces_regalos)
        print(f'La cantidad de ordenes regaladas es de: {ordenes_regaladas}')

    #Funcion que muestra los discos ordenados por precio
    def ordenar__precio(self):
        por_precio = list(filter(lambda x: x.precio_venta > 1, self.discos))
        por_precio.sort(key=lambda x: x.precio_venta)
        print("Los discos ordenados por precio son: ")
        for d in por_precio:
            d.show_attr()

    #Funcion que muestra los discos ordenados por rock
    def ordenar_rock(self):
        por_rock = list(filter(lambda x: x.genero == 'Rock', self.discos))
        for i in por_rock:
            i.show_attr()

    #Funcion que muestra los discos ordenados por pop
    def ordenar_pop(self):
        por_pop = list(filter(lambda x: x.genero == 'Pop', self.discos))
        for i in por_pop:
            i.show_attr()

    #Funcion que muestra los discos ordenados por rap
    def ordenar_rap(self):
        por_rap = list(filter(lambda x: x.genero == 'Rap', self.discos))
        for i in por_rap:
            i.show_attr()

    #Funcion que muestra los discos ordenados por jazz
    def ordenar_jazz(self):
        por_jazz = list(filter(lambda x: x.genero == 'Jazz', self.discos))
        for i in por_jazz:  
            i.show_attr()
    
    #Funcion que muestra los discos ordenados por genero en orden alfabetico
    def ordenar_genero(self):
        por_genero = list(sorted(self.discos, key=lambda x: x.genero))
        for i in por_genero:
            i.show_attr()
    
    #Funcion que muestra los discos ordenados por artista en orden alfabetico
    def ordenar_artista(self):
        por_artista = list(sorted(self.discos, key=lambda x: x.artista))
        for i in por_artista:
            i.show_attr()

    #De aqui en adelante, es donde las listas se guardan en un archivo .txt, haciendo uso del pickle.dump, luego se encuentra la funcion que lee cada archivo .txt y lo guarda en una lista, haciendo uso del pickle.load
    def escribir_discos(self):
       archivo = open('discos.txt', 'wb+')
       pickle.dump(self.discos, archivo)
       archivo.close()
    
    def leer_discos_bin(self):
        archivo = open("discos.txt", "rb+")
        self.discos = pickle.load(archivo)
        archivo.close()
        for d in self.discos:
            print("""
            ---------------------------
            Los discos disponibles son:
            ---------------------------
            """)
            d.show_attr()

    def escribir_clientes(self):
       archivo = open("clientes.txt", "wb+")
       pickle.dump(self.clientes, archivo)
       archivo.close()

    def leer_clientes_bin(self):
        archivo = open("clientes.txt", "rb+")
        self.clientes = pickle.load(archivo)
        archivo.close()
        for c in self.clientes:
            print("""
            ------------------------
            Los clientes son:
            ------------------------
            """)
            c.show_attr()
    
    def escribir_carrito(self):
       archivo = open("carrito.txt", "wb+")
       pickle.dump(self.carrito, archivo)
       archivo.close()
    
    def leer_carrito_bin(self):
        archivo = open("carrito.txt", "rb+")
        self.carrito = pickle.load(archivo)
        archivo.close()
        for c in self.carrito:
            print("""
            ------------------------
            El carrito contiene:
            ------------------------
            """)
            c.show_attr()
    
    def escribir_staff(self):
         archivo = open("staff.txt", "wb+")
         pickle.dump(self.staff, archivo)
         archivo.close()
        
    def leer_staff_bin(self):
        archivo = open("staff.txt", "rb+")
        self.staff = pickle.load(archivo)
        archivo.close()
        for s in self.staff:
            print("""
            ------------------------
            El Staff es:
            ------------------------
            """)
            s.show_attr()

    def escribir_ids(self):
        archivo = open("id.txt", "wb+")
        pickle.dump(self.ids, archivo)
        archivo.close()

    def leer_ids_bin(self):
        archivo = open("id.txt", "rb+")
        self.ids = pickle.load(archivo)
        archivo.close()
        for i in self.ids:
            i.show_attr()

    def escribir_ids_carrito(self):
        archivo = open("id_carrito.txt", "wb+")
        pickle.dump(self.ids_carrito, archivo)
        archivo.close()
    
    def leer_ids_carrito_bin(self):
        archivo = open("id_carrito.txt", "rb+")
        self.ids_carrito = pickle.load(archivo)
        archivo.close()
        for i in self.ids_carrito:
            i.show_attr()

    def escribir_veces_regalos(self):
        archivo = open("veces_regalos.txt", "wb+")
        pickle.dump(self.veces_regalos, archivo)
        archivo.close()
    
    def leer_veces_regalos_bin(self):
        archivo = open("veces_regalos.txt", "rb+")
        self.veces_regalos = pickle.load(archivo)
        archivo.close()
        for i in self.veces_regalos:
            i.show_attr()
    
    def escribir_discos_comprados(self):
        archivo = open("discos_comprados.txt", "wb+")
        pickle.dump(self.discos_comprados, archivo)
        archivo.close()

    def leer_discos_comprados_bin(self):
        archivo = open("discos_comprados.txt", "rb+")
        self.discos_comprados = pickle.load(archivo)
        archivo.close()
        for i in self.discos_comprados:
            print("""
            ------------------------------------------
            Los discos comprados por los clientes son:
            ------------------------------------------
            """)
            i.show_attr()

    def escribir_archivos(self):
        self.escribir_discos()
        self.escribir_clientes()
        self.escribir_carrito()
        self.escribir_staff()
        self.escribir_ids()
        self.escribir_ids_carrito()
        self.escribir_veces_regalos()
        self.escribir_discos_comprados()

    #Funcion que llama a todas las funciones de leer archivos binarios
    def leer_archivos_bin(self):
        self.leer_discos_bin()
        self.leer_clientes_bin()
        self.leer_carrito_bin()
        self.leer_staff_bin()
        self.leer_ids_bin()
        self.leer_ids_carrito_bin()
        self.leer_veces_regalos_bin()
        self.leer_discos_comprados_bin()

    #Funcion que llama a la funcion que contiene la lectura de archivos txt binarios y realiza el calling del menu princpial que se muestra al iniciar el programa
    def start(self):
        #self.escribir_archivos()
        self.leer_archivos_bin()
        self.menu_prin()
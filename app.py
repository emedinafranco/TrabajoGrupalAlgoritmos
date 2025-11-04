import estilos
import re
import json

productos = []
proveedores = []
def guardar_datos():
    with open ("productos.json", "w") as arch_prod:
        json.dump(productos, arch_prod, indent=4)
    with open ("proveedores.json", "w") as arch_prov:
        json.dump(proveedores, arch_proov, indent=4)  

def cargar_datos():
    global productos, proveedores
    try:
        with open ("productos.json", "r") as arch_prod: 
            productos=json.load(arch_prod)
    except FileNotFoundError:
        productos= []
    try:
        with open ("proveedores.json", "r") as arch_prov:
            proveedores= json.load(arch_prov) 
    except FileNotFoundError:
        proveedores= []


def agregar_productos():
    estilos.imprimir_titulo("Registro de producto", estilos.COLOR_BLUE)
    id_producto = int(input("Ingrese un número de identificación para el producto: "))
    if verificar_productos(id_producto,productos):
        print("El ID ya existe")
    else:

        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = input("Ingrese el precio del producto: ")
        stock = input("Ingrese cuántos productos se agregan al stock: ")

        if nombre_producto == "" or precio_producto == "" or stock == "":
            print("Error, datos incompletos o inválidos, reintente.")
        else:
            precio_producto = float(precio_producto)
            stock = int(stock)

            if precio_producto <= 0 or stock < 0:
                print("Error. El precio debe ser mayor a 0 y no puede haber stock negativo.")
            else:
                datos_producto = {
                    "ID Producto": id_producto,
                    "Nombre": nombre_producto,
                    "Precio": precio_producto,
                    "Stock": stock
                }
                productos.append(datos_producto)
                print("El producto fue agregado con éxito.")


def verificar_productos(id_productos,productos):
    for id in productos:
        if id["ID Producto"] == id_productos:
            return True
    return False

def modificar_producto():
    id_productos = int(input("Ingrese el ID del producto a modificar: "))
    encontrado = False

    for producto in productos:
        if producto["ID Producto"] == id_productos:
            encontrado = True
            print("Producto encontrado")
            print(f"Nombre: {producto['Nombre']}")
            print(f"Precio: {producto['Precio']}")
            print(f"Stock: {producto['Stock']}")

            print("\n¿Qué desea modificar?")

            print("1. Precio")
            print("2. Stock")

            opcion = int(input("Ingrese opción: "))
            
            if opcion == 1:
                nuevo_precio = float(input("Ingrese el precio nuevo: "))
                producto["Precio"] = nuevo_precio
                print("Precio Actulizado")
            
            elif opcion == 2:
                nuevo_stock = int(input("Ingrese el nuevo stock: "))
                producto["Stock"] = nuevo_stock
                print("Stock Actualizado")
            else:
                print("Opción incorrecta")
                opcion = int(input("Ingrese opción: "))
            break
    
    
    
    if not encontrado:
        print("No se encontró el producto deseado")
            




def listado_de_productos():
    estilos.imprimir_titulo("Lista de productos", estilos.COLOR_BLUE)
    if len(productos) == 0:
        print("No hay productos ingresados")
    else:
        i = 1
        for p in productos:
            print(i, "- ID:", p["ID Producto"], " - Nombre:", p["Nombre"], "- Precio:", p["Precio"], "- Stock:", p["Stock"])
            i += 1

def lista_precios_con_iva(productos):
    estilos.imprimir_titulo("Listado de precios con IVA", estilos.COLOR_BLUE)
    return list(map(lambda p: (p["Nombre"], p["Precio"] * 1.21), productos))

def registro_de_proveedores():
    
    estilos.imprimir_titulo("-- Registro de proveedores --", estilos.COLOR_BLUE)
    id_proveedor = int(input("Ingrese un número de identificación para el proveedor: "))
    if verificar_proveedores(id_proveedor,proveedores):
        print("El ID ya existe")
    else:
        nombre_proveedor = input("Ingrese el nombre del proveedor: ")
        telefono_proveedor = input("Ingrese número de teléfono: ")
        patron = ".*@.*"
        correo_electronico_proveedor = input("Ingrese el email del proveedor: ")
        while not re.match(patron,correo_electronico_proveedor):
            print("Mail Incorrecto, debe tener mínimo un @")
            correo_electronico_proveedor = input("Ingrese el email del proveedor: ")
        
        print("Mail correcto")

        if nombre_proveedor == "" or telefono_proveedor == "" or correo_electronico_proveedor == "":
            print("Datos incompletos, reingrese.")
        else:
            datos_proveedor = {
                "ID Proveedor": id_proveedor,
                "Nombre": nombre_proveedor,
                "Teléfono": telefono_proveedor,
                "Correo electrónico": correo_electronico_proveedor
            }
            proveedores.append(datos_proveedor)
            print("Proveedor registrado exitosamente.")

def verificar_proveedores(id_proveedor,proveedores):
    for id in proveedores:
        if id["ID Proveedor"] == id_proveedor:
            return True
    return False

def listado_de_proveedores():
    estilos.imprimir_titulo("-- Lista de proveedores --", estilos.COLOR_BLUE)
    if len(proveedores) == 0:
        print("No hay proveedores registrados")
    else:
        i = 1
        for p in proveedores:
            print(i, ". - Nombre:", p["Nombre"], "- Teléfono:", p["Teléfono"], "- Correo:", p["Correo electrónico"])
            i += 1
def buscar_proveedor(nombre):
    return list(filter(lambda p: p["Nombre"].lower() == nombre.lower(), proveedores))
def estadisticas_stock():
    if len (productos)== 0:
        print("No se ingresaron productos")
    else:
        total = 0
        max_precio = 0
        min_precio = float("inf")
        nombre_caro = ""
        nombre_barato = ""

        for p in productos:
            total += p["Precio"] * p["Stock"]

            if p["Precio"] > max_precio:
                max_precio = p["Precio"]
                nombre_caro = p["Nombre"]

            if p["Precio"] < min_precio:
                min_precio = p["Precio"]
                nombre_barato = p["Nombre"]

        promedio = total / len(productos)

    print("Estadisticas del stock")
    print("Valor total del stock: $", total)
    print("Precio promedio: $", (promedio))
    print("Producto mas caro:", nombre_caro, "($", max_precio, ")")
    print("Producto mas barato:", nombre_barato, "($", min_precio, ")")
def filtrar_stock_bajo():
    if len(productos) == 0:
        print("No hay productos cargados.")
        
    else:
        print("Productos con stock bajo")
        hay_bajos = False
        for p in productos:
            if p["Stock"] < 5:
                print(p["Nombre"], "- Stock:", p["Stock"])
                hay_bajos = True

        if not hay_bajos:
            print("No hay productos con stock bajo.")
def menu():
    while True:
        
        estilos.mostrar_menu_principal()

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar_productos()
        elif opcion == "2":
            listado_de_productos()
        elif opcion == "3":
            registro_de_proveedores()
        elif opcion == "4":
            listado_de_proveedores()
        elif opcion == "5":
            modificar_producto()
        elif opcion == "6":
            if len(productos) == 0:
                print("No hay productos ingresados.")
            else:
                precios_iva = lista_precios_con_iva(productos)
                for nombre, precio in precios_iva:
                    print(f"{nombre} - Precio con IVA: ${precio}")
        elif opcion == "7":
            if len (proveedores)== 0:
                print("No se ingresaron proveedores.")
            else:    
               nombre = input("Ingrese el nombre del proveedor a buscar: ")
               busqueda_proveedor = buscar_proveedor(nombre)
               if busqueda_proveedor:
                   for p in busqueda_proveedor:
                       print(f"Proveedor: {p['Nombre']} - Teléfono: {p['Teléfono']} - Correo: {p['Correo electrónico']}")
               else:
                  print("No se encontró ningún proveedor con ese nombre.")  
        elif opcion == "8":
            estadisticas_stock()    
        elif opcion == "0":
                guardar_datos()
                print("Saliendo del sistema...")
                break 
        else:
            print("Opción inválida, intente nuevamente.")

# Ejecutar el menú
cargar_datos()
menu()

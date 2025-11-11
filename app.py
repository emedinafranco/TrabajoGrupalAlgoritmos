import estilos
import re
import os
import json

productos = []
proveedores = []

"""Definición de patrones de validación usando expresiones regulares."""
patron_string = "^[A-Za-z\s]+$"
patron_positivos = "^[1-9][0-9]*(\.[0-9]+)?$"
patron_id = "^[0-9]{4}$"
patron_telefono = "^[0-9]{8}$"
patron_correo = ".*@.*"

def guardar_datos():
    with open("productos.json", "w") as arch_prod:
        json.dump(productos, arch_prod, indent=4)
    with open("proveedores.json", "w") as arch_prov:
        json.dump(proveedores, arch_prov, indent=4)

def cargar_datos():
    global productos, proveedores
    try:
        with open("productos.json", "r") as arch_prod:
            productos = json.load(arch_prod)
    except FileNotFoundError:
        productos = []
    try:
        with open("proveedores.json", "r") as arch_prov:
            proveedores = json.load(arch_prov)
    except FileNotFoundError:
        proveedores = []

def verificar_productos(id_productos, productos):
    for id in productos:
        if id["ID Producto"] == id_productos:
            return True
    return False

def verificar_proveedores(id_proveedor, proveedores):
    for prov in proveedores:
        if prov["ID Proveedor"] == id_proveedor:
            return True
    return False

def agregar_productos():
    estilos.imprimir_titulo("Registro de producto", estilos.COLOR_BLUE)
    id_producto = int(input("Ingrese un número de identificación para el producto: "))
    while not re.match(patron_id, str(id_producto)):
        estilos.notification("warn", "El ID debe tener 4 dígitos")
        id_producto = int(input("Ingrese un número de identificación para el producto: "))
    estilos.notification("ok", "ID correcto")
    
    if verificar_productos(id_producto, productos):
        estilos.notification("error", "El ID ya existe")
    else:
        nombre_producto = input("Ingrese el nombre del producto: ")
        while not re.match(patron_string, nombre_producto):
            estilos.notification("warn", "Nombre incorrecto, solo letras y espacios permitidos\n")
            nombre_producto = input("Ingrese el nombre del producto: ")
        estilos.notification("ok", "Nombre correcto")
        
        precio_producto = input("Ingrese el precio del producto: ")
        while not re.match(patron_positivos, precio_producto):
            estilos.notification("warn", "Precio incorrecto, debe ser un número positivo\n")
            precio_producto = input("Ingrese el precio del producto: ")
        estilos.notification("ok", "Precio correcto")
        
        stock = input("Ingrese cuántos productos se agregan al stock: ")
        while not re.match(patron_positivos, stock):
            estilos.notification("warn", "Stock incorrecto, debe ser un número entero positivo\n")
            stock = input("Ingrese cuántos productos se agregan al stock: ")
        estilos.notification("ok", "Stock ingresado correctamente")

        if nombre_producto == "" or precio_producto == "" or stock == "":
            estilos.notification("error", "Error, datos incompletos o inválidos, reintente.")
        else:
            precio_producto = float(precio_producto)
            stock = int(stock)

            if precio_producto <= 0 or stock < 0:
                estilos.notification("error", "Error. El precio debe ser mayor a 0 y no puede haber stock negativo.")
            else:
                datos_producto = {
                    "ID Producto": id_producto,
                    "Nombre": nombre_producto,
                    "Precio": precio_producto,
                    "Stock": stock
                }
                productos.append(datos_producto)
                estilos.notification("ok", "El producto fue agregado con éxito.")
                guardar_datos()

def modificar_producto():
    id_productos = int(input("Ingrese el ID del producto a modificar: "))
    encontrado = False

    for producto in productos:
        if producto["ID Producto"] == id_productos:
            encontrado = True
            estilos.notification("info", "Producto encontrado")
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
                estilos.notification("ok", "Precio Actualizado")
                guardar_datos()
            elif opcion == 2:
                nuevo_stock = int(input("Ingrese el nuevo stock: "))
                producto["Stock"] = nuevo_stock
                estilos.notification("ok", "Stock Actualizado")
                guardar_datos()
            else:
                estilos.notification("error", "Opción incorrecta")
            break
    
    if not encontrado:
        estilos.notification("warn", "No se encontró el producto deseado")

def listado_de_productos():
    estilos.imprimir_titulo("Lista de productos", estilos.COLOR_BLUE)
    if len(productos) == 0:
        estilos.notification("warn", "No hay productos ingresados")
    else:
        i = 1
        for p in productos:
            print(i, "- ID:", p["ID Producto"], " - Nombre:", p["Nombre"], "- Precio:", p["Precio"], "- Stock:", p["Stock"])
            i += 1

def lista_precios_con_iva(productos):
    return list(map(lambda p: (p["Nombre"], p["Precio"] * 1.21), productos))

def listado_de_productos_iva():
    estilos.imprimir_titulo("Listado de precios con IVA", estilos.COLOR_BLUE)
    if len(productos) == 0:
        estilos.notification("warn", "No hay productos ingresados")
    else:
        precios_iva = lista_precios_con_iva(productos)
        for nombre, precio in precios_iva:
            print(f"{nombre} - Precio con IVA: ${precio:.2f}")

def registro_de_proveedores():
    estilos.imprimir_titulo("-- Registro de proveedores --", estilos.COLOR_BLUE)
    
    id_proveedor = int(input("Ingrese un número de identificación para el proveedor: "))
    while not re.match(patron_id, str(id_proveedor)):
        estilos.notification("warn", "El ID debe tener 4 dígitos")
        id_proveedor = int(input("Ingrese un número de identificación para el proveedor: "))
    estilos.notification("ok", "ID correcto")
    
    if verificar_proveedores(id_proveedor, proveedores):
        estilos.notification("error", "El ID ya existe")
    else:
        nombre_proveedor = input("Ingrese el nombre del proveedor: ")
        while not re.match(patron_string, nombre_proveedor):
            estilos.notification("warn", "Nombre incorrecto, solo letras y espacios permitidos\n")
            nombre_proveedor = input("Ingrese el nombre del proveedor: ")
        estilos.notification("ok", "Nombre correcto")
        
        telefono_proveedor = input("Ingrese número de teléfono: ")
        while not re.match(patron_telefono, telefono_proveedor):
            estilos.notification("warn", "Teléfono incorrecto, debe tener 8 dígitos\n")
            telefono_proveedor = input("Ingrese número de teléfono: ")
        estilos.notification("ok", "Teléfono correcto")
        
        correo_electronico_proveedor = input("Ingrese el email del proveedor: ")
        while not re.match(patron_correo, correo_electronico_proveedor):
            estilos.notification("warn", "Mail Incorrecto, debe tener mínimo un @")
            correo_electronico_proveedor = input("Ingrese el email del proveedor: ")
        estilos.notification("ok", "Mail correcto")

        if nombre_proveedor == "" or telefono_proveedor == "" or correo_electronico_proveedor == "":
            estilos.notification("error", "Datos incompletos, reingrese.")
        else:
            datos_proveedor = {
                "ID Proveedor": id_proveedor,
                "Nombre": nombre_proveedor,
                "Teléfono": telefono_proveedor,
                "Correo electrónico": correo_electronico_proveedor
            }
            proveedores.append(datos_proveedor)
            estilos.notification("ok", "Proveedor registrado exitosamente.")
            guardar_datos()

def listado_de_proveedores():
    estilos.imprimir_titulo("-- Lista de proveedores --", estilos.COLOR_BLUE)
    if len(proveedores) == 0:
        estilos.notification("warn", "No hay proveedores registrados")
    else:
        i = 1
        for p in proveedores:
            print(i, ". - Nombre:", p["Nombre"], "- Teléfono:", p["Teléfono"], "- Correo:", p["Correo electrónico"])
            i += 1

def buscar_proveedor(nombre):
    return list(filter(lambda p: p["Nombre"].lower() == nombre.lower(), proveedores))

def estadisticas_stock():
    if len(productos) == 0:
        estilos.notification("warn", "No se ingresaron productos")
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

        estilos.mostrar_estadisticas(total, promedio, nombre_caro, max_precio, nombre_barato, min_precio)


def filtrar_stock_bajo():
    if len(productos) == 0:
        estilos.notification("warn", "No hay productos cargados.")
    else:
        print("\nProductos con stock bajo:")
        hay_bajos = False
        for p in productos:
            if p["Stock"] < 5:
                print(f"{p['Nombre']} - Stock: {p['Stock']}")
                hay_bajos = True

        if not hay_bajos:
            estilos.notification("info", "No hay productos con stock bajo.")

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_enter():
    input("\nPresione Enter para continuar...")

def menu():
    cargar_datos()
    
    while True:
        try:
            estilos.mostrar_menu_principal()
            opcion = int(input("Ingrese una opción: "))
            
            if opcion == 1:
                agregar_productos()
            elif opcion == 2:
                listado_de_productos()
            elif opcion == 3:
                registro_de_proveedores()
            elif opcion == 4:
                listado_de_proveedores()
            elif opcion == 5:
                modificar_producto()
            elif opcion == 6:
                listado_de_productos_iva()
            elif opcion == 7:
                if len(proveedores) == 0:
                    estilos.notification("warn", "No se ingresaron proveedores.")
                else:
                    nombre = input("Ingrese el nombre del proveedor a buscar: ")
                    busqueda_proveedor = buscar_proveedor(nombre)
                    if busqueda_proveedor:
                        for p in busqueda_proveedor:
                            print(f"Proveedor: {p['Nombre']} - Teléfono: {p['Teléfono']} - Correo: {p['Correo electrónico']}")
                    else:
                        estilos.notification("warn", "No se encontró ningún proveedor con ese nombre.")
            elif opcion == 8:
                estadisticas_stock()
            elif opcion == 9:
                filtrar_stock_bajo()
            elif opcion == 0:
                if estilos.comfirma_accion("¿Está seguro que desea salir?"):
                    guardar_datos()
                    print("Saliendo del sistema...")
                    break
            else:
                estilos.notification("error", "Opción inválida, intente nuevamente...")
        except ValueError:
            estilos.notification("error", "Error... Ingrese una opción numérica")
        except Exception as e:
            estilos.notification("error", f"Error inesperado: {str(e)}")
        
        esperar_enter()
        limpiar_pantalla()

#Ejecutar el rpograma
menu()
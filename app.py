productos = []
proveedores = []

def agregar_productos():
    print("-- Registro de producto --")
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
                "Nombre": nombre_producto,
                "Precio": precio_producto,
                "Stock": stock
            }
            productos.append(datos_producto)
            print("El producto fue agregado con éxito.")

def listado_de_productos():
    print("-- Lista de productos --")
    if len(productos) == 0:
        print("No hay productos ingresados")
    else:
        i = 1
        for p in productos:
            print(i, ". - Nombre:", p["Nombre"], "- Precio:", p["Precio"], "- Stock:", p["Stock"])
            i += 1

def registro_de_proveedores():
    print("-- Registro de proveedores --")
    nombre_proveedor = input("Ingrese el nombre del proveedor: ")
    telefono_proveedor = input("Ingrese número de teléfono: ")
    correo_electronico_proveedor = input("Ingrese el email del proveedor: ")

    if nombre_proveedor == "" or telefono_proveedor == "" or correo_electronico_proveedor == "":
        print("Datos incompletos, reingrese.")
    else:
        datos_proveedor = {
            "Nombre": nombre_proveedor,
            "Teléfono": telefono_proveedor,
            "Correo electrónico": correo_electronico_proveedor
        }
        proveedores.append(datos_proveedor)
        print("Proveedor registrado exitosamente.")

def listado_de_proveedores():
    print("-- Lista de proveedores --")
    if len(proveedores) == 0:
        print("No hay proveedores registrados")
    else:
        i = 1
        for p in proveedores:
            print(i, ". - Nombre:", p["Nombre"], "- Teléfono:", p["Teléfono"], "- Correo:", p["Correo electrónico"])
            i += 1

def menu():
    while True:
        print("\n--- Sistema de gestión ---")
        print("1- Alta de producto")
        print("2- Listado de productos")
        print("3- Alta de proveedores")
        print("4- Listado de proveedores")
        print("5- Salir")

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
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

# Ejecutar el menú
menu()

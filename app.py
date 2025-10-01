import estilos

productos = []
proveedores = []

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

def listado_de_productos():
    estilos.imprimir_titulo("Lista de productos", estilos.COLOR_BLUE)
    if len(productos) == 0:
        print("No hay productos ingresados")
    else:
        i = 1
        for p in productos:
            print(i, "- ID:", p["ID Producto"], " - Nombre:", p["Nombre"], "- Precio:", p["Precio"], "- Stock:", p["Stock"])
            i += 1

def registro_de_proveedores():
    estilos.imprimir_titulo("-- Registro de proveedores --", estilos.COLOR_BLUE)
    id_proveedor = int(input("Ingrese un número de identificación para el proveedor: "))
    if verificar_proveedores(id_proveedor,proveedores):
        print("El ID ya existe")
    else:
        nombre_proveedor = input("Ingrese el nombre del proveedor: ")
        telefono_proveedor = input("Ingrese número de teléfono: ")
        correo_electronico_proveedor = input("Ingrese el email del proveedor: ")

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
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

# Ejecutar el menú
menu()

import estilos
import re
import os
import json

productos = []
proveedores = []

"""Definición de patrones de validación usando expresiones regulares."""
patron_string = "^[A-Za-z\s]+$"
patron_positivos = "^[1-9][0-9]*([0-9]+)?$"
patron_id = "^[0-9]{4}$"
patron_telefono = "^[0-9]{8}$"
patron_correo = ".*@.*"

def guardar_datos():
    """
    Guarda en archivos JSON los datos actuales de productos y proveedores.

    Archivos generados:
        - productos.json
        - proveedores.json

    Si ocurre un FileNotFoundError (por ejemplo, la carpeta no existe),
    la función simplemente lo ignora.

    Returns:
        None
    """
    try:
       with open("productos.json", "w") as arch_prod:
          json.dump(productos, arch_prod, indent=4)
    except Exception as e:
        print("Error al generar el archivo de productos."+ e)  
    try:    
        with open("proveedores.json", "w") as arch_prov:
          json.dump(proveedores, arch_prov, indent=4)
    except Exception as e:
        print("Error al generar el archivo de proveedores"+ e)      
    

def cargar_datos():
    """
    Carga desde archivos JSON los datos almacenados de productos y proveedores.

    Si los archivos no existen, inicializa las listas como listas vacías para evitar errores.

    Globals:
        productos (list): Se actualiza con los datos cargados.
        proveedores (list): Se actualiza con los datos cargados.

    Returns:
        None
    """
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
    """
    Verifica si un ID de producto ya existe en la lista de productos.

    Args:
        id_productos (int): ID a buscar.
        productos (list): Lista de productos cargados.

    Returns:
        True si el ID existe, False en caso contrario.
    """
    for id in productos:
        if id["ID Producto"] == id_productos:
            return True
    return False

def verificar_proveedores(id_proveedor, proveedores):
    """
    Verifica si un ID de proveedor ya existe en la lista de proveedores.

    Args:
        id_proveedor (int): ID a buscar.
        proveedores (list): Lista de proveedores registrados.

    Returns:
        bool: True si el ID existe, False si no existe.
    """
    for prov in proveedores:
        if prov["ID Proveedor"] == id_proveedor:
            return True
    return False

def agregar_productos():
    """
    Permite registrar un nuevo producto solicitando datos al usuario.
    
    Validaciones:
        - ID de 4 digitos.
        - Nombre solo con letras y espacios.
        - Precio positivo.
        - Stock positivo.

    Si todos los datos son válidos, agrega el producto a la lista global
    y actualiza el archivo JSON.

    Returns:
        None
    """    
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
    """
    Permite modificar el precio o el stock de un producto existente.

    El usuario ingresa el ID del producto y elige que campo modificar.
    Si el producto no se encuentra, muestra un mensaje de advertencia.

    Cambios posibles:
        1. Precio
        2. Stock

    Luego de modificar el producto, guarda los cambios en el JSON.

    Returns:
        None
    """    
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
    """
    Muestra por pantalla todos los productos registrados, con su ID,
    nombre, precio y stock.

    Si no hay productos, informa al usuario.

    Returns:
        None
    """
    estilos.imprimir_titulo("Lista de productos", estilos.COLOR_BLUE)
    if len(productos) == 0:
        estilos.notification("warn", "No hay productos ingresados")
    else:
        i = 1
        for p in productos:
            print(i, "- ID:", p["ID Producto"], " - Nombre:", p["Nombre"], "- Precio:", p["Precio"], "- Stock:", p["Stock"])
            i += 1

def lista_precios_con_iva(productos):
    """
    Calcula el precio de cada producto con IVA (21%).

    Args:
        productos (list): Lista de productos.

    Returns:
        list: Lista de tuplas (nombre, precio_con_iva).
    """    
    return list(map(lambda p: (p["Nombre"], p["Precio"] * 1.21), productos))

def listado_de_productos_iva():
    """
    Muestra la lista de productos con sus precios ya calculados con IVA.

    Si no hay productos, se muestra un aviso.

    Returns:
        None
    """    
    estilos.imprimir_titulo("Listado de precios con IVA", estilos.COLOR_BLUE)
    if len(productos) == 0:
        estilos.notification("warn", "No hay productos ingresados")
    else:
        precios_iva = lista_precios_con_iva(productos)
        for nombre, precio in precios_iva:
            print(f"{nombre} - Precio con IVA: ${precio:.2f}")

def registro_de_proveedores():
    """
    Registra un nuevo proveedor solicitando datos al usuario.

    Validaciones:
        - ID de 4 dígitos unico.
        - Nombre solo letras y espacios.
        - Teléfono de 8 digitos.
        - Email que contenga '@'.

    Si los datos son validos, se guarda el proveedor en la lista global
    y se actualizan los archivos JSON.

    Returns:
        None
    """    
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
    """
    Muestra en pantalla todos los proveedores registrados.

    Incluye:
        - Nombre
        - Teléfono
        - Correo electrónico

    Returns:
        None
    """    
    estilos.imprimir_titulo("-- Lista de proveedores --", estilos.COLOR_BLUE)
    if len(proveedores) == 0:
        estilos.notification("warn", "No hay proveedores registrados")
    else:
        i = 1
        for p in proveedores:
            print(i, ". - Nombre:", p["Nombre"], "- Teléfono:", p["Teléfono"], "- Correo:", p["Correo electrónico"])
            i += 1

def buscar_proveedor(nombre):
    """
    Busca proveedores cuyo nombre coincida con el ingresado
    (no distingue mayúsculas/minúsculas).

    Args:
        nombre (str): Nombre a buscar.

    Returns:
        Lista de proveedores coincidentes.
    """    
    return list(filter(lambda p: p["Nombre"].lower() == nombre.lower(), proveedores))

def estadisticas_stock():
    """
    Calcula y muestra estadísticas del stock actual.

    Incluye:
        - Valor total del stock (precio * cantidad)
        - Precio promedio
        - Producto más caro
        - Producto más barato

    Returns:
        None
    """    
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
    """
    Muestra todos los productos cuyo stock es inferior a 5 unidades.

    Si no hay productos con stock bajo, informa al usuario.

    Returns:
        None
    """    
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

def productos_mayores_a(productos, precio_minimo):
    """
    Devuelve una lista con los nombres de los productos cuyo precio
    es mayor al precio indicado. Utiliza listas por comprension.

    Parametros:
        productos (lista): Lista de diccionarios con información de productos.
        precio_minimo (float): Valor umbral para filtrar productos.

    Returns:
        lista: Lista de nombres de productos cuyo precio es mayor al mínimo.

    Ejemplo:
        productos_mayores_a(productos, 1000)
    """
    return [p["Nombre"] for p in productos if p["Precio"] > precio_minimo]

def limpiar_pantalla():
    """
    Limpia la pantalla de la consola dependiendo del sistema operativo.

    - Windows → 'cls'
    - Linux/Mac → 'clear'

    Returns:
        None
    """    
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_enter():
    """
    Pausa la ejecución del programa hasta que el usuario presione Enter.

    Returns:
        None
    """    
    input("\nPresione Enter para continuar...")

def menu():
    """
    Muestra y controla el menú principal del sistema.

    Acciones disponibles:
        1. Agregar productos
        2. Listar productos
        3. Registrar proveedores
        4. Listar proveedores
        5. Modificar producto
        6. Listado de precios con IVA
        7. Buscar proveedor por nombre
        8. Estadísticas del stock
        9. Filtrar stock bajo
        0. Guardar y salir

    Controla errores de entrada y mantiene el programa en ejecución
    hasta que el usuario elija salir.

    Returns:
        None
    """        
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
            elif opcion == 10:
                valor = float(input("Mostrar productos con precio mayor a: "))
                resultado = productos_mayores_a(productos, valor)

                if resultado:
                    print("Productos encontrados:")
                    for nombre in resultado:
                       print(f"- {nombre}")
                else:
                    print("No hay productos con precio superior a ese valor.")
    
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
if __name__ == "__main__":
    menu()
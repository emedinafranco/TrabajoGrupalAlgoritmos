"""Funciones y constantes para estilos de salida en terminal.

Este módulo define códigos de color ANSI y funciones auxiliares para imprimir
títulos y el menú principal en la terminal con formato y colores.
"""
# Colores ANSI para la terminal
COLOR_RESET = "\033[0m"
COLOR_GREEN = "\033[92m"
COLOR_WHITE = "\033[97m"
COLOR_CYAN = "\033[96m"
COLOR_BLUE = "\033[94m"
COLOR_GRAY = "\033[90m"
COLOR_BOLD = "\033[1m"
COLOR_RED = "\033[91m"
COLOR_YELLOW = "\033[93m"

def notification(type, messagge):
    icon = {
        "ok": "✅",
        "error": "❌",
        "info": "ℹ️",
        "warn": "⚠️"
    }
    
    color = {
        "ok": COLOR_GREEN,
        "error": COLOR_RED,
        "info": COLOR_CYAN,
        "warn": COLOR_YELLOW,
    }
    
    print(f"{color[type]}{icon[type]}  {messagge}{COLOR_RESET}\n")

def imprimir_titulo(texto, color):
    """Imprime un título centrado en la terminal usando el color indicado.

    Muestra una línea superior e inferior de separación y centra el texto dentro
    de un ancho fijo. No retorna valor.

    Parámetros:
    - texto (str): El texto que se mostrará como título.
    - color (str): Código ANSI de color que se aplicará al título.
    """
    ancho = 60
    print(f"\n{color}{'=' * ancho}")
    print(f"{texto.center(ancho)}")
    print(f"{'=' * ancho}{COLOR_WHITE}\n")

def mostrar_menu_principal():
    """Muestra el menú principal del sistema en la terminal con formato coloreado.

    Presenta las opciones principales (altas, listados, modificación, precios, salir)
    utilizando los colores definidos en este módulo. No recibe parámetros ni retorna valor.
    """
    print(f"\n{COLOR_GREEN}")
    print("╔" + "═" * 58 + "╗")
    print("║" + "SISTEMA DE GESTIÓN".center(58) + "║")
    print("╠" + "═" * 58 + "╣")
    print("║                                                          ║")
    print(f"║  {COLOR_WHITE}1{COLOR_GREEN} → Alta de producto                                    ║")
    print(f"║  {COLOR_WHITE}2{COLOR_GREEN} → Listado de productos                                ║")
    print(f"║  {COLOR_WHITE}3{COLOR_GREEN} → Alta de proveedores                                 ║")
    print(f"║  {COLOR_WHITE}4{COLOR_GREEN} → Listado de proveedores                              ║")
    print(f"║  {COLOR_WHITE}5{COLOR_GREEN} → Modificar producto                                  ║")
    print(f"║  {COLOR_WHITE}6{COLOR_GREEN} → Listado de precios con iva                          ║")
    print(f"║  {COLOR_WHITE}7{COLOR_GREEN} → Busqueda de proveedores                             ║")
    print(f"║  {COLOR_WHITE}8{COLOR_GREEN} → Estadisticas del stock                              ║")
    print("║                                                          ║")
    print(f"║  {COLOR_RED}[0]{COLOR_RED} → Salir                                           {COLOR_GREEN}  ║")
    print("║                                                          ║")
    print(f"{COLOR_GREEN}╚" + "═" * 58 + "╝")

def comfirma_accion(messagge):
    """Imprime un mensaje de confirmación en color verde.

    Parámetros:
    - messagge (str): El mensaje que se mostrará como confirmación.
    """
    respuesta = input(f"{COLOR_GREEN}{messagge}{COLOR_RESET} (s/n): ").lower()
    return respuesta == 's' or respuesta == 'si'

def mostrar_estadisticas(total, promedio, producto_caro, precio_caro, producto_barato, precio_barato):
    """Muestra las estadísticas del stock en un formato visual.
    
    Parámetros:
    - total (float): Valor total del stock
    - promedio (float): Precio promedio
    - producto_caro (str): Nombre del producto más caro
    - precio_caro (float): Precio del producto más caro
    - producto_barato (str): Nombre del producto más barato
    - precio_barato (float): Precio del producto más barato
    """
    print(f"\n{COLOR_GREEN}╔═══════════════════════════════════════════════════════════╗")
    print(f"║{COLOR_BOLD}{COLOR_WHITE}              ESTADÍSTICAS DEL STOCK {COLOR_RESET}{COLOR_GREEN}                      ║")
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║                                                           ║")
    print(f"║  {COLOR_WHITE}💰 Valor total del stock:{COLOR_GREEN} ${total:,.2f}                    {COLOR_GREEN}║")
    print(f"║  {COLOR_WHITE}📈 Precio promedio:{COLOR_GREEN} ${promedio:,.2f}                          {COLOR_GREEN}║")
    print("║                                                           ║")
    print(f"║  {COLOR_WHITE}🔺 Producto más caro:{COLOR_RESET}                                    ║")
    print(f"║     {COLOR_YELLOW}{producto_caro[:30]}{COLOR_GREEN} - {COLOR_GREEN}${precio_caro:,.2f}                                    {COLOR_GREEN}║")
    print("║                                                           ║")
    print(f"║  {COLOR_WHITE}🔻 Producto más barato:{COLOR_RESET}                                  ║")
    print(f"║     {COLOR_YELLOW}{producto_barato[:30]}{COLOR_GREEN} - {COLOR_GREEN}${precio_barato:,.2f}                                 {COLOR_GREEN}║")
    print("║                                                           ║")
    print(f"╚═══════════════════════════════════════════════════════════╝{COLOR_RESET}\n")

# Colores ANSI para la terminal
COLOR_RESET = "\033[0m"
COLOR_GREEN = "\033[92m"
COLOR_WHITE = "\033[97m"
COLOR_CYAN = "\033[96m"
COLOR_BLUE = "\033[94m"
COLOR_GRAY = "\033[90m"
COLOR_BOLD = "\033[1m"

def imprimir_titulo(texto, color):
    ancho = 60
    print(f"\n{color}{'=' * ancho}")
    print(f"{texto.center(ancho)}")
    print(f"{'=' * ancho}{COLOR_WHITE}\n")

def mostrar_menu_principal():
    print(f"\n{COLOR_GREEN}")
    print("╔" + "═" * 58 + "╗")
    print("║" + "SISTEMA DE GESTIÓN".center(58) + "║")
    print("╠" + "═" * 58 + "╣")
    print("║                                                          ║")
    print(f"║  {COLOR_WHITE}1{COLOR_GREEN} → Alta de producto                                    ║")
    print(f"║  {COLOR_WHITE}2{COLOR_GREEN} → Listado de productos                                ║")
    print(f"║  {COLOR_WHITE}3{COLOR_GREEN} → Alta de proveedores                                 ║")
    print(f"║  {COLOR_WHITE}4{COLOR_GREEN} → Listado de proveedores                              ║")
    print(f"║  {COLOR_WHITE}5{COLOR_GREEN} → Listado de precios con iva                          ║")
    print(f"║  {COLOR_WHITE}0{COLOR_GREEN} → Salir                                               ║")
    print("║                                                          ║")
    print("╚" + "═" * 58 + "╝")
    print(COLOR_WHITE)


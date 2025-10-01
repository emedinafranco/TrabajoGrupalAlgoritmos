
# Colores ANSI para la terminal
COLOR_HEADER = "#00ff00"
COLOR_GREEN = "#2bff00"
COLOR_BLUE = "#0400ee"
COLOR_CYAN = "#00fff2"
COLOR_GRAY = "#9B9B9B"
COLOR_WHITE = "#FFFFFF"

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
    print(f"║  {COLOR_WHITE}1{COLOR_GREEN} → Alta de producto                                  ║")
    print(f"║  {COLOR_WHITE}2{COLOR_GREEN} → Listado de productos                              ║")
    print(f"║  {COLOR_WHITE}3{COLOR_GREEN} → Alta de proveedores                               ║")
    print(f"║  {COLOR_WHITE}4{COLOR_GREEN} → Listado de proveedores                            ║")
    print(f"║  {COLOR_WHITE}5{COLOR_GREEN} → Salir                                             ║")
    print("║                                                          ║")
    print("╚" + "═" * 58 + "╝")
    print(COLOR_WHITE)


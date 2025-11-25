import pytest
from unittest.mock import patch
import app

# Limpiar datos antes de cada test
@pytest.fixture(autouse=True)
def setup_datos():
    """Fixture para inicializar datos de prueba antes de cada test"""
    app.productos = []
    app.proveedores = []
    yield
    app.productos = []
    app.proveedores = []

@patch('app.guardar_datos')  # Mockear guardar_datos para que no escriba archivos
@patch('builtins.input')      # Mockear input para simular entradas del usuario
def test_agregar_productos_exitoso(mock_input, mock_guardar):
    """Test: agregar un producto con datos válidos"""
    mock_input.side_effect = [
        '1234',  # ID producto
        'Leche',  # Nombre
        '1500',  # Precio
        '20'     # Stock
    ]    
    app.agregar_productos()
    # Verificar que se agregó el producto
    assert len(app.productos) == 1
    assert app.productos[0]["ID Producto"] == 1234
    assert app.productos[0]["Nombre"] == "Leche"
    assert app.productos[0]["Precio"] == 1500.0
    assert app.productos[0]["Stock"] == 20
    
    # Verificar que se llamó a guardar_datos
    mock_guardar.assert_called_once()

@patch('app.guardar_datos')
@patch('builtins.input')
def test_agregar_productos_id_invalido(mock_input, mock_guardar):
    """Test: agregar producto con ID inválido primero, luego válido"""
    mock_input.side_effect = [
        '123',   # ID inválido (solo 3 dígitos)
        '5678',  # ID válido (4 dígitos)
        'Pan',   # Nombre
        '800',   # Precio
        '15'     # Stock
    ]
    
    app.agregar_productos()
    
    assert len(app.productos) == 1
    assert app.productos[0]["ID Producto"] == 5678
    assert app.productos[0]["Nombre"] == "Pan"

@patch('app.guardar_datos')
@patch('builtins.input')
def test_agregar_productos_nombre_invalido(mock_input, mock_guardar):
    """Test: agregar producto con nombre inválido primero"""
    mock_input.side_effect = [
        '9999',      # ID válido
        'Coca123',   # Nombre inválido (tiene números)
        'Coca Cola', # Nombre válido
        '2500',      # Precio
        '30'         # Stock
    ]
    
    app.agregar_productos()
    
    assert len(app.productos) == 1
    assert app.productos[0]["Nombre"] == "Coca Cola"
    assert app.productos[0]["Precio"] == 2500.0

@patch('app.guardar_datos')
@patch('builtins.input')
def test_agregar_productos_id_duplicado(mock_input, mock_guardar):
    """Test: intentar agregar producto con ID duplicado"""
    # Primero agregar un producto
    app.productos = [
        {
            "ID Producto": 1111,
            "Nombre": "Producto Existente",
            "Precio": 1000.0,
            "Stock": 10
        }
    ]
    
    # Intentar agregar otro con el mismo ID
    mock_input.side_effect = ['1111']  # ID duplicado
    
    app.agregar_productos()
    
    # No debe agregarse nada nuevo
    assert len(app.productos) == 1
    assert app.productos[0]["Nombre"] == "Producto Existente"
    mock_guardar.assert_not_called()

@patch('app.guardar_datos')
@patch('builtins.input')
def test_registro_proveedor_exitoso(mock_input, mock_guardar):
    """Test: registrar un proveedor con datos válidos"""
    mock_input.side_effect = [
        '5678',              # ID
        'La Serenisima',     # Nombre
        '11223344',          # Teléfono
        'serenisima@mail.com'  # Email
    ]
    
    app.registro_de_proveedores()
    
    assert len(app.proveedores) == 1
    assert app.proveedores[0]["ID Proveedor"] == 5678
    assert app.proveedores[0]["Nombre"] == "La Serenisima"
    mock_guardar.assert_called_once()

def test_verificar_productos_existente():
    """Test: verificar que detecta producto existente"""
    app.productos = [
        {"ID Producto": 1111, "Nombre": "Test", "Precio": 100, "Stock": 5}
    ]
    
    assert app.verificar_productos(1111, app.productos) == True

def test_verificar_productos_no_existente():
    """Test: verificar que detecta producto inexistente"""
    app.productos = [
        {"ID Producto": 1111, "Nombre": "Test", "Precio": 100, "Stock": 5}
    ]
    
    assert app.verificar_productos(9999, app.productos) == False

def test_lista_precios_con_iva():
    """Test: calcular precios con IVA (21%)"""
    app.productos = [
        {"ID Producto": 1, "Nombre": "Producto A", "Precio": 1000.0, "Stock": 10},
        {"ID Producto": 2, "Nombre": "Producto B", "Precio": 2000.0, "Stock": 5}
    ]
    
    resultado = app.lista_precios_con_iva(app.productos)
    
    assert len(resultado) == 2
    assert resultado[0][0] == "Producto A"
    assert resultado[0][1] == pytest.approx(1210.0)  # 1000 * 1.21
    assert resultado[1][0] == "Producto B"
    assert resultado[1][1] == pytest.approx(2420.0)  # 2000 * 1.21

def test_buscar_proveedor():
    """Test: buscar proveedor por nombre"""
    app.proveedores = [
        {"ID Proveedor": 1, "Nombre": "Arcor", "Teléfono": "12345678", "Correo electrónico": "arcor@mail.com"}
    ]
    
    resultado = app.buscar_proveedor("Arcor")
    
    assert len(resultado) == 1
    assert resultado[0]["Nombre"] == "Arcor"

def test_buscar_proveedor_case_insensitive():
    """Test: buscar sin distinguir mayúsculas"""
    app.proveedores = [
        {"ID Proveedor": 1, "Nombre": "Arcor", "Teléfono": "12345678", "Correo electrónico": "arcor@mail.com"}
    ]
    
    resultado = app.buscar_proveedor("ARCOR")
    
    assert len(resultado) == 1
    assert resultado[0]["Nombre"] == "Arcor"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
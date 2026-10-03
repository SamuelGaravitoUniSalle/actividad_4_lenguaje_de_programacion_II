def expect_error(label, action, expected):
    """Ejecuta una accion y verifica que lance el error esperado.

    Args:
        label: descripcion del caso que se prueba.
        action: funcion sin argumentos que debe fallar.
        expected: tipo de excepcion esperado.
    """
    try:
        action()
    except expected as error:
        print(f"  OK {label} -> {type(error).__name__}: {error}")
    else:
        raise AssertionError(f"{label}: no se lanzo {expected.__name__}")
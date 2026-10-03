from exercise3.medication.base_medication import Medication
 
class CommonMedication(Medication):
    """Representa un medicamento de venta libre, sin datos adicionales."""
 
    def warning_label(self):
        """Retorna la advertencia de un medicamento comun.
 
        Returns:
            Cadena vacia, porque un medicamento comun no requiere aviso.
        """
        return ""
 
 
class Antibiotic(Medication):
    """Representa un antibiotico con una duracion de tratamiento definida.
 
    Atributos:
        _treatment_days: numero de dias que debe completarse el tratamiento.
    """
 
    def __init__(self, name, dose, treatment_days):
        """Inicializa un antibiotico.
 
        Args:
            name: nombre del medicamento.
            dose: dosis indicada.
            treatment_days: dias de tratamiento, entero positivo.
 
        Raises:
            TypeError: si los dias de tratamiento no son un entero.
            ValueError: si los dias de tratamiento no son positivos.
        """
        super().__init__(name, dose)
        if isinstance(treatment_days, bool) or not isinstance(treatment_days, int):
            raise TypeError(
                f"Los dias de tratamiento deben ser un entero, no {type(treatment_days).__name__}."
            )
        if treatment_days <= 0:
            raise ValueError(
                f"Los dias de tratamiento deben ser positivos, se recibio {treatment_days}."
            )
        self._treatment_days = treatment_days
 
    def warning_label(self):
        """Retorna la advertencia de un antibiotico.
 
        Returns:
            Texto que indica completar todos los dias de tratamiento.
        """
        return f"Completar los {self._treatment_days} dias aunque mejoren los sintomas"
 
 
class ControlledMedication(Medication):
    """Representa un medicamento de venta controlada.
 
    Atributos:
        _registration_number: numero de registro oficial, obligatorio.
    """
 
    def __init__(self, name, dose, registration_number):
        """Inicializa un medicamento controlado.
 
        Args:
            name: nombre del medicamento.
            dose: dosis indicada.
            registration_number: numero de registro oficial, no vacio.
 
        Raises:
            TypeError: si el numero de registro no es una cadena de texto.
            ValueError: si el numero de registro esta vacio.
        """
        super().__init__(name, dose)
        if not isinstance(registration_number, str):
            raise TypeError(
                f"El numero de registro debe ser una cadena, no {type(registration_number).__name__}."
            )
        if not registration_number.strip():
            raise ValueError("El numero de registro es obligatorio y no puede estar vacio.")
        self._registration_number = registration_number.strip()
 
    def warning_label(self):
        """Retorna la advertencia de un medicamento controlado.
 
        Returns:
            Texto que indica la necesidad de receta oficial y el registro.
        """
        return f"Requiere receta oficial - Registro {self._registration_number}"
from exercise1 import Patient
from datetime import datetime

class RestrictedPatient(Patient):

    VALID_STATUSES = ("ingresado", "en tratamiento", "en recuperación", "alta")
 
    def __init__(self, name, age, id_number, diagnosis, status="ingresado"):
        """Inicializa un paciente con estado restringido.
        Args:
            name: nombre completo del paciente.
            age: edad del paciente en anios.
            id_number: numero de documento de identidad.
            diagnosis: diagnostico actual del paciente.
            status: estado clinico inicial, por defecto "ingresado".

        Raises:
            TypeError: si el estado no es una cadena de texto.
            ValueError: si el estado no pertenece al conjunto permitido.
        """
        super().__init__(name, age, id_number, diagnosis)
        self._status = None
        self._status_history = []
        self.status = status

    @property
    def status(self):
        """Retorna el estado clinico actual del paciente."""
        return self._status
 
    @status.setter
    def status(self, value):
        """Valida, normaliza y asigna el estado clinico del paciente.
 
        La entrada se normaliza quitando espacios sobrantes y pasando a
        minusculas. Cada cambio aceptado queda registrado en el historial.
 
        Args:
            value: nuevo estado clinico como cadena de texto.
 
        Raises:
            TypeError: si el valor no es una cadena de texto.
            ValueError: si el estado normalizado no esta en VALID_STATUSES.
        """
        if not isinstance(value, str):
            raise TypeError(
                f"El estado debe ser una cadena de texto, no {type(value).__name__}."
            )
        normalized = value.strip().lower()
        if normalized not in self.VALID_STATUSES:
            raise ValueError(
                f"Estado invalido: '{value}'. Los estados permitidos son: "
                f"{', '.join(self.VALID_STATUSES)}."
            )
        self._status_history.append(
            {
                "timestamp": datetime.now(),
                "previous": self._status,
                "new": normalized,
            }
        )
        self._status = normalized
 
    @property
    def status_history(self):
        """Retorna una copia del historial de cambios de estado."""
        return list(self._status_history)
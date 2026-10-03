from abc import ABC, abstractmethod

class Medication(ABC):
    """Clase abstracta que representa un medicamento generico.
 
    Las clases hijas deben implementar warning_label() con la advertencia
    propia de cada tipo de medicamento.
 
    Atributos:
        _name: nombre del medicamento.
        _dose: dosis indicada, por ejemplo "500 mg".
    """
 
    def __init__(self, name, dose):
        """Inicializa un medicamento.
 
        Args:
            name: nombre del medicamento.
            dose: dosis indicada.
        """
        self._name = name
        self._dose = dose
 
    @property
    def name(self):
        """Retorna el nombre del medicamento."""
        return self._name
 
    @property
    def dose(self):
        """Retorna la dosis del medicamento."""
        return self._dose
 
    @abstractmethod
    def warning_label(self):
        """Retorna la advertencia que debe acompanar al medicamento.
 
        Returns:
            Cadena de texto con la advertencia, o vacia si no aplica.
        """
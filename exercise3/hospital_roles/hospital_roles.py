from exercise1 import Patient
from exercise3.medication.medications import Medication

class Exercise3Patient(Patient):

    def __init__(self, name, age, id_number, diagnosis):
            """Inicializa un paciente.
    
            Args:
                name: nombre completo del paciente.
                age: edad del paciente en anios.
                id_number: numero de documento de identidad.
                diagnosis: diagnostico actual del paciente.
            """
            super().__init__(name, age, id_number, diagnosis)
            self._prescription = []

    def add_medication(self, medication):
        """Agrega un medicamento a la formula del paciente.
 
        Args:
            medication: instancia de Medication a formular.
 
        Raises:
            TypeError: si el objeto recibido no es un Medication.
        """
        if not isinstance(medication, Medication):
            raise TypeError(
                f"Se esperaba un Medication, no {type(medication).__name__}."
            )
        self._prescription.append(medication)
 
    def show_prescription(self):
        """Imprime la formula del paciente con la advertencia de cada medicamento.
 
        Debajo de cada medicamento se imprime su advertencia solo si no esta
        vacia.
        """
        print(f"Formula de {self._name}:")
        if not self._prescription:
            print("  (sin medicamentos formulados)")
        for medication in self._prescription:
            print(f"  - {medication.name} {medication.dose}")
            warning = medication.warning_label()
            if warning:
                print(f"      Advertencia: {warning}")
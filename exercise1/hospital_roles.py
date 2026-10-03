
from exercise1.person import Person

class Doctor(Person):
    """Representa a un medico, hijo de Person.

    Atributos:
        _specialty: especialidad medica del doctor.
    """

    def __init__(self, name, age, id_number, specialty):
        """Inicializa un medico.

        Args:
            name: nombre completo del medico.
            age: edad del medico en anios.
            id_number: numero de documento de identidad.
            specialty: especialidad medica.
        """
        super().__init__(name, age, id_number)
        self._specialty = specialty

    def individual_identification(self):
        """Retorna una cadena que identifica al medico.

        Returns:
            Texto con el nombre, la especialidad y el documento del medico.
        """
        return f"Dr. {self._name} - Especialidad: {self._specialty} (ID: {self._id_number})"


class Patient(Person):
    """Representa a un paciente, hijo de Person.

    Atributos:
        _diagnosis: diagnostico actual del paciente.
    """

    def __init__(self, name, age, id_number, diagnosis):
        """Inicializa un paciente.

        Args:
            name: nombre completo del paciente.
            age: edad del paciente en anios.
            id_number: numero de documento de identidad.
            diagnosis: diagnostico actual del paciente.
        """
        super().__init__(name, age, id_number)
        self._diagnosis = diagnosis

    def individual_identification(self):
        """Retorna una cadena que identifica al paciente.

        Returns:
            Texto con el nombre, el diagnostico y el documento del paciente.
        """
        return f"Paciente: {self._name} - Diagnostico: {self._diagnosis} (ID: {self._id_number})"


class Nurse(Person):
    """Representa a un enfermero, hijo de Person.

    Atributos:
        _shift: turno de trabajo, puede ser "mañana", "tarde" o "noche".
        _area: area del hospital donde trabaja, por ejemplo "Urgencias".
        _assigned_patients: lista de pacientes bajo su cuidado.
    """

    VALID_SHIFTS = ("mañana", "tarde", "noche")

    def __init__(self, name, age, id_number, shift, area):
        """Inicializa un enfermero.

        Args:
            name: nombre completo del enfermero.
            age: edad del enfermero en anios.
            id_number: numero de documento de identidad.
            shift: turno de trabajo ("morning", "afternoon" o "night").
            area: area del hospital donde trabaja.

        Raises:
            ValueError: si el turno no es uno de los permitidos.
        """
        super().__init__(name, age, id_number)
        if shift not in self.VALID_SHIFTS:
            raise ValueError(
                f"Turno invalido: '{shift}'. Debe ser uno de {self.VALID_SHIFTS}."
            )
        self._shift = shift
        self._area = area
        self._assigned_patients = []

    def register_round(self, patient):
        """Agrega un paciente a la lista del enfermero e imprime una confirmacion.

        Args:
            patient: paciente que pasa a estar bajo el cuidado del enfermero.
        """
        self._assigned_patients.append(patient)
        print(
            f"Ronda registrada: {self._name} atendio a {patient.name} "
            f"en {self._area} (turno {self._shift})."
        )

    def individual_identification(self):
        """Retorna una cadena que identifica al enfermero.

        Returns:
            Texto con el nombre, el area, el turno, la cantidad de pacientes
            asignados y el documento del enfermero.
        """
        return (
            f"Enfermero: {self._name} - Area: {self._area} - Turno: {self._shift} - "
            f"Pacientes asignados: {len(self._assigned_patients)} (ID: {self._id_number})"
        )
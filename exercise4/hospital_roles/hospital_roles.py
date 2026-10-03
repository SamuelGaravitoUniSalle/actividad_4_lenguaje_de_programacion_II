from exercise1 import Doctor
from exercise2 import RestrictedPatient
from exercise4.lab.base_exam import Exam 

class LabPatient(RestrictedPatient):
    """Paciente que ademas mantiene una lista de examenes de laboratorio.

    Atributos:
        _exams: examenes ordenados al paciente.
    """

    def __init__(self, name, age, id_number, diagnosis, status="ingresado"):
        """Inicializa un paciente con lista de examenes vacia.

        Args:
            name: nombre completo del paciente.
            age: edad del paciente en anios.
            id_number: numero de documento de identidad.
            diagnosis: diagnostico actual del paciente.
            status: estado clinico inicial, por defecto "ingresado".
        """
        super().__init__(name, age, id_number, diagnosis, status)
        self._exams = []

    @property
    def exams(self):
        """Retorna una copia de la lista de examenes del paciente."""
        return list(self._exams)

    def add_exam(self, exam):
        """Agrega un examen a la lista propia del paciente.

        Args:
            exam: instancia de Exam ordenada para este paciente.

        Raises:
            TypeError: si el objeto recibido no es un Exam.
        """
        if not isinstance(exam, Exam):
            raise TypeError(f"Se esperaba un Exam, no {type(exam).__name__}.")
        self._exams.append(exam)

    def show_results(self):
        """Imprime todos los examenes del paciente.

        Los examenes con resultado muestran valor, unidad e interpretacion.
        Los demas muestran el estado del proceso en que se encuentran.
        """
        print(f"Examenes de {self._name}:")
        if not self._exams:
            print("  (sin examenes ordenados)")
        for exam in self._exams:
            if exam.has_result:
                print(
                    f"  - {exam.name}: {exam.value} {exam.unit()} "
                    f"({exam.interpretation})"
                )
            else:
                print(f"  - {exam.name}: sin resultado - estado: {exam.status}")

    @property
    def abnormal_exams(self):
        """Retorna los examenes con resultado fuera del rango normal.

        Los examenes que todavia no tienen valor se ignoran sin error.

        Returns:
            Lista de examenes cuyo resultado no es normal.
        """
        return [
            exam for exam in self._exams if exam.has_result and not exam.is_normal
        ]


class LabDoctor(Doctor):
    """Medico que puede tener pacientes asignados y ordenarles examenes.

    Atributos:
        _assigned_patients: pacientes bajo la responsabilidad del medico.
    """

    def __init__(self, name, age, id_number, specialty):
        """Inicializa un medico sin pacientes asignados.

        Args:
            name: nombre completo del medico.
            age: edad del medico en anios.
            id_number: numero de documento de identidad.
            specialty: especialidad medica.
        """
        super().__init__(name, age, id_number, specialty)
        self._assigned_patients = []

    def assign_patient(self, patient):
        """Asigna un paciente al medico si todavia no lo tiene.

        Args:
            patient: paciente que pasa a cargo del medico.
        """
        if patient not in self._assigned_patients:
            self._assigned_patients.append(patient)

    def order_exam(self, patient, exam):
        """Ordena un examen a un paciente asignado a este medico.

        Args:
            patient: paciente al que se le ordena el examen.
            exam: examen a ordenar.

        Raises:
            ValueError: si el paciente no esta asignado al medico, o si el
                examen pertenece a otro paciente u otro medico.
            TypeError: si el paciente no es un LabPatient.
        """
        if patient not in self._assigned_patients:
            raise ValueError(
                f"El paciente {patient.name} no esta asignado al Dr. {self._name}."
            )
        if exam.patient is not patient:
            raise ValueError("El examen fue creado para un paciente distinto.")
        if exam.requesting_doctor is not self:
            raise ValueError("El examen fue creado a nombre de otro medico.")
        if not isinstance(patient, LabPatient):
            raise TypeError(f"Se esperaba un LabPatient, no {type(patient).__name__}.")
        patient.add_exam(exam)
        print(f"Examen ordenado: {exam.name} para {patient.name} por el Dr. {self._name}.")
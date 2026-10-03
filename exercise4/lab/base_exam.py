from abc import ABC, abstractmethod
from exercise4.exceptions import ExamStateError

class Exam(ABC):
    """Clase abstracta que representa un examen de laboratorio.

    El examen pasa por tres estados en orden estricto: "ordenado",
    "muestra tomada" y "resultado disponible". Las clases hijas definen el rango
    normal y la unidad de medida.

    Atributos:
        _name: nombre del examen.
        _patient: paciente al que se le ordeno el examen.
        _requesting_doctor: medico que ordeno el examen.
        _status: estado actual dentro del proceso.
        _value: resultado numerico, None mientras no exista.
    """

    ORDERED = "ordenado"
    SAMPLE_TAKEN = "muestra tomada"
    RESULT_AVAILABLE = "resultado disponible"
    VALID_STATUSES = (ORDERED, SAMPLE_TAKEN, RESULT_AVAILABLE)

    def __init__(self, name, patient, requesting_doctor):
        """Inicializa un examen en estado "ordered" y sin resultado.

        Args:
            name: nombre del examen.
            patient: paciente al que se le ordena el examen.
            requesting_doctor: medico que ordena el examen.

        Raises:
            TypeError: si el paciente o el medico no son del tipo esperado.
        """
        from exercise4.hospital_roles.hospital_roles import LabDoctor, LabPatient

        if not isinstance(patient, LabPatient):
            raise TypeError(f"Se esperaba un LabPatient, no {type(patient).__name__}.")
        if not isinstance(requesting_doctor, LabDoctor):
            raise TypeError(
                f"Se esperaba un LabDoctor, no {type(requesting_doctor).__name__}."
            )
        self._name = name
        self._patient = patient
        self._requesting_doctor = requesting_doctor
        self._status = self.ORDERED
        self._value = None

    @property
    def name(self):
        """Retorna el nombre del examen."""
        return self._name

    @property
    def patient(self):
        """Retorna el paciente al que se le ordeno el examen."""
        return self._patient

    @property
    def requesting_doctor(self):
        """Retorna el medico que ordeno el examen."""
        return self._requesting_doctor

    @property
    def status(self):
        """Retorna el estado actual del examen."""
        return self._status

    @status.setter
    def status(self, new_status):
        """Avanza el estado del examen un paso a la vez.

        La entrada se normaliza quitando espacios y pasando a minusculas.
        No se permite saltar pasos, retroceder ni repetir el estado actual.

        Args:
            new_status: estado al que se quiere pasar.

        Raises:
            TypeError: si el estado no es una cadena de texto.
            ValueError: si el estado no pertenece al conjunto permitido.
            ExamStateError: si la transicion salta un paso, retrocede o repite.
        """
        if not isinstance(new_status, str):
            raise TypeError(
                f"El estado debe ser una cadena de texto, no {type(new_status).__name__}."
            )
        normalized = new_status.strip().lower()
        if normalized not in self.VALID_STATUSES:
            raise ValueError(
                f"Estado invalido: '{new_status}'. Los estados permitidos son: "
                f"{', '.join(self.VALID_STATUSES)}."
            )
        current_index = self.VALID_STATUSES.index(self._status)
        target_index = self.VALID_STATUSES.index(normalized)
        if target_index <= current_index:
            raise ExamStateError(
                f"No se puede pasar de '{self._status}' a '{normalized}': "
                "el proceso no admite retroceder ni repetir un estado."
            )
        if target_index > current_index + 1:
            skipped = self.VALID_STATUSES[current_index + 1]
            raise ExamStateError(
                f"No se puede pasar de '{self._status}' a '{normalized}': "
                f"falta el paso intermedio '{skipped}'."
            )
        self._status = normalized

    @property
    def value(self):
        """Retorna el resultado numerico, o None si todavia no existe."""
        return self._value

    @value.setter
    def value(self, new_value):
        """Carga el resultado del examen y marca el resultado como disponible.

        Si el examen esta en "muestra tomada", el estado cambia automaticamente
        a "resultado disponible". Si ya tenia resultado, se permite corregirlo.

        Args:
            new_value: resultado numerico no negativo.

        Raises:
            TypeError: si el valor no es un numero.
            ValueError: si el valor es negativo.
            ExamStateError: si la muestra todavia no ha sido tomada.
        """
        if isinstance(new_value, bool) or not isinstance(new_value, (int, float)):
            raise TypeError(
                f"El resultado debe ser numerico, no {type(new_value).__name__}."
            )
        if new_value < 0:
            raise ValueError(f"El resultado no puede ser negativo, se recibio {new_value}.")
        if self._status == self.ORDERED:
            raise ExamStateError(
                "No se puede cargar un resultado mientras el examen esta "
                "'ordenado': primero debe tomarse la muestra."
            )
        self._value = new_value
        if self._status == self.SAMPLE_TAKEN:
            self.status = self.RESULT_AVAILABLE

    @abstractmethod
    def normal_range(self):
        """Retorna el rango normal del examen.

        Returns:
            Tupla (minimo, maximo) de los valores considerados normales.
        """

    @abstractmethod
    def unit(self):
        """Retorna la unidad de medida del examen.

        Returns:
            Cadena con la unidad, por ejemplo "mg/dL".
        """

    @property
    def has_result(self):
        """Indica si ya se cargo un valor para el examen."""
        return self._value is not None

    @property
    def is_normal(self):
        """Indica si el resultado esta dentro del rango normal, extremos incluidos.

        Raises:
            ExamStateError: si el examen todavia no tiene resultado.
        """
        self._require_result()
        minimum, maximum = self.normal_range()
        return minimum <= self._value <= maximum

    @property
    def interpretation(self):
        """Interpreta el resultado frente al rango normal.

        Returns:
            "bajo", "normal" o "alto".

        Raises:
            ExamStateError: si el examen todavia no tiene resultado.
        """
        self._require_result()
        minimum, maximum = self.normal_range()
        if self._value < minimum:
            return "bajo"
        if self._value > maximum:
            return "normal"
        return "alto"

    def _require_result(self):
        """Verifica que exista un resultado.

        Raises:
            ExamStateError: si el examen todavia no tiene resultado.
        """
        if not self.has_result:
            raise ExamStateError(
                f"El examen '{self._name}' no tiene resultado todavia "
                f"(estado: '{self._status}')."
            )

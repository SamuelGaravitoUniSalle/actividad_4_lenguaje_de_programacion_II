from exercise4.lab.base_exam import Exam


class Glycemia(Exam):
    """Examen de glucosa en sangre."""

    def __init__(self, patient, requesting_doctor):
        """Inicializa un examen de glucemia.

        Args:
            patient: paciente al que se le ordena el examen.
            requesting_doctor: medico que ordena el examen.
        """
        super().__init__("Glycemia", patient, requesting_doctor)

    def normal_range(self):
        """Retorna el rango normal de glucemia: de 70 a 100."""
        return (70, 100)

    def unit(self):
        """Retorna la unidad de la glucemia: mg/dL."""
        return "mg/dL"


class Hemoglobin(Exam):
    """Examen de hemoglobina en sangre."""

    def __init__(self, patient, requesting_doctor):
        """Inicializa un examen de hemoglobina.

        Args:
            patient: paciente al que se le ordena el examen.
            requesting_doctor: medico que ordena el examen.
        """
        super().__init__("Hemoglobin", patient, requesting_doctor)

    def normal_range(self):
        """Retorna el rango normal de hemoglobina: de 12 a 16."""
        return (12, 16)

    def unit(self):
        """Retorna la unidad de la hemoglobina: g/dL."""
        return "g/dL"


class Cholesterol(Exam):
    """Examen de colesterol total en sangre."""

    def __init__(self, patient, requesting_doctor):
        """Inicializa un examen de colesterol.

        Args:
            patient: paciente al que se le ordena el examen.
            requesting_doctor: medico que ordena el examen.
        """
        super().__init__("Cholesterol", patient, requesting_doctor)

    def normal_range(self):
        """Retorna el rango normal de colesterol: de 0 a 200."""
        return (0, 200)

    def unit(self):
        """Retorna la unidad del colesterol: mg/dL."""
        return "mg/dL"
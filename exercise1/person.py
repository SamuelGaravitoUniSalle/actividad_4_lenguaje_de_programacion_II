"""Modulo que modela personas de un hospital y demuestra polimorfismo."""


class Person:
    """Representa a una persona generica dentro del hospital.

    Atributos:
        _name: nombre completo de la persona.
        _age: edad de la persona en anios.
        _id_number: numero de documento de identidad.
    """

    def __init__(self, name, age, id_number):
        """Inicializa una persona.

        Args:
            name: nombre completo de la persona.
            age: edad de la persona en anios.
            id_number: numero de documento de identidad.
        """
        self._name = name
        self._age = age
        self._id_number = id_number

    @property
    def name(self):
        """Retorna el nombre de la persona."""
        return self._name

    def individual_identification(self):
        """Retorna una cadena que identifica a la persona.

        Returns:
            Texto con el nombre y el documento de la persona.
        """
        return f"Persona: {self._name} (ID: {self._id_number})"





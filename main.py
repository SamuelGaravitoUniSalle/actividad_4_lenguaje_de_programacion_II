from utils import expect_error
from exercise2 import RestrictedPatient
from exercise1 import Doctor, Nurse, Patient, Person
from exercise4.exceptions.exceptions import ExamStateError
from exercise4 import LabPatient, LabDoctor, Exam, Cholesterol, Hemoglobin, Glycemia
from exercise3 import Exercise3Patient, Medication, ControlledMedication, Antibiotic, CommonMedication

def main_exercise1():
    """Prueba el polimorfismo con medicos, pacientes y enfermeros en una lista."""

    print("\n" + "=" * 40)
    print("       EJECUCIÓN DEL EJERCICIO 1")
    print("=" * 40 + "\n")

    doctor = Doctor("Carlos Ramirez", 45, "1001", "Cardiologia")
    patient_one = Patient("Laura Gomez", 30, "2001", "Arritmia")
    patient_two = Patient("Pedro Diaz", 8, "2002", "Bronquitis")
    nurse = Nurse("Ana Torres", 28, "3001", "mañana", "Urgencias")

    nurse.register_round(patient_one)
    nurse.register_round(patient_two)
    print()
    people = [doctor, patient_one, nurse, patient_two, Person("Visitante Anonimo", 50, "9999")]

    for person in people:
        print(person.individual_identification())


def main_exercise2():
    """Verifica la normalizacion, el rechazo de estados invalidos y el historial."""

    print("\n" + "=" * 40)
    print("       EJECUCIÓN DEL EJERCICIO 2")
    print("=" * 40 + "\n")
    patient = RestrictedPatient("Test Patient", 40, "0000", "Fractura")
 
    patient.status = "  En Recuperación "
    print(f"Caso 1 - estado guardado: '{patient.status}'")
 
    try:
        patient.status = "muerto de risa"
    except ValueError as error:
        print(f"Caso 2 - ValueError: {error}")
 
    try:
        patient.status = 42
    except Exception as error:
        print(f"Caso 3 - {type(error).__name__}: {error}")
 
    print("Historial:")
    for entry in patient.status_history:
        print(f"  {entry['previous']} -> {entry['new']}")

def main_exercise3():
    """Verifica la clase abstracta, las validaciones y la formula del paciente."""

    print("\n" + "=" * 40)
    print("       EJECUCIÓN DEL EJERCICIO 3")
    print("=" * 40 + "\n")

    try:
        Medication("Generico", "1 mg")
    except TypeError as error:
        print(f"Medication abstracta - TypeError: {error}")
 
    invalid_cases = [
        ("dias 0", lambda: Antibiotic("Amoxicilina", "500 mg", 0)),
        ("dias '7'", lambda: Antibiotic("Amoxicilina", "500 mg", "7")),
        ("dias True", lambda: Antibiotic("Amoxicilina", "500 mg", True)),
        ("registro vacio", lambda: ControlledMedication("Morfina", "10 mg", "   ")),
        ("registro None", lambda: ControlledMedication("Morfina", "10 mg", None)),
    ]
    for label, build in invalid_cases:
        try:
            build()
        except (TypeError, ValueError) as error:
            print(f"{label} - {type(error).__name__}: {error}")
 
    patient = Exercise3Patient("Laura Gomez", 30, "2001", "Infeccion respiratoria")
    patient.add_medication(CommonMedication("Acetaminofen", "500 mg"))
    patient.add_medication(Antibiotic("Amoxicilina", "500 mg", 7))
    patient.add_medication(ControlledMedication("Morfina", "10 mg", "XYZ-123"))
    print()
    patient.show_prescription()

def main_exercise4():
    """Prueba el ciclo completo de un examen y la deteccion de alterados."""

    print("\n" + "=" * 40)
    print("       EJECUCIÓN DEL EJERCICIO 4")
    print("=" * 40 + "\n")

    doctor = LabDoctor("Carlos Ramirez", 45, "1001", "Cardiologia")
    patient = LabPatient("Laura Gomez", 30, "2001", "Control general")

    print("1. Orden rechazada si el paciente no esta asignado")
    expect_error(
        "orden sin asignacion",
        lambda: doctor.order_exam(patient, Glycemia(patient, doctor)),
        ValueError,
    )

    print("\n2. Ciclo completo de un examen")
    doctor.assign_patient(patient)
    glycemia = Glycemia(patient, doctor)
    doctor.order_exam(patient, glycemia)
    expect_error("resultado antes de la muestra", lambda: setattr(glycemia, "value", 90), ExamStateError)
    expect_error("is_normal sin resultado", lambda: glycemia.is_normal, ExamStateError)
    expect_error("saltar a 'resultado disponible'", lambda: setattr(glycemia, "status", "resultado disponible"), ExamStateError)
    glycemia.status = "muestra tomada"
    expect_error("valor negativo", lambda: setattr(glycemia, "value", -5), ValueError)
    expect_error("retroceder a 'ordenado'", lambda: setattr(glycemia, "status", "ordenado"), ExamStateError)
    glycemia.value = 85
    assert glycemia.status == Exam.RESULT_AVAILABLE
    print(f"  OK estado tras cargar el valor: '{glycemia.status}'")
    expect_error("retroceder a 'muestra tomada'", lambda: setattr(glycemia, "status", "muestra tomada"), ExamStateError)

    print("\n3. Tres examenes al mismo paciente")
    hemoglobin = Hemoglobin(patient, doctor)
    cholesterol = Cholesterol(patient, doctor)
    doctor.order_exam(patient, hemoglobin)
    doctor.order_exam(patient, cholesterol)

    hemoglobin.status = "muestra tomada"
    hemoglobin.value = 10.5
    cholesterol.status = "muestra tomada"
    print()
    patient.show_results()

    assert patient.abnormal_exams == [hemoglobin]
    print("\n  OK con colesterol pendiente, solo Hemoglobin esta alterado")

    cholesterol.value = 240
    assert patient.abnormal_exams == [hemoglobin, cholesterol]
    assert glycemia not in patient.abnormal_exams
    print("  OK con colesterol cargado, alterados: " + ", ".join(e.name for e in patient.abnormal_exams))
    print()
    patient.show_results()


if __name__ == "__main__":
    main_exercise1()
    main_exercise2()
    main_exercise3()
    main_exercise4()

class Personas:
    def __init__(self, param_nombre, param_email):
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0
        
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def asistencia_clase(self):
        self.asistencia += 1


class Profesor(Personas):
    def __init__(self, param_nombre, param_email, legajo_empleado):
        self.legajo_empleado = legajo_empleado
        super().__init__(param_nombre, param_email)
    def asistencia_clase(self):
        self.asistencia += 1

profesor_pepe = Profesor("Pepe", "jose@um.edu.ar", "256631")
print(id(profesor_pepe))

print("El nombre es:  ")
print(profesor_pepe.nombre)

print("El email es:  ")
print(profesor_pepe.email)

print("El legajo es:  ")
print(profesor_pepe.legajo_empleado)

print("Su asistencia es:  ")
print(profesor_pepe.asistencia)

print("El profesor fue a la clase...")
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()

print("Su asistencia es:  ")
print(profesor_pepe.asistencia)


class Alumno(Personas):

    def __init__(self, param_nombre, param_email, numero_legajo, param_carrera):
        self.legajo = numero_legajo
        self.carrera = param_carrera
        self.materia_cursando = []
        super().__init__(param_nombre, param_email)

    def cursando(self, materia):
        self.materia_cursando.append(materia)

        
alumno_victoria = Alumno("María", "victoria@um.alumno.ar", "653210", "Ing. Informatica")

print("El nombre es:  ")
print(alumno_victoria.nombre)

print("El mail es:  ")
print(alumno_victoria.email)

print("El legajo es:  ")
print(alumno_victoria.legajo)

print("Carrera:  ")
print(alumno_victoria.carrera)


class Materia:

    def __init__ (self, param_materia, codigo_materia, param_carga):
        self.materia = param_materia
        self.codigo = codigo_materia
        self.carga = param_carga

materia_quimica = Materia("Química", "0065", "4 horas")
print("Materia:  ")
print(materia_quimica.materia)

print("Código:  ")
print(materia_quimica.codigo)

print("Carga horaria:  ")
print(materia_quimica.carga)
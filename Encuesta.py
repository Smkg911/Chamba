class Encuesta:
    def __init__(self):
        self.opiniones = {
            ("menoresDe_18", "soltero"): [],
            ("menoresDe_18", "casado"): [],
            ("entre_18_54", "soltero"): [],
            ("entre_18_54", "casado"): [],
            ("mayoresDe_55", "soltero"): [],
            ("mayoresDe_55", "casado"): []
        }

    def agregarOpinion(self, rangoEdad, estadoCivil, opinion):
        Valor = (rangoEdad, estadoCivil)
        self.opiniones[Valor].append(opinion)

    def obtenerTotalOpiniones(self):
        totalOpiniones = sum(len(opiniones) for opiniones in self.opiniones.values())
        return totalOpiniones

    def obtenerPromedioOpiniones(self):
        sumaTotal = sum(sum(opiniones) for opiniones in self.opiniones.values())
        totalOpiniones = self.obtenerTotalOpiniones()
        if totalOpiniones == 0:
            return 0
        return sumaTotal / totalOpiniones

    def obtenerValorParcialEncuesta(self, rangoEdad, estadoCivil):
        Valor = (rangoEdad, estadoCivil)
        opiniones = self.opiniones.get(Valor, [])
        if not opiniones:
            return 0
        return sum(opiniones) / len(opiniones)

# Ejemplo de uso
encuesta = Encuesta()
encuesta.agregarOpinion("menoresDe_18", "soltero", 8)
encuesta.agregarOpinion("menoresDe_18", "soltero", 2)
encuesta.agregarOpinion("entre_18_54", "casado", 6)
encuesta.agregarOpinion("mayoresDe_55", "soltero", 4)
encuesta.agregarOpinion("mayoresDe_55", "soltero", 4)

print(f"Total de opiniones: {encuesta.obtenerTotalOpiniones()}")
print(f"Promedio de opiniones: {encuesta.obtenerPromedioOpiniones()}")
print(f"Valor parcial de la encuesta para menoresDe_18_soltero: {encuesta.obtenerValorParcialEncuesta('menoresDe_18', 'soltero')}")

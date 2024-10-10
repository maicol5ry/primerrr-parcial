class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"

class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas, es_automatico):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas
        self.es_automatico = es_automatico

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Número de Puertas: {self.numero_puertas}, Es Automático: {self.es_automatico}"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindraje, tipo):
        super().__init__(marca, modelo, año)
        self.cilindraje = cilindraje
        self.tipo = tipo

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Cilindraje: {self.cilindraje}, Tipo: {self.tipo}"

def main():
    auto1 = Auto("toyota", "Corolla", 2020, 4, True)
    auto2 = Auto("honda", "Civic", 2019, 4, False)
    moto1 = Moto("yamaha", "YZF-R3", 2022, 321, "Deportiva")
    moto2 = Moto("Suzuki", "GSX250R", 2021, 248, "Deportiva")
    
    vehiculos = [auto1, auto2, moto1, moto2]
    for vehiculo in vehiculos:
        print(vehiculo.mostrar_info())

if __name__ == "__main__":
    main()

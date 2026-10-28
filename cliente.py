from persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, rut, telefono, direccion):
        super().__init__(nombre, rut, telefono)
        self.direccion = direccion
        self.bicicletas = []  # Lista para almacenar las bicicletas del cliente
        
        
    def agregar_bicicleta(self, bicicleta):
        self.bicicletas.append(bicicleta)
        print(f"Bicicleta agregada al cliente {self.nombre}:")
        
        

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Dirección: {self.direccion}")
        
        
    def contar_bicicletas(self):
        return len(self.bicicletas)
        


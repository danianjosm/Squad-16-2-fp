import math

class RefugioObj:
    def __init__(self, nome, endereco, status, recursos, latitude, longitude):
        self.nome = nome.strip()
        self.endereco = endereco.strip()
        self.status = status.strip()
        self.recursos = recursos.strip()
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def formatar_para_linha(self):
        return f"| {self.nome} | {self.endereco} | {self.status} | {self.recursos} | {self.latitude} | {self.longitude} |"

    def calcular_distancia(self, lat_usuario, lon_usuario):
        return math.sqrt((self.latitude - lat_usuario)**2 + (self.longitude - lon_usuario)**2)

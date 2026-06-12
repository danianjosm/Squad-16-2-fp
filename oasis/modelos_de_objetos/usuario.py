class UsuarioObj:
    def __init__(self, username, senha, tipo, latitude, longitude):
        self.username = username
        self.senha = senha
        self.tipo = tipo.strip().lower()
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def is_admin(self):
        return self.tipo == 'admin'

    def calcular_distancia(self, loja):
        return ((self.latitude - loja.latitude)**2 + (self.longitude - loja.longitude)**2) ** 0.5

class UsuarioObj:
    def __init__(self, username, senha, tipo, latitude, longitude):
        self.username = username
        self.senha = senha
        self.tipo = tipo.strip().lower()
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def is_admin(self):
        return self.tipo == 'admin'

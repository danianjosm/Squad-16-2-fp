class RefugioObj:
    """
    Representa um ponto de refugio climático
    atributos 
        nome(str): nome do refugio
        endereço(str): Localização no formato UF, CIDADE, BAIRRO
        status(str):Ativo ou fechado 
        latitude(float): codernada geográfica
        longitude(float): Coordenada geográfica  
    """
    def __init__(self, nome, endereco, status, recursos, latitude, longitude):
        self.nome = nome.strip()
        self.endereco = endereco.strip()
        self.status = status.strip()
        self.recursos = recursos.strip()
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def formatar_para_linha(self):
        return f"| {self.nome} | {self.endereco} | {self.status} | {self.recursos} | {self.latitude} | {self.longitude} |"
    """Converte o objeto em uma linha formatada para salvar no banco de dados """
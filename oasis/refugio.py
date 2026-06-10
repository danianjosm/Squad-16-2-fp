class Refugio:

    def __init__(self, nome, bairro):
        self.nome = nome 
        self.bairro = bairro 
        self.status = True 

    def __str__(self):
        if  self.status:
            situacao = "ativo"
        else :
            situacao = "fechado"
        return f"{self.nome} - {self.bairro} - {situacao}"

r = Refugio("Casa de Apoio", "boa viagem")
print(r)
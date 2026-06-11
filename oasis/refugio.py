class Refugio:

    def __init__(self, nome, bairro):
        self.nome = nome
        self.bairro = bairro
        self.status = True
        self.tem_agua = False
        self.tem_ar_condicionado = False
        self.arborizado = False

    def __str__(self):
        if self.status:
            situacao = "ativo"
        else:
            situacao = "fechado"

        recursos = []
        if self.tem_agua:
            recursos.append("água")
        if self.tem_ar_condicionado:
            recursos.append("ar condicionado")
        if self.arborizado:
            recursos.append("arborizado")

        if recursos:
            recursos_str = ", ".join(recursos)
        else:
            recursos_str = "sem recursos informados"

        return f"{self.nome} - {self.bairro} - {situacao} | {recursos_str}"


r = Refugio("Casa de Apoio", "boa viagem")  # teste de criação de redugio
print(r)

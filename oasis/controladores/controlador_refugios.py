from modelos_de_objetos.refugio import RefugioObj

class ControladorRefugios:
    CAMINHO_BANCO_DE_DADOS = 'oasis/banco_de_dados/refugios.txt'
    
    @staticmethod
    def inserir(refugio_obj):
        arquivo = open(ControladorRefugios.CAMINHO_BANCO_DE_DADOS, 'a', encoding='utf-8')
        try:
            arquivo.write(refugio_obj.formatar_para_linha() + "\n")
        finally:
            arquivo.close()
            
    @staticmethod
    def selecionar(quantidade, indice_inicial):
        refugios = open(ControladorRefugios.CAMINHO_BANCO_DE_DADOS, 'r', encoding='utf-8')
        linha_inicial = indice_inicial
        linha_final = indice_inicial + quantidade
        
        try:
            todas_as_linhas = refugios.readlines()
            cabecalho = todas_as_linhas[0]
            linhas_de_dados = todas_as_linhas[1:]
            dados_fatiados = linhas_de_dados[linha_inicial : linha_final]
        finally:
            refugios.close()

        print(cabecalho.strip())
        
        if len(dados_fatiados) == 0:
            print("Fim da linha, sem dados")
        else:
            for linhas in dados_fatiados:
                print(linhas.strip())
        
        return len(dados_fatiados)

    @staticmethod
    def buscar_todos():
        arquivo = open(ControladorRefugios.CAMINHO_BANCO_DE_DADOS, 'r', encoding='utf-8')
        lista_refugios = []
        try:
            linhas = arquivo.readlines()[1:]
            for linha in linhas:
                if not linha.strip(): continue
                dados = linha.strip().split('|')
                if len(dados) >= 7:
                    nome = dados[1].strip()
                    end = dados[2].strip()
                    status = dados[3].strip()
                    rec = dados[4].strip()
                    lat = dados[5].strip()
                    lon = dados[6].strip()
                    lista_refugios.append(RefugioObj(nome, end, status, rec, lat, lon))
        finally:
            arquivo.close()
        return lista_refugios

    @staticmethod
    def atualizar(indice, refugio_obj):
        arquivo = open(ControladorRefugios.CAMINHO_BANCO_DE_DADOS, 'r', encoding='utf-8')
        linhas = arquivo.readlines()
        arquivo.close()
        
        linhas[indice + 1] = refugio_obj.formatar_para_linha() + "\n"
        
        arquivo = open(ControladorRefugios.CAMINHO_BANCO_DE_DADOS, 'w', encoding='utf-8')
        arquivo.writelines(linhas)
        arquivo.close()

    @staticmethod
    def deletar(indice):
        arquivo = open(ControladorRefugios.CAMINHO_BANCO_DE_DADOS, 'r', encoding='utf-8')
        linhas = arquivo.readlines()
        arquivo.close()
        
        del linhas[indice + 1]
        
        arquivo = open(ControladorRefugios.CAMINHO_BANCO_DE_DADOS, 'w', encoding='utf-8')
        arquivo.writelines(linhas)
        arquivo.close()

from modelos_de_objetos.usuario import UsuarioObj
from modelos_de_objetos.refugio import RefugioObj

class ConectorBanco:
    class Refugio:
        CAMINHO_BANCO_DE_DADOS = 'oasis/banco_de_dados/refugios.txt'
        
        def inserir(refugio_obj):
            arquivo = open(ConectorBanco.Refugio.CAMINHO_BANCO_DE_DADOS, 'a', encoding='utf-8')
            try:
                arquivo.write(refugio_obj.formatar_para_linha() + "\n")
            finally:
                arquivo.close()
                
        def selecionar(quantidade, indice_inicial):
            refugios = open(ConectorBanco.Refugio.CAMINHO_BANCO_DE_DADOS, 'r', encoding='utf-8')

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

        def buscar_todos():
            arquivo = open(ConectorBanco.Refugio.CAMINHO_BANCO_DE_DADOS, 'r', encoding='utf-8')
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

        def atualizar(indice, refugio_obj):
            arquivo = open(ConectorBanco.Refugio.CAMINHO_BANCO_DE_DADOS, 'r', encoding='utf-8')
            linhas = arquivo.readlines()
            arquivo.close()
            
            linhas[indice + 1] = refugio_obj.formatar_para_linha() + "\n"
            
            arquivo = open(ConectorBanco.Refugio.CAMINHO_BANCO_DE_DADOS, 'w', encoding='utf-8')
            arquivo.writelines(linhas)
            arquivo.close()

        def deletar(indice):
            arquivo = open(ConectorBanco.Refugio.CAMINHO_BANCO_DE_DADOS, 'r', encoding='utf-8')
            linhas = arquivo.readlines()
            arquivo.close()
            
            del linhas[indice + 1]
            
            arquivo = open(ConectorBanco.Refugio.CAMINHO_BANCO_DE_DADOS, 'w', encoding='utf-8')
            arquivo.writelines(linhas)
            arquivo.close()


    class Usuario:
        CAMINHO_BANCO_DE_DADOS = 'oasis/banco_de_dados/usuarios.txt'
        
        def cadastrar(usuario, senha, latitude, longitude):
            arquivo = open(ConectorBanco.Usuario.CAMINHO_BANCO_DE_DADOS, 'a', encoding='utf-8')
            try:
                arquivo.write(f"| {usuario} | {senha} | leitura_apenas | {latitude} | {longitude} |\n")
            finally:
                arquivo.close()
                
        def autenticar(usuario, senha):
            arquivo = open(ConectorBanco.Usuario.CAMINHO_BANCO_DE_DADOS, 'r', encoding='utf-8')
            try:
                linhas = arquivo.readlines()[1:] 
                for linha in linhas:
                    if not linha.strip():
                        continue
                        
                    dados = linha.strip().split('|')
                    
                    if len(dados) >= 6:
                        u_salvo = dados[1].strip()
                        s_salva = dados[2].strip()
                        tipo_salvo = dados[3].strip()
                        lat_salvo = dados[4].strip()
                        lon_salvo = dados[5].strip()
                        
                        if u_salvo == usuario and s_salva == senha:
                            return UsuarioObj(u_salvo, s_salva, tipo_salvo, lat_salvo, lon_salvo)
            finally:
                arquivo.close()
            return None

        def buscar_todos():
            arquivo = open(ConectorBanco.Usuario.CAMINHO_BANCO_DE_DADOS, 'r', encoding='utf-8')
            lista_usuarios = []
            try:
                linhas = arquivo.readlines()[1:]
                for linha in linhas:
                    if not linha.strip(): continue
                    dados = linha.strip().split('|')
                    if len(dados) >= 6:
                        u_salvo = dados[1].strip()
                        s_salva = dados[2].strip()
                        tipo_salvo = dados[3].strip()
                        lat_salvo = dados[4].strip()
                        lon_salvo = dados[5].strip()
                        lista_usuarios.append(UsuarioObj(u_salvo, s_salva, tipo_salvo, lat_salvo, lon_salvo))
            finally:
                arquivo.close()
            return lista_usuarios

        def atualizar(indice, usuario_obj):
            arquivo = open(ConectorBanco.Usuario.CAMINHO_BANCO_DE_DADOS, 'r', encoding='utf-8')
            linhas = arquivo.readlines()
            arquivo.close()
            
            linha_formatada = f"| {usuario_obj.username} | {usuario_obj.senha} | {usuario_obj.tipo} | {usuario_obj.latitude} | {usuario_obj.longitude} |\n"
            linhas[indice + 1] = linha_formatada
            
            arquivo = open(ConectorBanco.Usuario.CAMINHO_BANCO_DE_DADOS, 'w', encoding='utf-8')
            arquivo.writelines(linhas)
            arquivo.close()

        def deletar(indice):
            arquivo = open(ConectorBanco.Usuario.CAMINHO_BANCO_DE_DADOS, 'r', encoding='utf-8')
            linhas = arquivo.readlines()
            arquivo.close()
            
            del linhas[indice + 1]
            
            arquivo = open(ConectorBanco.Usuario.CAMINHO_BANCO_DE_DADOS, 'w', encoding='utf-8')
            arquivo.writelines(linhas)
            arquivo.close()

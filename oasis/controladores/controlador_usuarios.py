from modelos_de_objetos.usuario import UsuarioObj

class ControladorUsuarios:
    CAMINHO_BANCO_DE_DADOS = 'oasis/banco_de_dados/usuarios.txt'
    
    @staticmethod
    def cadastrar(usuario, senha, latitude, longitude):
        arquivo = open(ControladorUsuarios.CAMINHO_BANCO_DE_DADOS, 'a', encoding='utf-8')
        try:
            arquivo.write(f"| {usuario} | {senha} | leitura_apenas | {latitude} | {longitude} |\n")
        finally:
            arquivo.close()
            
    @staticmethod
    def autenticar(usuario, senha):
        arquivo = open(ControladorUsuarios.CAMINHO_BANCO_DE_DADOS, 'r', encoding='utf-8')
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

    @staticmethod
    def buscar_todos():
        arquivo = open(ControladorUsuarios.CAMINHO_BANCO_DE_DADOS, 'r', encoding='utf-8')
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

    @staticmethod
    def atualizar(indice, usuario_obj):
        arquivo = open(ControladorUsuarios.CAMINHO_BANCO_DE_DADOS, 'r', encoding='utf-8')
        linhas = arquivo.readlines()
        arquivo.close()
        
        linha_formatada = f"| {usuario_obj.username} | {usuario_obj.senha} | {usuario_obj.tipo} | {usuario_obj.latitude} | {usuario_obj.longitude} |\n"
        linhas[indice + 1] = linha_formatada
        
        arquivo = open(ControladorUsuarios.CAMINHO_BANCO_DE_DADOS, 'w', encoding='utf-8')
        arquivo.writelines(linhas)
        arquivo.close()

    @staticmethod
    def deletar(indice):
        arquivo = open(ControladorUsuarios.CAMINHO_BANCO_DE_DADOS, 'r', encoding='utf-8')
        linhas = arquivo.readlines()
        arquivo.close()
        
        del linhas[indice + 1]
        
        arquivo = open(ControladorUsuarios.CAMINHO_BANCO_DE_DADOS, 'w', encoding='utf-8')
        arquivo.writelines(linhas)
        arquivo.close()

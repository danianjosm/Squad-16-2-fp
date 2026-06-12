from utilitarios.conector_banco import ConectorBanco
from modelos_de_objetos.usuario import UsuarioObj

def listar_usuarios():
    print("\n--- LISTA DE USUÁRIOS ---")
    usuarios = ConectorBanco.Usuario.buscar_todos()
    for i, u in enumerate(usuarios):
        print(f"{i} - {u.username} | {u.tipo.upper()}")
    input("\nPressione Enter para voltar...")

def editar_usuario():
    print("\n--- EDITAR USUÁRIO ---")
    usuarios = ConectorBanco.Usuario.buscar_todos()
    for i, u in enumerate(usuarios):
        print(f"{i} - {u.username} ({u.tipo})")
        
    try:
        idx = int(input("\nDigite o número do usuário para editar: "))
        if 0 <= idx < len(usuarios):
            u = usuarios[idx]
            print(f"\nEditando: {u.username}")
            print("Dica: Aperte Enter sem digitar nada para manter a informação atual.")
            
            novo_user = input(f"Novo username ({u.username}): ") or u.username
            nova_senha = input(f"Nova senha ({u.senha}): ") or u.senha
            novo_tipo = input(f"Novo papel ({u.tipo}): ") or u.tipo
            nova_lat = input(f"Nova latitude ({u.latitude}): ") or u.latitude
            nova_lon = input(f"Nova longitude ({u.longitude}): ") or u.longitude
            
            user_editado = UsuarioObj(novo_user, nova_senha, novo_tipo, nova_lat, nova_lon)
            ConectorBanco.Usuario.atualizar(idx, user_editado)
            print("\nUsuário editado com sucesso!")
        else:
            print("\nNúmero inválido.")
    except ValueError:
        print("\nVocê não digitou um número válido.")
    input("Pressione Enter para voltar...")

def deletar_usuario():
    print("\n--- DELETAR USUÁRIO ---")
    usuarios = ConectorBanco.Usuario.buscar_todos()
    for i, u in enumerate(usuarios):
        print(f"{i} - {u.username} ({u.tipo})")
        
    try:
        idx = int(input("\nDigite o número do usuário para deletar: "))
        if 0 <= idx < len(usuarios):
            ConectorBanco.Usuario.deletar(idx)
            print("\nUsuário deletado com sucesso!")
        else:
            print("\nNúmero inválido.")
    except ValueError:
        print("\nVocê não digitou um número válido.")
    input("Pressione Enter para voltar...")

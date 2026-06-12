from controladores.controlador_usuarios import ControladorUsuarios
from modelos_de_objetos.usuario import UsuarioObj

def listar_usuarios():
    usuarios = ControladorUsuarios.buscar_todos()
    if not usuarios:
        print("\nNenhum usuário cadastrado no momento.")
        input("\nPressione Enter para voltar...")
        return
        
    pagina_atual = 0
    usuarios_por_pagina = 5
    
    while True:
        print("\n" * 50)
        print(f"--- LISTA DE USUÁRIOS (Página {pagina_atual + 1}) ---")
        
        indice_inicial = pagina_atual * usuarios_por_pagina
        indice_final = indice_inicial + usuarios_por_pagina
        usuarios_fatiados = usuarios[indice_inicial:indice_final]
        
        if not usuarios_fatiados:
            print("Fim da linha, sem dados")
        else:
            for i, u in enumerate(usuarios_fatiados):
                idx = indice_inicial + i
                print(f"{idx} - {u.username} | {u.tipo.upper()}")
                
        print("\n[ P ] Próxima Página  |  [ A ] Página Anterior  |  [ Qualquer tecla ] Voltar ao Menu")
        acao = input("Escolha o que fazer: ").strip().upper()
        
        if acao == 'P':
            if len(usuarios_fatiados) < usuarios_por_pagina or (pagina_atual + 1) * usuarios_por_pagina >= len(usuarios):
                print("\nVocê já está no limite! Não há próxima página.")
                input("Pressione Enter para continuar...")
            else:
                pagina_atual += 1
        elif acao == 'A':
            if pagina_atual > 0:
                pagina_atual -= 1
            else:
                print("\nVocê já está na primeira página!")
                input("Pressione Enter para continuar...")
        else:
            break

def editar_usuario():
    print("\n--- EDITAR USUÁRIO ---")
    usuarios = ControladorUsuarios.buscar_todos()
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
            ControladorUsuarios.atualizar(idx, user_editado)
            print("\nUsuário editado com sucesso!")
        else:
            print("\nNúmero inválido.")
    except ValueError:
        print("\nVocê não digitou um número válido.")
    input("Pressione Enter para voltar...")

def deletar_usuario():
    print("\n--- DELETAR USUÁRIO ---")
    usuarios = ControladorUsuarios.buscar_todos()
    for i, u in enumerate(usuarios):
        print(f"{i} - {u.username} ({u.tipo})")
        
    try:
        idx = int(input("\nDigite o número do usuário para deletar: "))
        if 0 <= idx < len(usuarios):
            ControladorUsuarios.deletar(idx)
            print("\nUsuário deletado com sucesso!")
        else:
            print("\nNúmero inválido.")
    except ValueError:
        print("\nVocê não digitou um número válido.")
    input("Pressione Enter para voltar...")

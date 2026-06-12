from utilitarios.conector_banco import ConectorBanco

while True:
    print("\n" * 50)
    print("--- ACESSO AO OASIS ---")
    print("1. Fazer Login")
    print("2. Cadastrar Novo Usuário")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        
        usuario_logado = ConectorBanco.Usuario.autenticar(usuario, senha)
        
        if usuario_logado is not None:
            import visualizadores.menu_principal
            visualizadores.menu_principal.exibir_menu(usuario_logado)
            break
        else:
            print("\nUsuário ou senha incorretos!")
            input("Pressione Enter para tentar de novo...")
            
    elif opcao == '2':
        usuario = input("Novo Usuário: ")
        senha = input("Nova Senha: ")
        lat = input("Sua Latitude (Ex: -8.0476): ")
        lon = input("Sua Longitude (Ex: -34.8770): ")
        
        ConectorBanco.Usuario.cadastrar(usuario, senha, lat, lon)
        print("\nUsuário cadastrado com sucesso! Agora você pode fazer login.")
        input("Pressione Enter para voltar...")
        
    elif opcao == '0':
        print("Até logo!")
        break
        
    else:
        print("Opção inválida.")
        input("Pressione Enter para continuar...")

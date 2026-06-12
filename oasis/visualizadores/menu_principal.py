from visualizadores import menu_refugios, menu_usuarios

def exibir_menu(usuario_logado):
    while True:
        print("\n" * 50)
        print(f"\n--- BEM VINDO AO OASIS ({usuario_logado.tipo.upper()}) ---")
        
        print("1. Listar refúgios (paginado)")
        print("2. Buscar refúgios mais próximos")
        
        if usuario_logado.is_admin():
            print("3. Criar novo refúgio")
            print("4. Editar refúgio")
            print("5. Deletar refúgio")
            print("6. Listar todos os usuários")
            print("7. Editar usuário")
            print("8. Deletar usuário")
            
        print("0. Sair do programa")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            menu_refugios.listar_paginado()
            
        elif opcao == '2':
            menu_refugios.buscar_proximos(usuario_logado)
            
        elif opcao == '3' and usuario_logado.is_admin():
            menu_refugios.criar_refugio()
            
        elif opcao == '4' and usuario_logado.is_admin():
            menu_refugios.editar_refugio()
            
        elif opcao == '5' and usuario_logado.is_admin():
            menu_refugios.deletar_refugio()

        elif opcao == '6' and usuario_logado.is_admin():
            menu_usuarios.listar_usuarios()

        elif opcao == '7' and usuario_logado.is_admin():
            menu_usuarios.editar_usuario()

        elif opcao == '8' and usuario_logado.is_admin():
            menu_usuarios.deletar_usuario()
            
        elif opcao == '0':
            print("Saindo do Oasis. Até logo!")
            break
            
        else:
            print("Opção inválida ou você não tem permissão para isso!")
            input("Pressione Enter para continuar...")

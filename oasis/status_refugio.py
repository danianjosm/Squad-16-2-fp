def atualizar_status(refugios, usuario_logado):
    # filtrando para os refugios da pessoa logada
    refugios_do_usuario = [r for r in refugios if r.usuario == usuario_logado]
    
    if not refugios_do_usuario:
        print(f"Você não tem refúgios cadastrados")
        return

    listar_refugios(refugios_do_usuario)

    num_refugio = int(input("\nDigite o número do refúgio: "))
    refugio = refugios_do_usuario[num_refugio - 1]
    
    # status atual
    if refugio.status:
        print(f"\nStatus atual de: ativo")
    else:
        print(f"\nStatus atual de: fechado")
    
    # escolhe o novo status
    print("\n1. Marcar como ativo")
    print("2. Marcar como fechado")
    escolha = int(input("\nEscolha: "))
    
    if escolha == 1:
        refugio.status = True
        print(f"Status atualizado para: Ativo!")
    elif escolha == 2:
        refugio.status = False
        print(f"Status atualizado para: Fechado!")
    else:
        print("Opção inválida!")
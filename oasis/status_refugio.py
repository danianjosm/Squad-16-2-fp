def atualizar_status(refugios):
    listar_refugios(refugios)
    
    num_refugio = int(input("\nDigite o número do refúgio: "))
    refugio = refugios[num_refugio - 1]
    
    # mostra o status atual
    if refugio.status:
        print(f"\nStatus atual de {refugio.nome}: ativo")
    else:
        print(f"\nStatus atual de {refugio.nome}: fechado")
    
    # usuário escolhe o novo status
    print("\n1. Marcar como ativo")
    print("2. Marcar como fechado")
    escolha = int(input("Escolha: "))
    
    if escolha == 1:
        refugio.status = True
        print(f"Status atualizado para: ativo!")
    elif escolha == 2:
        refugio.status = False
        print(f"Status atualizado para: fechado!")
    else:
        print("Opção inválida!")
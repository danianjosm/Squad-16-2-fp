from controladores.controlador_refugios import ControladorRefugios

def atualizar_status_refugio():
    print("\n--- ATUALIZAR STATUS DE REFÚGIO ---")


    refugios = ControladorRefugios.buscar_todos()


    if not refugios:
        print("Nenhum refúgio cadastrado.")
        input("Pressione Enter para voltar...")
        return

    for i, r in enumerate(refugios):
        print(f"{i} - {r.nome} | {r.endereco} | Status: {r.status}")

    try:
        idx = int(input("\nDigite o número do refúgio para alterar o status: "))

        if 0 <= idx < len(refugios):
            refugio = refugios[idx]

            print(f"\nRefúgio: {refugio.nome}")
            print(f"Status atual: {refugio.status}")

            print("\n1. Marcar como ATIVO")
            print("2. Marcar como FECHADO")
            escolha = int(input("\nEscolha: "))

            if escolha == 1:
                refugio.status = 'ATIVO'
                ControladorRefugios.atualizar(idx, refugio)
                print("\n Status atualizado para: ATIVO!")
            elif escolha == 2:
                refugio.status = 'FECHADO'
                ControladorRefugios.atualizar(idx, refugio)
                print("\n Status atualizado para: FECHADO!")
            else:
                print("\nOpção inválida!")
        else:
            print("\nNúmero inválido")
    except ValueError:
        print("\nVocê não digitou um número válido.")
    
    input("Pressione Enter para voltar...")
from utilitarios.conector_banco import ConectorBanco
from modelos_de_objetos.refugio import RefugioObj

def atualizar_status_refugio():
    print("\n--- ATUALIZAR STATUS DE RÉFUGIO ---")0


    refugios = ConectorBanco.Refugio.buscar_todos()


    if not refugios:
        print("Nenhum refúgio cadastrado.")
        input("Pressione Enter para voltar...")
        return

    for i, r in enumerate(refugios):
        print(f"{i} - {r.nome} | {r.endereco} | Status: {r.status}")

    try:
        idx = int(input("\nDIgite o número do refúgio para alterar o status: "))

        if 0 <= idx < len(refugios):
            refugio = refugios[idx]

            print(f"\nRefúgio: {refugio.nome}")
            print(f"Status atual: {refugio.status}")

            print("\n1. Marcar como ATIVO")
            print("2. Marcar como FECHADO")
            escolha = int(input("\nEscolha: "))

            if escolha == 1:
                refugio.status = 'ATIVO'
                ConectorBanco.Refugio.atualizar(idx, refugio)
                print("\n Status atualizado para: ATIVO!")
            elif escolha == 2:
                refugio.status = 'FECHADO'
                ConectorBanco.Refugio.atualizar(idx, refugio)
                print("\n Status atualizado para: FECHADIO!")
            else:
                print("\nOpção inválida!")
        else:
            print("\nNúmero inválido")
    except ValueError:
        print("\nVocê não digitou um número válido.")
    
    input("Pressione Enter para voltar...")
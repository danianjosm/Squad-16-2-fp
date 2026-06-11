def listar_refugios(refugios):
    print("\n===== REFÚGIOS CADASTRADOS =====")

    if not refugios:
        print("Nenhum refúgio cadastrado.")
        return
    
    for i, refugio in enumerate(refugios, start=1):
        print(f"{i}. {refugio}")
    
    print("=" * 32)
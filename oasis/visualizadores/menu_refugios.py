from utilitarios.conector_banco import ConectorBanco
from modelos_de_objetos.refugio import RefugioObj

def listar_paginado():
    pagina_atual = 0
    lojas_por_pagina = 5
    
    while True:
        print("\n" * 50)
        print(f"--- LISTA DE REFÚGIOS (Página {pagina_atual + 1}) ---")
        indice_inicial = pagina_atual * lojas_por_pagina
        
        quantidade_impressa = ConectorBanco.Refugio.selecionar(lojas_por_pagina, indice_inicial)
        
        print("\n[ P ] Próxima Página  |  [ A ] Página Anterior  |  [ Qualquer tecla ] Voltar ao Menu")
        acao = input("Escolha o que fazer: ").strip().upper()
        
        if acao == 'P':
            if quantidade_impressa < lojas_por_pagina:
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

def buscar_proximos(usuario_logado):
    print("\n--- OS 3 REFÚGIOS MAIS PRÓXIMOS DE VOCÊ ---")
    todas_as_lojas = ConectorBanco.Refugio.buscar_todos()
    
    if len(todas_as_lojas) == 0:
        print("Nenhum refúgio cadastrado no momento.")
    else:
        todas_as_lojas.sort(key=lambda loja: loja.calcular_distancia(usuario_logado.latitude, usuario_logado.longitude))
        
        for i, loja in enumerate(todas_as_lojas[:3]):
            print(f"{i+1}º Lugar - {loja.nome}")
            print(f"   Endereço: {loja.endereco}")
            print(f"   Status: {loja.status} | Recursos: {loja.recursos}\n")
            
    input("Pressione Enter para voltar...")

def criar_refugio():
    print("\n--- CADASTRO DE NOVO REFÚGIO ---")
    nome = input("Nome do refúgio (Ex: #133 REFÚGIO NOVO): ")
    end = input("Endereço (Ex: PE, RECIFE, CENTRO): ")
    status = input("Status (ATIVO/FECHADO): ")
    rec = input("Recursos (Ex: ['ÁGUA']): ")
    lat = input("Latitude (Ex: -8.0476): ")
    lon = input("Longitude (Ex: -34.8770): ")
    
    nova_loja = RefugioObj(nome, end, status, rec, lat, lon)
    ConectorBanco.Refugio.inserir(nova_loja)
    
    print("\nRefúgio criado com sucesso!")
    input("Pressione Enter para voltar...")

def editar_refugio():
    print("\n--- EDITAR REFÚGIO ---")
    lojas = ConectorBanco.Refugio.buscar_todos()
    for i, l in enumerate(lojas):
        print(f"{i} - {l.nome} ({l.endereco})")
    
    try:
        idx = int(input("\nDigite o número numérico do refúgio para editar: "))
        if 0 <= idx < len(lojas):
            loja = lojas[idx]
            print(f"\nEditando: {loja.nome}")
            print("Dica: Aperte Enter sem digitar nada para manter a informação atual.")
            
            novo_nome = input(f"Novo nome ({loja.nome}): ") or loja.nome
            novo_end = input(f"Novo endereço ({loja.endereco}): ") or loja.endereco
            novo_status = input(f"Novo status ({loja.status}): ") or loja.status
            novo_rec = input(f"Novos recursos ({loja.recursos}): ") or loja.recursos
            nova_lat = input(f"Nova latitude ({loja.latitude}): ") or loja.latitude
            nova_lon = input(f"Nova longitude ({loja.longitude}): ") or loja.longitude
            
            loja_editada = RefugioObj(novo_nome, novo_end, novo_status, novo_rec, nova_lat, nova_lon)
            ConectorBanco.Refugio.atualizar(idx, loja_editada)
            print("\nRefúgio editado com sucesso!")
        else:
            print("\nNúmero inválido.")
    except ValueError:
        print("\nVocê não digitou um número válido.")
    input("Pressione Enter para voltar...")

def deletar_refugio():
    print("\n--- DELETAR REFÚGIO ---")
    lojas = ConectorBanco.Refugio.buscar_todos()
    for i, l in enumerate(lojas):
        print(f"{i} - {l.nome}")
        
    try:
        idx = int(input("\nDigite o número do refúgio para deletar: "))
        if 0 <= idx < len(lojas):
            ConectorBanco.Refugio.deletar(idx)
            print("\nRefúgio deletado com sucesso!")
        else:
            print("\nNúmero inválido.")
    except ValueError:
        print("\nVocê não digitou um número válido.")
    input("Pressione Enter para voltar...")

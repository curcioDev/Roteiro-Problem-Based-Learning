pecas = []
caixas = []
proximo_id_caixa = 1


def limpar_tela():
    print("\n" * 2)


def exibir_menu():
    print("=" * 60)
    print("   SISTEMA DE GESTÃO DE PEÇAS - CONTROLE DE QUALIDADE")
    print("=" * 60)
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair")
    print("=" * 60)


def avaliar_peca(peso, cor, comprimento):
    motivos_reprovacao = []
    
    if peso < 95 or peso > 105:
        motivos_reprovacao.append(f"Peso fora da faixa (95g-105g): {peso}g")
    
    cor_normalizada = cor.lower().strip()
    if cor_normalizada not in ['azul', 'verde']:
        motivos_reprovacao.append(f"Cor inválida (apenas azul ou verde): {cor}")
    
    if comprimento < 10 or comprimento > 20:
        motivos_reprovacao.append(f"Comprimento fora da faixa (10cm-20cm): {comprimento}cm")
    
    if len(motivos_reprovacao) == 0:
        status = "APROVADA"
    else:
        status = "REPROVADA"
    
    return status, motivos_reprovacao


def obter_caixa_aberta():
    global proximo_id_caixa
    
    for caixa in caixas:
        if caixa['status'] == 'aberta':
            return caixa
    
    nova_caixa = {
        'id_caixa': proximo_id_caixa,
        'pecas': [],
        'status': 'aberta'
    }
    caixas.append(nova_caixa)
    proximo_id_caixa += 1
    print(f"[INFO] Nova caixa criada: Caixa #{nova_caixa['id_caixa']}")
    
    return nova_caixa


def adicionar_peca_na_caixa(id_peca):
    caixa = obter_caixa_aberta()
    caixa['pecas'].append(id_peca)
    
    quantidade_atual = len(caixa['pecas'])
    print(f"[INFO] Peça #{id_peca} adicionada na Caixa #{caixa['id_caixa']} ({quantidade_atual}/10 peças)")
    
    if quantidade_atual >= 10:
        caixa['status'] = 'fechada'
        print(f"[INFO] Caixa #{caixa['id_caixa']} FECHADA (capacidade máxima atingida)")


def cadastrar_nova_peca():
    limpar_tela()
    print("-" * 60)
    print("   CADASTRO DE NOVA PEÇA")
    print("-" * 60)
    
    while True:
        id_peca = input("Digite o ID da peça: ").strip()
        if not id_peca:
            print("⚠ Erro: O ID não pode estar vazio. Tente novamente.")
            continue
        
        if any(p['id'] == id_peca for p in pecas):
            print(f"⚠ Erro: Já existe uma peça com o ID '{id_peca}'. Tente outro ID.")
            continue
        
        break
    
    while True:
        try:
            peso = float(input("Digite o peso da peça (em gramas): "))
            if peso <= 0:
                print("⚠ Erro: O peso deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("⚠ Erro: Digite um número válido para o peso.")
    
    print("\nCor da peça:")
    print("  1 - Azul")
    print("  2 - Verde")
    while True:
        opcao_cor = input("Escolha a cor (1 ou 2): ").strip()
        if opcao_cor == '1':
            cor = 'azul'
            break
        elif opcao_cor == '2':
            cor = 'verde'
            break
        else:
            print("⚠ Erro: Digite 1 para azul ou 2 para verde.")
    
    while True:
        try:
            comprimento = float(input("Digite o comprimento da peça (em centímetros): "))
            if comprimento <= 0:
                print("⚠ Erro: O comprimento deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("⚠ Erro: Digite um número válido para o comprimento.")
    
    status, motivos_reprovacao = avaliar_peca(peso, cor, comprimento)
    
    peca = {
        'id': id_peca,
        'peso': peso,
        'cor': cor,
        'comprimento': comprimento,
        'status': status,
        'motivos_reprovacao': motivos_reprovacao,
        'id_caixa': None
    }
    
    pecas.append(peca)
    
    print("\n" + "=" * 60)
    print(f"✓ Peça cadastrada com sucesso!")
    print(f"  Status: {status}")
    
    if status == "APROVADA":
        adicionar_peca_na_caixa(id_peca)
        caixa_atual = obter_caixa_aberta()
        for caixa in caixas:
            if id_peca in caixa['pecas']:
                peca['id_caixa'] = caixa['id_caixa']
                break
    else:
        print(f"  Motivos da reprovação:")
        for motivo in motivos_reprovacao:
            print(f"    - {motivo}")
    
    print("=" * 60)
    input("\nPressione ENTER para continuar...")


def listar_pecas():
    limpar_tela()
    print("-" * 60)
    print("   LISTAGEM DE PEÇAS")
    print("-" * 60)
    
    if len(pecas) == 0:
        print("Nenhuma peça cadastrada no sistema.")
        input("\nPressione ENTER para continuar...")
        return
    
    pecas_aprovadas = [p for p in pecas if p['status'] == 'APROVADA']
    pecas_reprovadas = [p for p in pecas if p['status'] == 'REPROVADA']
    
    print("\n✓ PEÇAS APROVADAS:")
    print("-" * 60)
    if len(pecas_aprovadas) == 0:
        print("  Nenhuma peça aprovada.")
    else:
        for peca in pecas_aprovadas:
            print(f"  ID: {peca['id']}")
            print(f"    Peso: {peca['peso']}g")
            print(f"    Cor: {peca['cor']}")
            print(f"    Comprimento: {peca['comprimento']}cm")
            if peca['id_caixa']:
                print(f"    Caixa: #{peca['id_caixa']}")
            print()
    
    print("\n✗ PEÇAS REPROVADAS:")
    print("-" * 60)
    if len(pecas_reprovadas) == 0:
        print("  Nenhuma peça reprovada.")
    else:
        for peca in pecas_reprovadas:
            print(f"  ID: {peca['id']}")
            print(f"    Peso: {peca['peso']}g")
            print(f"    Cor: {peca['cor']}")
            print(f"    Comprimento: {peca['comprimento']}cm")
            print(f"    Motivos da reprovação:")
            for motivo in peca['motivos_reprovacao']:
                print(f"      - {motivo}")
            print()
    
    print("=" * 60)
    print(f"Total: {len(pecas_aprovadas)} aprovadas | {len(pecas_reprovadas)} reprovadas")
    print("=" * 60)
    input("\nPressione ENTER para continuar...")


def remover_peca():
    limpar_tela()
    print("-" * 60)
    print("   REMOVER PEÇA CADASTRADA")
    print("-" * 60)
    
    if len(pecas) == 0:
        print("Nenhuma peça cadastrada no sistema.")
        input("\nPressione ENTER para continuar...")
        return
    
    print("\nPeças cadastradas:")
    for peca in pecas:
        print(f"  - ID: {peca['id']} | Status: {peca['status']}")
    
    print()
    id_peca = input("Digite o ID da peça que deseja remover (ou 'cancelar' para voltar): ").strip()
    
    if id_peca.lower() == 'cancelar':
        return
    
    peca_encontrada = None
    for peca in pecas:
        if peca['id'] == id_peca:
            peca_encontrada = peca
            break
    
    if peca_encontrada is None:
        print(f"\n⚠ Erro: Peça com ID '{id_peca}' não encontrada.")
        input("\nPressione ENTER para continuar...")
        return
    
    if peca_encontrada['id_caixa'] is not None:
        for caixa in caixas:
            if caixa['id_caixa'] == peca_encontrada['id_caixa']:
                if id_peca in caixa['pecas']:
                    caixa['pecas'].remove(id_peca)
                    print(f"[INFO] Peça removida da Caixa #{caixa['id_caixa']}")
                break
    
    pecas.remove(peca_encontrada)
    
    print(f"\n✓ Peça '{id_peca}' removida com sucesso!")
    input("\nPressione ENTER para continuar...")


def listar_caixas_fechadas():
    limpar_tela()
    print("-" * 60)
    print("   LISTAGEM DE CAIXAS FECHADAS")
    print("-" * 60)
    
    caixas_fechadas = [c for c in caixas if c['status'] == 'fechada']
    
    if len(caixas_fechadas) == 0:
        print("\nNenhuma caixa fechada ainda.")
    else:
        print(f"\nTotal de caixas fechadas: {len(caixas_fechadas)}\n")
        for caixa in caixas_fechadas:
            print(f"  Caixa #{caixa['id_caixa']} - Status: FECHADA")
            print(f"    Quantidade de peças: {len(caixa['pecas'])}")
            print(f"    IDs das peças: {', '.join(caixa['pecas'])}")
            print()
    
    print("=" * 60)
    input("\nPressione ENTER para continuar...")


def gerar_relatorio_final():
    limpar_tela()
    print("=" * 60)
    print("   RELATÓRIO FINAL DO SISTEMA")
    print("=" * 60)
    
    pecas_aprovadas = [p for p in pecas if p['status'] == 'APROVADA']
    pecas_reprovadas = [p for p in pecas if p['status'] == 'REPROVADA']
    caixas_fechadas = [c for c in caixas if c['status'] == 'fechada']
    
    print(f"\n1. RESUMO GERAL")
    print(f"   Total de peças cadastradas: {len(pecas)}")
    print(f"   Peças aprovadas: {len(pecas_aprovadas)}")
    print(f"   Peças reprovadas: {len(pecas_reprovadas)}")
    
    print(f"\n2. MOTIVOS DE REPROVAÇÃO")
    if len(pecas_reprovadas) == 0:
        print("   Nenhuma peça reprovada.")
    else:
        motivos_count = {
            'peso': 0,
            'cor': 0,
            'comprimento': 0
        }
        
        for peca in pecas_reprovadas:
            for motivo in peca['motivos_reprovacao']:
                if 'Peso' in motivo:
                    motivos_count['peso'] += 1
                if 'Cor' in motivo:
                    motivos_count['cor'] += 1
                if 'Comprimento' in motivo:
                    motivos_count['comprimento'] += 1
        
        print(f"   Peso fora da faixa: {motivos_count['peso']} ocorrências")
        print(f"   Cor inválida: {motivos_count['cor']} ocorrências")
        print(f"   Comprimento fora da faixa: {motivos_count['comprimento']} ocorrências")
    
    print(f"\n3. INFORMAÇÕES DE ARMAZENAMENTO")
    print(f"   Total de caixas utilizadas: {len(caixas)}")
    print(f"   Caixas fechadas: {len(caixas_fechadas)}")
    print(f"   Caixas abertas: {len(caixas) - len(caixas_fechadas)}")
    
    if len(caixas) > 0:
        print(f"\n4. DETALHAMENTO DAS CAIXAS")
        for caixa in caixas:
            status_texto = "FECHADA" if caixa['status'] == 'fechada' else "ABERTA"
            print(f"   Caixa #{caixa['id_caixa']} - {status_texto}")
            print(f"     Peças armazenadas: {len(caixa['pecas'])}/10")
            if len(caixa['pecas']) > 0:
                print(f"     IDs: {', '.join(caixa['pecas'])}")
    
    if len(pecas) > 0:
        taxa_aprovacao = (len(pecas_aprovadas) / len(pecas)) * 100
        print(f"\n5. INDICADORES DE QUALIDADE")
        print(f"   Taxa de aprovação: {taxa_aprovacao:.1f}%")
        print(f"   Taxa de reprovação: {100 - taxa_aprovacao:.1f}%")
    
    print("\n" + "=" * 60)
    input("\nPressione ENTER para continuar...")


def main():
    while True:
        limpar_tela()
        exibir_menu()
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == '1':
            cadastrar_nova_peca()
        elif opcao == '2':
            listar_pecas()
        elif opcao == '3':
            remover_peca()
        elif opcao == '4':
            listar_caixas_fechadas()
        elif opcao == '5':
            gerar_relatorio_final()
        elif opcao == '0':
            limpar_tela()
            print("=" * 60)
            print("   Encerrando o sistema...")
            print("   Obrigado por utilizar o Sistema de Gestão de Peças!")
            print("=" * 60)
            break
        else:
            print("\n⚠ Opção inválida! Por favor, escolha uma opção do menu.")
            input("Pressione ENTER para continuar...")


if __name__ == "__main__":
    main()

estoque_comida = {
    "Arroz": 6,
    "Queijo": 8,
    "Ovos": 4,
    "Cuscuz": 6,
    "Açucar": 5,
    "Sal": 10,
    "Oleo": 18,
    "Carne": 7,
    "Soja": 23,
    "Frutas": 8
}

estoque_bebida = {
    "Água Mineral(20L)": 50,
    "Polpa de laranja": 20,
    "Polpa uva": 18,
    "Leite": 25,
    "Chá Gelado": 15,
    "Suco de Tamarindo": 10,
    "Achocolatado": 22,
    "Iorgute natural": 12,
    "Água de Coco": 16,
    "Café com Leite": 14
}


def mostrar_estoque():
    """Mostra todos os produtos e suas quantidades."""
    print("Comidas:")
    for produto, qtd in estoque_comida.items():
        print(f"{produto}: {qtd}")
    print("Bebidas:")
    for produto, qtd in estoque_bebida.items():
        print(f"{produto}: {qtd}")


def adicionar_produto(nome, qtd):
    """Adiciona um novo produto ao estoque ou soma à quantidade existente."""
    while qtd <= 0:
        qtd = int(input("Digite um quantidade válida:"))
    if nome in estoque_comida:
        estoque_comida[nome] += qtd
    elif nome in estoque_bebida:
        estoque_bebida[nome] += qtd
    else:
        while True:
            tipo = input("Novo produto, selecione a categoria. Comida ou bebida? (C/B):").upper()
            if tipo == 'C':
                estoque_comida[nome] = qtd
            elif tipo == 'B':
                estoque_bebida[nome] = qtd
            else:
                print('Tipo inválido. Tente novamente.')
                continue
            break


def remover_produto(nome, qtd):
    """Remove certa quantidade do produto (se houver o suficiente)."""
    while qtd <= 0:
        print("Quantidade deve ser maior que zero!")
        qtd = int(input('Digite a quantidade nova:'))

    if nome in estoque_comida:
        if estoque_comida[nome] >= qtd:
            estoque_comida[nome] -= qtd
            print(f"Removido {qtd} unidades de {nome} com sucesso!")
        else:
            print(f"Quantidade insuficiente! Disponível: {estoque_comida[nome]}")
    elif nome in estoque_bebida:
        if estoque_bebida[nome] >= qtd:
            estoque_bebida[nome] -= qtd
            print(f"Removido {qtd} unidades de {nome} com sucesso!")
        else:
            print(f"Quantidade insuficiente! Disponível: {estoque_bebida[nome]}")

def consultar_produto(nome):
    """Mostra a quantidade atual de um produto específico."""
    if nome in estoque_comida:
        print(f"Há {estoque_comida[nome]} unidades de {nome} no estoque de Comida")
        return estoque_comida[nome]
    elif nome in estoque_bebida:
        print(f"Há {estoque_bebida[nome]} unidades de {nome} no estoque de Bebida")
        return estoque_bebida[nome]
    return None


def salvar_relatorio():
    """Gera um arquivo estoque.txt com os produtos e quantidades finais."""
    with open('estoque.txt', 'w') as f:
        f.write("RELATÓRIO DE ESTOQUE")
        f.write("COMIDAS:\n")
        for produto, qtd in estoque_comida.items():
            f.write(f"{produto}: {qtd}\n")
        f.write("\nBEBIDAS:\n")
        for produto, qtd in estoque_bebida.items():
            f.write(f"{produto}: {qtd}\n")


def repor_automatico():
    """Aumenta em 5 unidades qualquer item com quantidade menor que 3."""
    for produto in estoque_comida:
        if estoque_comida[produto] < 3:
            estoque_comida[produto] += 5
            print(f"Reposição automática: {produto} +5 unidades")
    for produto in estoque_bebida:
        if estoque_bebida[produto] < 3:
            estoque_bebida[produto] += 5
            print(f"Reposição automática: {produto} +5 unidades")


def menu():
    print("""Opções:
1. Mostrar estoque
2. Adicionar produto
3. Remover produto
4. Consultar produto
5. Salvar relatório
6. Repor produtos
7. Sair""")


while True:
    menu()
    opcao = str(input("Digite a opção:"))
    if opcao == '1':
        mostrar_estoque()
    elif opcao == '2':
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        adicionar_produto(nome, quantidade)
    elif opcao == '3':
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        if not remover_produto(nome, quantidade):
            print("Quantidade insuficiente ou produto não encontrado!")
    elif opcao == '4':
        nome = input("Nome do produto: ")
        quantidade = consultar_produto(nome)
        if quantidade is None:
            print("Produto não encontrado!")
    elif opcao == '5':
        salvar_relatorio()
        print("Relatório salvo em 'estoque.txt'")
    elif opcao == '6':
        repor_automatico()
    elif opcao == '7':
        break
    else:
        print("Opção inválida!")

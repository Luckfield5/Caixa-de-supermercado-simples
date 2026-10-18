# Caixa de supermercado

import json
import os


ARQUIVO = "produtos.json" # json para guardar os dados
SENHA_ADMIN = "061023" # Senha para o admin guardar produtos

# Carregar arquivos do .json
def carregar ():
    if not os.path.exists(ARQUIVO):
        return {}
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

# Salvar os produtos
def salvar(produtos):
        with open(ARQUIVO,"w", encoding="utf-8") as f:
            json.dump(produtos, f, ensure_ascii=False, indent=4)

# Listar os produtos
def listar(produtos):
    if not produtos:
        print("Nenhum produtos cadastrado.")
        return
    print("\n--- PRODUTOS---")
    for nome, preco in produtos.items():
        print(f"{nome}: R$ {preco:.2f}")

# Adicionar os produtos
def adicionar(produtos):
    senha = input("Digite a senha do Administrador: ")
    if senha != SENHA_ADMIN:
        print("Senha incorreta!. Acesso Negado!")
        return
    nome = input("Nome do produto: ").strip().lower()
    try:
        preco = float(input("Preço: R$ ").replace(",","."))
    except ValueError:
        print("Preço inválido!.")
        return
    produtos[nome] = preco
    salvar(produtos)
    print("Produto salvo!.")

#Esse é o caixa
def caixa(produtos):
    if not produtos:
        print("Cadastre produtos antes de usar o caixa")
        return
    subtotal = 0
    while True:
        nome = input("Produto(ou 'fim' para encerrar): ").strip().lower()
        if nome == "fim":
            break
        if nome not in produtos:
            print("Produto não encontrado")
            continue
        try:
            quantidade = int(input("Quantidade: "))
        except ValueError:
            print("Quantidade inválida!.")
            continue
        subtotal += produtos[nome] * quantidade # O subtotal da compra

# Desconto, Subtotal e Total das compras
    desconto = subtotal * 0.10 if subtotal >= 100 else 0
    total = subtotal - desconto
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Total: R$ {total:.2f}")

# Carregar os produtos
produtos = carregar()

# While para mostrar as opções
while True:
    print("\n1 - Caixa")
    print("2 - Listar produtos")
    print("3 - Adicionar produto (Apenas Admins)")
    print("4 - Sair")
    opcao = input("Escolha uma das opções: ")

    if opcao == "1":
        caixa(produtos)
    elif opcao == "2":
        listar(produtos)
    elif opcao == "3":
        adicionar(produtos)
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção Inválida")

# Caixa de Supermercado

Sistema de caixa em Python para terminal, com cadastro de produtos e preços salvos em arquivo JSON. Projeto de estudo da faculdade (ADS).

## Funcionalidades

- Caixa: registra vários produtos e quantidades, calcula subtotal, desconto e total
- Desconto de 10% em compras a partir de R$ 100,00
- Listagem de produtos e preços cadastrados
- Cadastro de novos produtos, protegido por senha de administrador
- Dados salvos em `produtos.json`, então nada se perde ao fechar o programa

## Tecnologias

- Python 3
- Módulos `json` e `os` (biblioteca padrão, não precisa instalar nada)

## Como usar

```
1 - Caixa
2 - Listar produtos
3 - Adicionar produto (apenas admins)
4 - Sair
```

Para cadastrar produtos, escolha a opção 3 e informe a senha de administrador definida em `SENHA_ADMIN` no código.

## O que aprendi

- Funções, dicionários, laços e tratamento de erros com `try/except`
- Leitura e escrita de arquivos JSON
- Controle de versão com Git e GitHub

## Próximas melhorias

- [ ] Remover e editar produtos
- [ ] Cupom fiscal com a lista de itens
- [ ] Trocar o JSON por SQLite

## Autor
Lucas Limeira. Obrigado por ver meu projeto

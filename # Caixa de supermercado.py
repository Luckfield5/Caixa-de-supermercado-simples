# Caixa de supermercado
produto = input("Digite o produto: ")
preco = float(input("Preço: R$ "))
quantidade = int(input("Quantidade: "))

subtotal = preco * quantidade
if subtotal >= 100:
    desconto = subtotal * 0.10
else:
    desconto = 0
total = subtotal - desconto

print(f"Produto: {produto}")
print(f"Subtotal: R$ {subtotal: 2f}")
print(f"Desconto: R$ {desconto: .2f}")
print(f"Total: R$ {total: .2f}")
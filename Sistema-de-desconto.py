# Sistema de desconto progressivo
# O desconto é definido de acordo com o valor total da compra.

# Entrada do valor da compra
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Verifica qual desconto deve ser aplicado
if valor_compra < 200:
    desconto = 0.05
elif valor_compra < 300:
    desconto = 0.10
else:
    desconto = 0.15

# Calcula o valor do desconto
valor_desconto = valor_compra * desconto

# Calcula o valor final da compra
valor_final = valor_compra - valor_desconto

# Exibe os resultados
print("\n--- Resultado da compra ---")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor a pagar: R$ {valor_final:.2f}")
# Preço com Desconto
# Descrição: Peça o preço original de um produto e a porcentagem de desconto. Calcule e mostre o preço final após o desconto.

preco = float(input("Digite o preço do produto: "))
porcentagem = int(input("Digite a porcentagem do desconto: "))
desconto = preco * (porcentagem / 100)

valor_final = preco - desconto

print(f"O preço com desconto é de: R${valor_final:.2f}")
print("Bem-vindo ao PDV")

compras = []

while True: 
    valor = float(input("Digite o valor da compra: "))

    if valor == 0:
        break

    idade = int(input("Digite sua idade: "))

    if valor < 0 or idade < 0:
        print("Valor ou idade não podem ser negativos.Por favor, informe um valor positivo")
        continue

    valor_final = valor

    if idade >= 65:
        valor_final *= 0.80
    if valor_final > 100:
        valor_final *= 0.90

    valor_final = valor_final

    desconto = valor - valor_final

    compras.append({
        "valor": valor ,
        "desconto_aplicado": desconto,
        "valor_final": valor_final
    })

    print(f"Valor final: R$ {valor_final:.2f}")
    print()

quantidade = len(compras)

total_bruto = 0 
total_descontos = 0 
total_final = 0 

for compra in compras:
    total_bruto += compra["valor"]
    total_descontos += compra["desconto_aplicado"]
    total_final += compra["valor_final"]

print("\nResumo")
print("Quantidade de compras:", quantidade)
print(f"Total Bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos concedidos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")


    

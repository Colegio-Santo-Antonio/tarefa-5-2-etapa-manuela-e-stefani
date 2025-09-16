# Leia uma linha com o número do cartão
# student.py

# Lê o número do cartão (string de dígitos)
cartao = input().strip()

# Transforma em lista de inteiros
digitos = [int(d) for d in cartao]

# Separar ímpares e pares a partir da direita
# ímpares (posição -1, -3, -5, ...)
impares = digitos[-1::-2]
# pares (posição -2, -4, -6, ...)
pares = digitos[-2::-2]

# Soma dos ímpares
soma_impares = sum(impares)

# Tratamento dos pares: dobrar e somar dígitos se necessário
soma_pares = 0
for p in pares:
    dobro = p * 2
    if dobro >= 10:
        dobro = (dobro // 10) + (dobro % 10)  # soma os dígitos
    soma_pares += dobro

# Soma total
soma_total = soma_impares + soma_pares

# Verifica se é múltiplo de 10
if soma_total % 10 == 0:
    print("Cartão válido")
else:
    print("Cartão inválido")

# TODO: implemente a verificação pelo algoritmo de Luhn
# Siga as dicas do README.

# Ao final, imprima exatamente:
# print("Cartão válido")  ou  print("Cartão inválido")

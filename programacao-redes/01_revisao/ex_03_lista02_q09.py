preco = float(input("Digite o preço do produto: "))

if preco > 0:
    if preco <= 50:
        aumento = 0.05
    elif preco > 100:
        aumento = 0.15
    else:
        aumento = 0.10

    valor_aumento = preco * aumento
    novo_preco = preco + valor_aumento

    if novo_preco <= 80:
        classificacao = "barato"
    elif 80 < novo_preco <= 120:
        classificacao = "normal"
    elif 120 < novo_preco <= 200:
        classificacao = "caro"
    else:
        classificacao = "muito caro"

    print(f"O valor do aumento será R$ {valor_aumento:.2f}")
    print(f"O novo preço será R$ {novo_preco:.2f}")
    print(f"O novo preço do produto é {classificacao}!")
else:
    print("O preço deve ser maior que zero!")

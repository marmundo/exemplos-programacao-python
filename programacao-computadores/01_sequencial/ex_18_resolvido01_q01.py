quantidade_paes = int(input("Digite a quantidade de pães: "))
quantidade_envelhecidos = int(input(f"Dos {quantidade_paes} pães, quantos são envelhecidos: "))

quantidade_novos = quantidade_paes - quantidade_envelhecidos

preco_total_sem_desconto = quantidade_paes * 0.25
preco_total_com_desconto = quantidade_novos * 0.25 + quantidade_envelhecidos * 0.25 / 2
valor_desconto = preco_total_sem_desconto - preco_total_com_desconto

print(f"Você comprou {quantidade_novos} pães novos e {quantidade_envelhecidos} pães envelhecidos.")
print(f"O preço sem desconto é R$ {preco_total_sem_desconto:.2f}")
print(f"O valor do desconto é R$ {valor_desconto:.2f}")
print(f"O preço com desconto é R$ {preco_total_com_desconto:.2f}")

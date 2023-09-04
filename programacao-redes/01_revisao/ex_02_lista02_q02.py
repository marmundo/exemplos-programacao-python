nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print(f"A média é {media}")

if 7 <= media <= 10:  # media >= 7 and media <= 10:
    print("Aprovado!")
elif 4 <= media < 7:
    print("Prova Final!")
elif 0 <= media < 4:
    print("Reprovado!")
else:
    print("Média inválida!")

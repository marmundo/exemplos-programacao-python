nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2
print(f"A média do aluno foi {media:.1f}!")

if media >= 9:
    print("O aluno está aprovado com louvor!")
elif media >= 6:
    print("O aluno está aprovado!")
elif media == 0:
    print("O importante é ser feliz!")
elif media < 2:
    print("O aluno está reprovado!")
else:
    print("O aluno está em recuperação!")

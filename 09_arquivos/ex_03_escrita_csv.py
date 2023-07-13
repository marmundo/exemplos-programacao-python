arquivo = open("contatos.csv", "a", encoding="utf-8")

nome = input("Digite o nome: ")
email = input("Digite o e-mail: ")
telefone = input("Digite o telefone: ")

arquivo.write(f"{nome};{email};{telefone}\n")

arquivo.close()

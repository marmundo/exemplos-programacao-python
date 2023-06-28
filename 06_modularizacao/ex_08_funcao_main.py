def fatorial_for(n):
    fatorial = 1

    for i in range(n, 1, -1):
        fatorial *= i

    return fatorial


def fatorial_rec(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial_rec(n - 1)


def main():
    numero = int(input("Digite um valor inteiro: "))
    print(f"O fatorial com 'for' de {numero} é {fatorial_for(numero)}!")
    print(f"O fatorial 'recursivo' de {numero} é {fatorial_rec(numero)}!")


main()

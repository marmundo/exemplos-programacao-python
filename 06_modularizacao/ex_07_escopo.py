a = 10


def funcao1():
    a = 20
    print("Função 1:", a)


def funcao2():
    print("Função 2:", a)


def funcao3():
    global a
    print("Função 3.1:", a)
    a = 20
    print("Função 3.2:", a)


funcao1()
print("Depois da função 1:", a)

funcao2()
print("Depois da função 2:", a)

funcao3()
print("Depois da função 3:", a)

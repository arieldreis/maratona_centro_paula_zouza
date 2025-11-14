# Exemplo E
while True:
    pontos_variacoes_energia = int(input())
    lista_variacao_energia = []
    energia = 0
    nivel = 0
    menor_nivel = 0
    if pontos_variacoes_energia == 0:
        break
    for index in range(pontos_variacoes_energia):
        variacao_energia = int(input())
        lista_variacao_energia.append(variacao_energia)
    soma = sum(lista_variacao_energia)
    print(soma)
    # print(min(lista_variacao_energia))
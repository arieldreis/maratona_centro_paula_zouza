while True:
    quantidade_paradas = int(input())
    ocupacao_atual = 0
    maior_ocupacao = 0
    if quantidade_paradas == 0:
        break
    for index in range(quantidade_paradas):
        entrada, saida = map(int, input().split())
        ocupacao_atual+=entrada
        ocupacao_atual-=saida
        if ocupacao_atual > maior_ocupacao:
            maior_ocupacao = ocupacao_atual
    print(maior_ocupacao)
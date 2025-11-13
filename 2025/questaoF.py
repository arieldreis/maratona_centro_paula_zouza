# Exemplo F
while True:
    listaDados = []
    quantidade = int(input())
    if quantidade == 0:
        break
    for index in range(quantidade):
        teste_casos = int(input())
        listaDados.append(teste_casos)
    maior = max(listaDados)
    menor = min(listaDados)
    media = sum(listaDados) / len(listaDados)
    print(maior, menor, media)
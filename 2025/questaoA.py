# Exemplo A
while True:
    quantidade_medicoes = int(input())
    lista_medidas = []
    if quantidade_medicoes == 0:
        break
    for index in range(quantidade_medicoes):
        potencias_medidas = int(input())
        lista_medidas.append(potencias_medidas)
    calculo_potencias = sum(lista_medidas) - (sum(lista_medidas) * 0.1)
    print(calculo_potencias)
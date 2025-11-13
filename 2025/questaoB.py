# Exemplo B
while True:
    quantidade_drones = int(input())
    listaDrones = []
    if quantidade_drones == 0:
        break
    for index in range(quantidade_drones):
        v1, v2, v3, v4, v5 = map(int, input().split())
        dadosDrones = v1, v2, v3, v4, v5
        listaDrones.append(dadosDrones)

    print(listaDrones)


#  beecrowd | 1973
#  Jornada nas Estrelas

estrelas = int(input())

lista_carneiros = list(map(int, input().split()))
i = 0
aux = [0] * estrelas
carneiros_roubados = 0

while i in range(estrelas):
    if lista_carneiros[i] > 0:
        if lista_carneiros[i] % 2 == 0:
            if aux[i] == 0:
                aux[i] = 1
            lista_carneiros[i] -= 1
            carneiros_roubados += 1
            i -= 1
        else:
            if aux[i] == 0:
                aux[i] = 1
            lista_carneiros[i] -= 1
            carneiros_roubados += 1
            i += 1
    else:
        if lista_carneiros[i] % 2 == 0:
            if aux[i] == 0:
                aux[i] = 1
            i -= 1
        else:
            if aux[i] == 0:
                aux[i] = 1
            i += 1

print(sum(aux), sum(lista_carneiros))

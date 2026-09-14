import heapq
import itertools
import math


def distancia_euclidiana(coord_a, coord_b):
    xa, ya = coord_a
    xb, yb = coord_b
    return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)


def a_star_search(grafo, coordenadas, inicio, destino):
    contador = itertools.count()  # desempate para o heap

    h_inicio = distancia_euclidiana(coordenadas[inicio], coordenadas[destino])
    lista_aberta = [(h_inicio, next(contador), inicio, 0, None)]

    tabela_hash = {} # nos completamente expandidos

    veio_de = {}

    while lista_aberta:
        f_atual, _, atual, g_atual, pai = heapq.heappop(lista_aberta)

        if atual in tabela_hash:
            continue

        tabela_hash[atual] = g_atual         # fecha o no, registra na tabela hash e guarda o caminho ate ele.
        veio_de[atual] = pai

        if atual == destino:
            break

        for vizinho, custo_aresta in grafo.get(atual, []):         # processa os sub-nos (vizinhos) do no atual.
            if vizinho in tabela_hash:
                continue  # ja fechado, ignora

            novo_custo = g_atual + custo_aresta
            h_vizinho = distancia_euclidiana(coordenadas[vizinho], coordenadas[destino])
            f_vizinho = novo_custo + h_vizinho

            heapq.heappush(
                lista_aberta, (f_vizinho, next(contador), vizinho, novo_custo, atual)
            )

    return veio_de, tabela_hash


def reconstruir_caminho(veio_de, inicio, destino):
    if destino not in veio_de:
        return []

    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = veio_de.get(atual)

    caminho.reverse()

    if not caminho or caminho[0] != inicio:
        return []

    return caminho
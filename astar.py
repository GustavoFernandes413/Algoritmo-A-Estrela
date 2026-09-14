import math


def distancia_euclidiana(coord_a, coord_b): # calcula distancia euclideana
    xa, ya = coord_a
    xb, yb = coord_b
    return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)


def a_star_search(grafo, coordenadas, inicio, destino):
    lista_aberta = [inicio] # nos descobertos mas nao expandidos
    lista_fechada = [] # nos expandidos
    tabela_hash = {inicio: 0} # menor custo g(n) p/ cada no, registro de nos processados

    veio_de = {inicio: None}

    while lista_aberta:
        atual = min(
            lista_aberta,
            key=lambda no: tabela_hash[no]
            + distancia_euclidiana(coordenadas[no], coordenadas[destino]),
        )

        if atual == destino:
            break

        lista_aberta.remove(atual)
        lista_fechada.append(atual)

        for vizinho, custo_aresta in grafo.get(atual, []): # processa os nos vizinhos do atual
            if vizinho in lista_fechada:
                continue  # ja foi totalmente explorado, ignora

            novo_custo = tabela_hash[atual] + custo_aresta

            if vizinho not in tabela_hash or novo_custo < tabela_hash[vizinho]: # atualiza se for a
                # primeira vez alcancando o vizinho ou se encontrar um caminho mais barato
                tabela_hash[vizinho] = novo_custo
                veio_de[vizinho] = atual

                if vizinho not in lista_aberta:
                    lista_aberta.append(vizinho)

    return veio_de, tabela_hash


def reconstruir_caminho(veio_de, inicio, destino):
    if destino not in veio_de:
        return []

    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = veio_de[atual]

    caminho.reverse()

    if not caminho or caminho[0] != inicio: # validacao p/ garantir que comeca no no de inicio
        return []

    return caminho
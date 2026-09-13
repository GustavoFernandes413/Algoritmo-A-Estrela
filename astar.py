import heapq

class PriorityQueue:
    def __init__(self):
        self.elementos = []

    def vazia(self):
        return not self.elementos

    def inserir(self, item, prioridade):
        heapq.heappush(self.elementos, (prioridade, item))

    def remover(self):
        return heapq.heappop(self.elementos)[1]


def a_star_search(grafo, heuristicas, inicio, destino):
    fronteira = PriorityQueue()
    fronteira.inserir(inicio, 0)

    veio_de = {inicio: None}
    custo_ate_aqui = {inicio: 0}

    while not fronteira.vazia():
        atual = fronteira.remover()

        if atual == destino:
            break

        for vizinho, custo_aresta in grafo.get(atual, []):
            novo_custo = custo_ate_aqui[atual] + custo_aresta

            if vizinho not in custo_ate_aqui or novo_custo < custo_ate_aqui[vizinho]:
                custo_ate_aqui[vizinho] = novo_custo
                # f(n) = g(n) + h(n)
                prioridade = novo_custo + heuristicas.get(vizinho, 0)
                fronteira.inserir(vizinho, prioridade)
                veio_de[vizinho] = atual

    return veio_de, custo_ate_aqui


def reconstruir_caminho(veio_de, inicio, destino):
    if destino not in veio_de:
        return []  # destino nunca foi alcançado, não existe caminho

    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = veio_de[atual]

    caminho.reverse()
    return caminho
import os

from astar import a_star_search, reconstruir_caminho
from saida import salvar_resultado, gerar_graphviz

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_GRAFO = os.path.join(BASE_DIR, "dados", "grafo.txt")
CAMINHO_RESULTADO = os.path.join(BASE_DIR, "dados", "resultado.txt")
CAMINHO_DOT = os.path.join(BASE_DIR, "dados", "grafo.dot")

INICIO = "A"
DESTINO = "E"


def ler_grafo(caminho):
    nos = []
    grafo = {}
    heuristicas = {}

    with open(caminho, "r", encoding="utf-8") as f:
        linhas = [linha.strip() for linha in f]

    for linha in linhas:
        if not linha or linha.startswith("#"):
            continue

        partes = linha.split()

        if len(partes) > 2 and all(p.isalpha() for p in partes):
            nos = partes
            for no in nos:
                grafo.setdefault(no, [])

        elif len(partes) == 3:
            origem, destino, custo = partes[0], partes[1], float(partes[2])
            grafo.setdefault(origem, []).append((destino, custo))
            grafo.setdefault(destino, []).append((origem, custo))  # bidirecional

        elif len(partes) == 2:
            no, valor = partes[0], float(partes[1])
            heuristicas[no] = valor

    return nos, grafo, heuristicas


def main():
    nos, grafo, heuristicas = ler_grafo(CAMINHO_GRAFO)

    print("Nós encontrados:", nos)
    print("\nLista de adjacência:")
    for no, vizinhos in grafo.items():
        print(f"  {no}: {vizinhos}")
    print("\nHeurísticas:")
    for no, valor in heuristicas.items():
        print(f"  {no}: {valor}")

    veio_de, custo_ate_aqui = a_star_search(grafo, heuristicas, INICIO, DESTINO)
    caminho = reconstruir_caminho(veio_de, INICIO, DESTINO)

    print(f"\nBusca A* de {INICIO} até {DESTINO}:")
    if caminho:
        print("  Caminho encontrado:", " -> ".join(caminho))
        print("  Custo total:", custo_ate_aqui[DESTINO])
    else:
        print("  Nenhum caminho encontrado entre os nós informados.")

    custo_total = custo_ate_aqui.get(DESTINO)
    salvar_resultado(CAMINHO_RESULTADO, caminho, custo_total, INICIO, DESTINO)
    gerar_graphviz(CAMINHO_DOT, grafo, caminho)

    print(f"\nResultado salvo em: {CAMINHO_RESULTADO}")
    print(f"Código Graphviz salvo em: {CAMINHO_DOT}")


if __name__ == "__main__":
    main()
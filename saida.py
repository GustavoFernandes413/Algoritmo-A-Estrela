def salvar_resultado(caminho_saida, caminho, custo_total, inicio, destino):

    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write(f"Busca A* de {inicio} até {destino}\n")
        f.write("=" * 40 + "\n\n")

        if caminho:
            f.write("Caminho encontrado:\n")
            f.write(" -> ".join(caminho) + "\n\n")
            f.write(f"Custo total: {custo_total}\n")
        else:
            f.write("Nenhum caminho encontrado entre os nós informados.\n")


def gerar_graphviz(caminho_dot, grafo, caminho):
    arestas_caminho = set()
    for i in range(len(caminho) - 1):
        arestas_caminho.add(frozenset((caminho[i], caminho[i + 1])))

    linhas = ["graph G {", '    rankdir=LR;', '    node [shape=circle];']
    ja_desenhadas = set()

    for origem, vizinhos in grafo.items():
        for destino_no, custo in vizinhos:
            par = frozenset((origem, destino_no))
            if par in ja_desenhadas:
                continue
            ja_desenhadas.add(par)

            no_caminho = par in arestas_caminho
            cor = 'color="red", penwidth=2.5' if no_caminho else 'color="black"'

            linhas.append(
                f'    "{origem}" -- "{destino_no}" [label="{custo}", {cor}];'
            )

    linhas.append("}")

    with open(caminho_dot, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas) + "\n")
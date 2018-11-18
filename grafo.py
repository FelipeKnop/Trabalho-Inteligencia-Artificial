class Cidade:

    def __init__(self, _id) -> None:
        self.id = _id
        self.vizinhos = list()

    def __repr__(self) -> str:
        return f'Cidade({self.id})'


class Grafo:

    def __init__(self, cidades, distancias, heuristicas) -> None:
        self.cidades = cidades
        self.distancias = distancias
        self.heuristicas = heuristicas

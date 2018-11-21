class Cidade:

    def __init__(self, _id) -> None:
        self.id = _id
        self.vizinhos = list()

    def __repr__(self) -> str:
        return f'Cidade({self.id})'


class No:

    def __init__(self, cidade) -> None:
        self.cidade = cidade
        self.valor = 0
        self.pai = None
        self.filhos = list()
        self.expandido = False
        self.cont_filho = 0


class Grafo:

    def __init__(self, cidades, distancias, heuristicas) -> None:
        self.cidades = cidades
        self.distancias = distancias
        self.heuristicas = heuristicas
        self.id_inicio = None
        self.id_fim = None

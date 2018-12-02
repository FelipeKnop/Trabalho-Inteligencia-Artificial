from queue import Queue

from algoritmo import Algoritmo
from grafo import No


class BuscaLargura(Algoritmo):

    @property
    def nome(self) -> str:
        return 'Busca em Largura'

    def executa(self) -> None:
        raiz = No(self.grafo.cidades[self.grafo.id_inicio])

        if self.grafo.id_inicio == self.grafo.id_fim:
            self.gera_solucao(raiz)
            return

        no = raiz

        fechados = [False] * len(self.grafo.cidades)

        fila = Queue()

        self.gera_filhos(raiz, fechados)

        for i in range(len(self.grafo.cidades)):
            if len(no.filhos) > i:
                fila.put(no.filhos[i])

        while not fila.empty():
            aux = fila.get()
            aux.pai.cont_filho += 1
            if aux.cidade.id == self.grafo.id_fim:
                self.gera_solucao(aux)
                return

            if not aux.expandido:
                self.gera_filhos(aux, fechados)

            for j in range(len(self.grafo.cidades)):
                if len(aux.filhos) > j:
                    fila.put(aux.filhos[j])

        self.gera_solucao()
        return

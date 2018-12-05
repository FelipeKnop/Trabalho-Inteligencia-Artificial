from queue import LifoQueue

from algoritmo import Algoritmo
from grafo import No


class BuscaProfundidade(Algoritmo):

    @property
    def nome(self) -> str:
        return 'Busca em Profundidade'

    def executa(self) -> None:
        raiz = No(self.grafo.cidades[self.grafo.id_inicio])

        if self.grafo.id_inicio == self.grafo.id_fim:
            self.gera_solucao(raiz)
            return

        no = raiz

        fechados = [False] * len(self.grafo.cidades)

        pilha = LifoQueue()

        self.gera_filhos(raiz, fechados)

        for i in reversed(range(len(self.grafo.cidades))):
            if len(no.filhos) > i:
                pilha.put(no.filhos[i])

        while not pilha.empty():
            aux = pilha.get()
            aux.pai.cont_filho += 1
            if aux.cidade.id == self.grafo.id_fim:
                self.gera_solucao(aux)
                return

            if not aux.expandido:
                self.gera_filhos(aux, fechados)

            for j in reversed(range(len(self.grafo.cidades))):
                if len(aux.filhos) > j:
                    pilha.put(aux.filhos[j])

        self.gera_solucao()
        return

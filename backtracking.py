from algoritmo import Algoritmo
from grafo import No


class Backtracking(Algoritmo):

    @property
    def nome(self) -> str:
        return 'Backtracking'

    def executa(self) -> None:
        raiz = No(self.grafo.cidades[self.grafo.id_inicio])

        if self.grafo.id_inicio == self.grafo.id_fim:
            self.gera_solucao(raiz)
            return

        no = raiz

        while True:
            if len(no.cidade.vizinhos) > no.cont_filho:
                if self.confere_ancestral(no, no.cidade.vizinhos[no.cont_filho].id):
                    no.cont_filho += 1
                else:
                    filho = self.gera_filho(no)
                    if filho.cidade.id == self.grafo.id_fim:
                        self.gera_solucao(filho)
                        return
                    no = filho
            elif no == raiz:
                self.gera_solucao()
                return
            else:
                self.num_nos_visitados += 1
                self.num_nos_expandidos -= 1
                temp = no.pai
                temp.filhos.remove(no)
                no = temp

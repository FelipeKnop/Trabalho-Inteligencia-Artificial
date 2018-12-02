from algoritmo import Algoritmo
from grafo import No


class BuscaIDAEstrela(Algoritmo):

    @property
    def nome(self) -> str:
        return 'Busca IDA*'

    def executa(self) -> None:
        raiz = No(self.grafo.cidades[self.grafo.id_inicio])

        if self.grafo.id_inicio == self.grafo.id_fim:
            self.gera_solucao(raiz)
            return

        no = raiz

        fechados = [False] * len(self.grafo.cidades)
        descartados = [None] * len(self.grafo.cidades)
        patamar = self.grafo.heuristicas[self.grafo.id_inicio][self.grafo.id_fim]

        descarte = 0

        while True:
            if len(no.cidade.vizinhos) > no.cont_filho:
                if self.confere_ancestral(no, no.cidade.vizinhos[no.cont_filho].id):
                    no.cont_filho += 1
                else:
                    filho = self.gera_filho(no)
                    if filho.valor + self.grafo.heuristicas[filho.cidade.id][self.grafo.id_fim] > patamar + 0.00001:
                        descartados[descarte] = filho
                        descarte += 1
                    elif filho.cidade.id == self.grafo.id_fim:
                        self.gera_solucao(filho)
                        return
                    else:
                        no = filho
            elif no == raiz:
                if descarte == 0:
                    self.gera_solucao()
                    return

                menor = descartados[0]

                for i in range(1, descarte):
                    if self.grafo.heuristicas[descartados[i].cidade.id][self.grafo.id_fim] + descartados[i].valor < \
                            self.grafo.heuristicas[menor.cidade.id][self.grafo.id_fim] + menor.valor:
                        menor = descartados[i]

                if self.grafo.heuristicas[menor.cidade.id][self.grafo.id_fim] + menor.valor == patamar:
                    self.gera_solucao()
                    return

                fechados = [False] * len(self.grafo.cidades)
                patamar = self.grafo.heuristicas[menor.cidade.id][self.grafo.id_fim] + menor.valor
                descarte = 0
                raiz.cont_filho = 0
            else:
                fechados[no.cidade.id] = True
                temp = no.pai
                temp.filhos.remove(no)
                no = temp

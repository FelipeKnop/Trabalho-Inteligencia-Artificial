from algoritmo import Algoritmo
from grafo import No


class BuscaOrdenada(Algoritmo):

    @property
    def nome(self) -> str:
        return 'Busca Ordenada'

    def executa(self) -> None:
        raiz = No(self.grafo.cidades[self.grafo.id_inicio])

        if self.grafo.id_inicio == self.grafo.id_fim:
            self.gera_solucao(raiz)
            return

        no = raiz

        fechados = [False] * len(self.grafo.cidades)

        abertos = list()

        self.gera_filhos(raiz, fechados)

        abertos += [
            no.filhos[i]
            for i in range(len(self.grafo.cidades))
            if len(no.filhos) > i
        ]

        tamanho = len(abertos)

        while True:
            if len(abertos) == 0:
                self.gera_solucao()
                return

            menor = abertos[0]

            for i in range(1, tamanho):
                if abertos[i].valor < menor.valor:
                    menor = abertos[i]

            if menor.cidade.id == self.grafo.id_fim:
                self.gera_solucao(menor, len(abertos), fechados.count(True))
                return
            else:
                no = menor
                if not no.expandido:
                    self.gera_filhos(no, fechados)

                abertos.remove(menor)

                abertos += [
                    no.filhos[i]
                    for i in range(len(self.grafo.cidades))
                    if len(no.filhos) > i
                ]

                if len(abertos) == tamanho:
                    fechados[no.cidade.id] = True
                else:
                    tamanho = len(abertos)

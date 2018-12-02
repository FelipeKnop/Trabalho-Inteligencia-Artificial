from abc import ABC, abstractmethod

from grafo import Grafo, No


class Algoritmo(ABC):

    def __init__(self, grafo: Grafo) -> None:
        self.grafo = grafo
        self.caminho = list()
        self.profundidade = 0
        self.custo_solucao = 0

        self.num_nos_expandidos = 1
        self.num_nos_visitados = 0

        self.fator_ramificacao = 0

    @property
    @abstractmethod
    def nome(self) -> str:
        """
        Define o nome formal do algoritmo (ex: Busca em Largura, Backtracking, Busca A*, etc...)
        :return: nome formal do algoritmo
        """

    @abstractmethod
    def executa(self) -> None:
        """
        Método abstrato com a implementação do algoritmo.
        """

    def gera_solucao(self, no=None):
        if no is None:
            self.caminho = None
            return

        while no.pai is not None:
            self.custo_solucao += self.grafo.distancias[no.pai.cidade.id][no.cidade.id]
            self.caminho.insert(0, str(no.cidade.id))
            self.profundidade += 1
            no = no.pai

        if no.pai is None:
            self.caminho.insert(0, str(no.cidade.id))

    def confere_ancestral(self, no, id):
        while no.pai is not None:
            if no.pai.cidade.id == id:
                return True
            no = no.pai

        return False

    def gera_filho(self, no):
        self.num_nos_expandidos += 1
        no.expandido = True

        filho = No(no.cidade.vizinhos[no.cont_filho])
        filho.pai = no
        filho.valor = no.valor + self.grafo.distancias[no.cidade.id][filho.cidade.id]
        no.filhos.append(filho)
        no.cont_filho += 1

        return filho

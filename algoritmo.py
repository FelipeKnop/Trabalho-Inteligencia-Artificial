from abc import ABC, abstractmethod

from grafo import Grafo


class Algoritmo(ABC):

    def __init__(self, grafo: Grafo) -> None:
        self.grafo = grafo
        self.caminho = list()
        self.profundidade = -1
        self.custo_solucao = -1

        self.num_nos_expandidos = 0
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

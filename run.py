import sys
from argparse import ArgumentParser
from time import time

import numpy as np

from a_estrela import BuscaAEstrela
from backtracking import Backtracking
from grafo import Grafo, Cidade
from gulosa import BuscaGulosa
from ida_estrela import BuscaIDAEstrela
from largura import BuscaLargura
from ordenada import BuscaOrdenada
from profundidade import BuscaProfundidade

ALGORITMOS = {
    'backtracking': Backtracking,
    'largura': BuscaLargura,
    'profundidade': BuscaProfundidade,
    'ordenada': BuscaOrdenada,
    'gulosa': BuscaGulosa,
    'a': BuscaAEstrela,
    'ida': BuscaIDAEstrela
}


def cria_grafo(inicio: int, fim: int) -> Grafo:
    """
    Lê os dados do grafo do arquivo .txt e retorna a instância do Grafo.

    :param inicio: id do nó inicial do grafo
    :param fim: id do nó objetivo do grafo
    :return: instância da classe Grafo
    """

    # Lê o arquivo com as informações do grafo
    with open('dist8.txt', 'r') as f:
        linhas = f.readlines()

    # Primeira linha do arquivo indica a quantidade de cidades
    quantidade = int(linhas[0])

    # Cria a lista de cidades
    cidades = [Cidade(i) for i in range(quantidade)]

    # Obtém as matriz de distância entre as cidades
    distancias = np.array(
        [
            linhas[i].strip('\n').split(' ')  # strip remove o \n no final da linha e split separa os número por espaços
            for i in range(1, quantidade + 1)
        ]
    ).astype(float)  # Transforma os números de string pra int

    # Preenche a lista de vizinhos de cada cidade a partir da matriz de distâncias
    for i in range(quantidade):
        for j in range(quantidade):
            if distancias[i, j] > 0:
                cidades[i].vizinhos.append(cidades[j])

    # Obtém as matriz de heurísticas
    heuristicas = np.array(
        [
            linhas[i].strip('\n').split(' ')  # strip remove o \n no final da linha e split separa os número por espaços
            for i in range(quantidade + 2, len(linhas))
        ]
    ).astype(float)  # Transforma os números de string pra int

    # Cria instância da classe Grafo com as informações lidas do arquivo
    grafo = Grafo(cidades, distancias, heuristicas)

    if inicio < 0 or inicio >= quantidade:
        print('Valor inválido para o id do nó inicial.', file=sys.stderr)
        exit(0)

    if fim < 0 or fim >= quantidade:
        print('Valor inválido para o id do nó final.', file=sys.stderr)
        exit(0)

    grafo.id_inicio = inicio
    grafo.id_fim = fim

    return grafo


def executa(inicio: int, fim: int, algoritmos: list) -> None:
    """
    Executa os algoritmos selecionados para solução do problema.

    :param inicio: id do nó inicial do grafo
    :param fim: id do nó objetivo do grafo
    :param algoritmos: lista de algoritmos
    """

    grafo = cria_grafo(inicio, fim)

    for alg in algoritmos:
        # Obtém e instancia a classe apropriada para o algoritmo selecionado
        classe_algoritmo = ALGORITMOS[alg]
        algoritmo = classe_algoritmo(grafo)

        print('\n\n--------------------------------------------\n')
        print(f'Iniciando execução do algoritmo de {algoritmo.nome}\n')

        start_time = time()  # Inicia o contador de tempo
        algoritmo.executa()
        end_time = time()  # Finaliza o contador de tempo

        print(f'Algoritmo de {algoritmo.nome} concluído.\n')

        if algoritmo.caminho is None:
            print('\nSolução não encontrada\n')
        else:
            print('\nSolução:\n')
            print(f'Caminho: {" -> ".join(algoritmo.caminho)}\n')
            print(f'Profundidade: {algoritmo.profundidade}\n')
            print(f'Custo: {algoritmo.custo_solucao}\n')

            print(f'\nNúmero total de nós expandidos: {algoritmo.num_nos_expandidos}\n')
            print(f'Número total de nós visitados: {algoritmo.num_nos_visitados}\n')

            print(f'\nValor médio do fator de ramificação: {algoritmo.fator_ramificacao}\n')

        print(f'\nTempo total de execução: {end_time - start_time:.2f} segundos.\n')
        print('--------------------------------------------')


def main() -> None:
    # Obtém os parâmetros da linha de comando
    parser = make_parser()
    args = parser.parse_args()

    try:
        # Obtém nós de início e fim do grafo
        inicio = int(args.inicial)
        fim = int(args.final)
    except ValueError:
        print('Valores de id para os nós inicial e final devem ser números inteiros.')
        return

    # Obtém lista de algoritmos selecionados
    algoritmos = args.algoritmos

    if not algoritmos:
        # Se lista vazia, seleciona todos os algoritmos disponíveis
        algoritmos = list(ALGORITMOS.keys())  # Converte de dict_keys para list
    else:
        # Se não estiver vazia, verifica se todos os algoritmos escolhidos são válidos
        for alg in algoritmos:
            try:
                _ = ALGORITMOS[alg]
            except KeyError:
                print(f'Algoritmo "{alg}" não reconhecido. As opcões válidas são: ' +
                      ', '.join([f'"{alg}"' for alg in ALGORITMOS.keys()]))
                return

    print(f'Algoritmos escolhidos: {algoritmos}')

    executa(inicio, fim, algoritmos)


def make_parser() -> ArgumentParser:
    """
    Cria a instância de ArgumentParser para obter os argumentos de linha de comando.

    :return: instância de ArgumentParser com as regras definidas
    """

    parser = ArgumentParser(
        description='Trabalho prático da disciplina DCC014 - Inteligência Artificial, implementado pelos alunos Davi '
                    'de Almeida Cardoso e Felipe Barra Knop, para resolução do problema 5 - Mapa (Grafo de Cidades).'
    )

    parser.add_argument(
        'inicial',
        action='store',
        help='id do nó inicial do grafo. Deve ser um número inteiro entre 0 e a quantidade de nós no grafo.'
    )

    parser.add_argument(
        'final',
        action='store',
        help='id do nó objetivo do grafo. Deve ser um número inteiro entre 0 e a quantidade de nós no grafo.'
    )

    parser.add_argument(
        'algoritmos',
        nargs='*',
        help='algoritmos a serem utilizados para a resolução do problema. As opções válidas são:\n' +
             ', '.join([f'"{alg}"' for alg in ALGORITMOS.keys()]) +
             '.\n\nCaso nenhuma opção seja escolhida, serão usados todos os algoritmos.'
    )

    return parser


if __name__ == '__main__':
    main()

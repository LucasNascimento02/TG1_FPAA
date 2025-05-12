import numpy as np
from typing import List, Tuple, Optional
from dataclasses import dataclass
from heapq import heappush, heappop

@dataclass
class No:
    posicao: Tuple[int, int]
    custo_g: float 
    custo_h: float 
    pai: Optional['No'] = None

    @property
    def custo_f(self) -> float:
        return self.custo_g + self.custo_h

    def __lt__(self, outro: 'No') -> bool:
        return self.custo_f < outro.custo_f

class BuscadorCaminho:
    def __init__(self, labirinto: List[List[str]]):
        """
        Inicializa o buscador de caminho com um labirinto.
        
        Args:
            labirinto: Matriz 2D representando o labirinto
                      'S': Posição inicial
                      'E': Posição final
                      '0': Células livres
                      '1': Obstáculos
        """
        self.labirinto = np.array(labirinto)
        self.linhas, self.colunas = self.labirinto.shape
        self.pos_inicial = self._encontrar_posicao('S')
        self.pos_final = self._encontrar_posicao('E')
        
        if not self.pos_inicial or not self.pos_final:
            raise ValueError("O labirinto deve conter tanto 'S' (início) quanto 'E' (fim)")

    def _encontrar_posicao(self, alvo: str) -> Optional[Tuple[int, int]]:
        """Encontra a posição de um elemento específico no labirinto."""
        posicoes = np.where(self.labirinto == alvo)
        if len(posicoes[0]) > 0:
            return (posicoes[0][0], posicoes[1][0])
        return None

    def _posicao_valida(self, pos: Tuple[int, int]) -> bool:
        """Verifica se uma posição é válida no labirinto."""
        linha, coluna = pos
        return (0 <= linha < self.linhas and 
                0 <= coluna < self.colunas and 
                self.labirinto[linha][coluna] != '1')

    def _obter_vizinhos(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Retorna as posições vizinhas válidas."""
        linha, coluna = pos
        direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        vizinhos = []
        
        for dl, dc in direcoes:
            nova_pos = (linha + dl, coluna + dc)
            if self._posicao_valida(nova_pos):
                vizinhos.append(nova_pos)
        
        return vizinhos

    def _distancia_manhattan(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> float:
        """Calcula a distância de Manhattan entre duas posições."""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def encontrar_caminho(self) -> Optional[List[Tuple[int, int]]]:
        """
        Encontra o caminho mais curto usando o algoritmo A*.
        
        Returns:
            Lista de coordenadas representando o caminho encontrado, ou None se não houver caminho.
        """
        if not self.pos_inicial or not self.pos_final:
            return None

        conjunto_aberto = []
        conjunto_fechado = set()
        
        no_inicial = No(
            posicao=self.pos_inicial,
            custo_g=0,
            custo_h=self._distancia_manhattan(self.pos_inicial, self.pos_final)
        )
        
        heappush(conjunto_aberto, no_inicial)
        
        dicionario_nos = {self.pos_inicial: no_inicial}
        
        while conjunto_aberto:
            atual = heappop(conjunto_aberto)
            
            if atual.posicao == self.pos_final:
                caminho = []
                while atual:
                    caminho.append(atual.posicao)
                    atual = atual.pai
                return caminho[::-1]
            
            conjunto_fechado.add(atual.posicao)
            
            for pos_vizinho in self._obter_vizinhos(atual.posicao):
                if pos_vizinho in conjunto_fechado:
                    continue
                
                custo_g = atual.custo_g + 1
                
                if pos_vizinho not in dicionario_nos or custo_g < dicionario_nos[pos_vizinho].custo_g:
                    no_vizinho = No(
                        posicao=pos_vizinho,
                        custo_g=custo_g,
                        custo_h=self._distancia_manhattan(pos_vizinho, self.pos_final),
                        pai=atual
                    )
                    dicionario_nos[pos_vizinho] = no_vizinho
                    heappush(conjunto_aberto, no_vizinho)
        
        return None

    def obter_labirinto_com_caminho(self, caminho: List[Tuple[int, int]]) -> List[List[str]]:
        """
        Retorna o labirinto com o caminho marcado.
        
        Args:
            caminho: Lista de coordenadas do caminho encontrado
            
        Returns:
            Labirinto com o caminho marcado com '*'
        """
        labirinto_copia = self.labirinto.copy()
        for pos in caminho[1:-1]:
            linha, coluna = pos
            labirinto_copia[linha][coluna] = '*'
        return labirinto_copia.tolist() 
import pytest
from src.pathfinder import BuscadorCaminho

def test_labirinto_valido():
    """Testa um labirinto válido com solução."""
    labirinto = [
        ['S', '0', '1', '0', '0'],
        ['0', '0', '1', '0', '1'],
        ['0', '1', '0', '0', '0'],
        ['1', '0', '0', 'E', '1']
    ]
    
    buscador = BuscadorCaminho(labirinto)
    caminho = buscador.encontrar_caminho()
    
    assert caminho is not None
    assert caminho[0] == (0, 0)
    assert caminho[-1] == (3, 3)
    
    for i in range(len(caminho) - 1):
        atual = caminho[i]
        proximo = caminho[i + 1]
        assert abs(atual[0] - proximo[0]) + abs(atual[1] - proximo[1]) == 1

def test_sem_solucao():
    """Testa um labirinto sem solução possível."""
    labirinto = [
        ['S', '1', '0', '0', '0'],
        ['1', '1', '1', '0', '1'],
        ['0', '1', '0', '0', '0'],
        ['1', '0', '0', 'E', '1']
    ]
    
    buscador = BuscadorCaminho(labirinto)
    caminho = buscador.encontrar_caminho()
    
    assert caminho is None

def test_sem_inicio_fim():
    """Testa um labirinto sem posições inicial ou final."""
    labirinto = [
        ['0', '0', '1', '0', '0'],
        ['0', '0', '1', '0', '1'],
        ['0', '1', '0', '0', '0'],
        ['1', '0', '0', '0', '1']
    ]
    
    with pytest.raises(ValueError):
        BuscadorCaminho(labirinto)

def test_visualizacao_caminho():
    """Testa a visualização do caminho no labirinto."""
    labirinto = [
        ['S', '0', '1', '0', '0'],
        ['0', '0', '1', '0', '1'],
        ['0', '1', '0', '0', '0'],
        ['1', '0', '0', 'E', '1']
    ]
    
    buscador = BuscadorCaminho(labirinto)
    caminho = buscador.encontrar_caminho()
    labirinto_com_caminho = buscador.obter_labirinto_com_caminho(caminho)
    
    assert labirinto_com_caminho[0][0] == 'S'
    assert labirinto_com_caminho[3][3] == 'E'
    
    posicoes_caminho = set(caminho[1:-1])
    for linha in range(len(labirinto_com_caminho)):
        for coluna in range(len(labirinto_com_caminho[0])):
            if (linha, coluna) in posicoes_caminho:
                assert labirinto_com_caminho[linha][coluna] == '*' 
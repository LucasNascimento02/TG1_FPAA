# Integrantes

- Lucas Ribeiro do Nascimento

# BuscadorCaminho - Implementação do Algoritmo A*

Este projeto implementa o algoritmo A* para encontrar o caminho mais curto em um labirinto 2D. A implementação foi projetada para ajudar um robô de resgate a navegar através de obstáculos para atingir seu destino de forma eficiente.

## Estrutura do Projeto

```
.
├── src/
│   ├── pathfinder.py    # Implementação principal do algoritmo A*
│   └── exemplo.py       # Script de exemplo
├── tests/
│   └── test_pathfinder.py  # Casos de teste
├── requirements.txt     # Dependências do projeto
└── README.md           # Este arquivo
```

## Requisitos

- Python 3.7+
- numpy
- pytest (para executar os testes)

## Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd buscador-caminho
```


## Uso

Execute o script de exemplo:
```bash
python src/exemplo.py
```

Execute os testes:
```bash
pytest tests/
```

## Como Funciona

### Representação do Labirinto

O labirinto é representado como uma matriz 2D onde:
- `S`: Posição inicial
- `E`: Posição final
- `0`: Células livres (onde o robô pode se mover)
- `1`: Obstáculos
- `*`: Caminho percorrido (mostrado na saída)

### Algoritmo A*

O algoritmo A* combina:
1. **g(n)**: O custo real do nó inicial até o nó atual
2. **h(n)**: O custo estimado do nó atual até o nó final (distância de Manhattan)

O algoritmo usa uma fila de prioridade para sempre explorar o caminho mais promissor primeiro, baseado no valor f(n) = g(n) + h(n).

### Funcionalidades

- Busca de caminho eficiente usando o algoritmo A*
- Heurística de distância de Manhattan
- Visualização do caminho
- Suíte de testes abrangente
- Tratamento de erros para labirintos inválidos

## Exemplo

Labirinto de entrada:
```
S 0 1 0 0
0 0 1 0 1
0 1 0 0 0
1 0 0 E 1
```

Caminho de saída:
```
S * 1 0 0
* * 1 0 1
0 1 * 0 0
1 * * E 1
```

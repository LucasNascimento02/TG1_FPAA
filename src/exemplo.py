from pathfinder import BuscadorCaminho

def imprimir_labirinto(labirinto):
    """Imprime o labirinto formatado."""
    for linha in labirinto:
        print(' '.join(linha))

def main():
    # Exemplo de labirinto do projeto
    labirinto = [
        ['S', '0', '1', '0', '0'],
        ['0', '0', '1', '0', '1'],
        ['0', '1', '0', '0', '0'],
        ['1', '0', '0', 'E', '1']
    ]
    
    print("Labirinto Original:")
    imprimir_labirinto(labirinto)
    print("\nBuscando caminho...")
    
    buscador = BuscadorCaminho(labirinto)
    caminho = buscador.encontrar_caminho()
    
    if caminho:
        print("\nCaminho encontrado!")
        print("Coordenadas:", caminho)
        
        print("\nLabirinto com caminho:")
        labirinto_com_caminho = buscador.obter_labirinto_com_caminho(caminho)
        imprimir_labirinto(labirinto_com_caminho)
    else:
        print("\nNenhum caminho encontrado!")

if __name__ == "__main__":
    main() 
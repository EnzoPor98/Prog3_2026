from ejercicio2.pokemon import Pokemon
from ejercicio2.pokedex import Pokedex

def main():
    pokedex = Pokedex()
    pokedex.cargar_csv("C:/Users/x/Desktop/Estudios/Enzo/2.2. Programación III/Trabajo Grupal N°1/Prog3_2026/ejercicio2/pokemon.csv")
    
    pikachu = pokedex._pokemones[24]
    por_tipos = pokedex.agrupar_por_tipo()
    por_generaciones = pokedex.agrupar_por_generacion()
    
    print(f"Total de pokemones cargados: {len(pokedex)}\n")
    
    print(f"¿Pikachu está en la pokedex? {pikachu in pokedex}\n")
    
    print(f"Pokemones de tipo 'Electric': {[p.name for p in pokedex.filtrar_por_tipo('Electric')]}\n")
    
    print(f"Pokemones de la generación 1: {[p.name for p in pokedex.filtrar_por_generacion(1)]}\n")
    
    print(f"Buscar por nombre 'Bulbasaur': {pokedex.buscar_por_nombre('Bulbasaur')}\n")
    
    print(f"Pokemones de tipo 'Fire' y generación 1: {[p.name for p in pokedex.filtrar(tipo='Fire', generacion=1)]}\n")
    
    print(f"Pokemones agrupados por tipo: {[p.name for p in por_tipos['Fire']]}\n")
    
    print(f"Pokemones agrupados por generación: {[p.name for p in por_generaciones[1]]}\n")
    
    print(f"Pokemones con mas de 200 de hp: {[p.name for p in pokedex.top_n(200, 'hp')]}\n")
    
    print(f"Tipos mas comunes: {pokedex.tipos_mas_comunes()}")

if __name__ == '__main__':
    main()
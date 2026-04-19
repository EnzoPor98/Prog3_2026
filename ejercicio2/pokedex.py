import csv
from pokemon import Pokemon
from stats import Stats

class Pokedex:
    
    def __init__(self):
        self.pokemones : list = []


    def __len__(self) -> int:
        return len(self.pokemones)

    def __contains__(self, pokemon) -> bool:
        return pokemon in self.pokemones
    
    def cargar_csv(self, file_path: str) -> None:
        try:
            with open(file_path, mode='r', encoding='utf-8') as f:
                lector = csv.DictReader(f)
                for fila in lector:
                    
                    nuevo_pokemon = Pokemon(
                        id=int(fila['id']), 
                        name=fila['name'],
                        form=fila['form'],
                        type1=fila['type1'],
                        type2=fila['type2'],
                        stats=None, # De momento None, o procesa tus stats aquí
                        generation=int(fila['generation'])
                    )
                    
                    
                    self.pokemones.append(nuevo_pokemon)
                    
            print(f"Carga finalizada: {len(self.pokemones)} pokemones en memoria.")
            
        except FileNotFoundError:
            print("Error: No se encontró el archivo pokemon.csv")

    def filtrar_por_tipo(self, tipo: str) -> list:
        return [p for p in self.pokemones if p.type1 == tipo or p.type2 == tipo]
    

    def filtrar_por_generacion(self, gen: int) -> list:
        return [p for p in self.pokemones if p.generation == gen]
    

    def buscar_por_nombre(self, nombre: str):
        for p in self.pokemones:
            if p.name.lower() == nombre.lower():
                return p
        return None
    
    def filtrar(self, tipo=None, generacion=None, legendario=None, hp_min=0, ataque_min=0) -> list:
      
        if tipo:
            resultados = [p for p in resultados if p.type1 == tipo or p.type2 == tipo]
            
        if generacion:
            resultados = [p for p in resultados if p.generation == generacion]
            
        if hp_min > 0:
            resultados = [p for p in resultados if p.stats.hp >= hp_min]
       
        if ataque_min > 0:
            resultados = [p for p in resultados if p.stats.attack >= ataque_min]
            
        return resultados



    def agrupar_por_tipo(self) -> dict:
        grupos = {}
    
        for p in self.pokemones:
            tipos_del_p = [p.type1]
            if p.type2: 
                tipos_del_p.append(p.type2)
                
            for t in tipos_del_p:
                if t not in grupos:
                    grupos[t] = []
                
                grupos[t].append(p)
                
        return grupos
    

    def agrupar_por_generacion(self) -> dict:
        grupos = {}
        
        for p in self.pokemones:
            
            gen = p.generation
            
            if gen not in grupos:
                grupos[gen] = []
                
            grupos[gen].append(p)
            
        return grupos
    

    def top_n(self, n: int, stat: str) -> list:
    
        pokemones_ordenados = sorted(
            self.pokemones, 
            key=lambda p: getattr(p.stats, stat), 
            reverse=True
        )
        
        return pokemones_ordenados[:n]
    

    def tipos_mas_comunes(self, n: int) -> list:
        conteo = {}
        
        for p in self.pokemones:
            tipos_p = [p.type1]
            if p.type2: 
                tipos_p.append(p.type2)
                
            for t in tipos_p:
                conteo[t] = conteo.get(t, 0) + 1
                
        
        resultado = sorted(conteo.items(), key=lambda x: x[1], reverse=True)
        
        return resultado[:n]
        
    
            
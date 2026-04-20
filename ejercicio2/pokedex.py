import csv
from ejercicio2.pokemon import Pokemon
from ejercicio2.stats import Stats


class Pokedex:

    def __init__(self):
        self._pokemones: list = []

    def __len__(self) -> int:
        return len(self._pokemones)

    def __contains__(self, pokemon) -> bool:
        return pokemon in self._pokemones

    def cargar_csv(self, file_path: str) -> None:
        try:
            with open(file_path, mode="r", encoding="utf-8") as f:
                lector = csv.DictReader(f)
                for fila in lector:

                    nuevo_pokemon = Pokemon(
                        id=int(fila["id"]),
                        name=fila["name"],
                        form=fila["form"],
                        type1=fila["type1"],
                        type2=fila["type2"],
                        stats=Stats(
                            hp=int(fila["hp"]),
                            attack=int(fila["attack"]),
                            defense=int(fila["defense"]),
                            sp_atk=int(fila["sp_atk"]),
                            sp_def=int(fila["sp_def"]),
                            speed=int(fila["speed"]),
                        ),
                        generation=int(fila["generation"]),
                    )

                    self._pokemones.append(nuevo_pokemon)

            print(f"Carga finalizada: {len(self._pokemones)} pokemones en memoria.")

        except FileNotFoundError:
            print("Error: No se encontró el archivo pokemon.csv")

    def filtrar_por_tipo(self, tipo: str) -> list[Pokemon]:
        return [p for p in self._pokemones if p.type1 == tipo or p.type2 == tipo]

    def filtrar_por_generacion(self, gen: int) -> list[Pokemon]:
        return [p for p in self._pokemones if p.generation == gen]

    def buscar_por_nombre(self, nombre: str) -> Pokemon | None:
        for p in self._pokemones:
            if p.name.lower() == nombre.lower():
                return p
        return None

    def filtrar(
        self,
        tipo: str = None,
        generacion: int = None,
        legendario: bool = None,
        hp_min: int = None,
        ataque_min: int = None,
    ) -> list[Pokemon]:
        resultados = []

        for p in self._pokemones:
            if tipo != None and (tipo != p.type1 and tipo != p.type2):
                continue

            if generacion != None and generacion != p.generation:
                continue

            if hp_min != None and hp_min > p.stats.hp:
                continue

            if ataque_min != None and ataque_min > p.stats.attack:
                continue

            resultados.append(p)

        return resultados

    def agrupar_por_tipo(self) -> dict[str, list[Pokemon]]:
        grupos = {}

        for p in self._pokemones:
            tipos_del_p = [p.type1]
            if p.type2:
                tipos_del_p.append(p.type2)

            for t in tipos_del_p:
                if t not in grupos:
                    grupos[t] = []

                grupos[t].append(p)

        return grupos

    def agrupar_por_generacion(self) -> dict[int, list[Pokemon]]:
        grupos = {}

        for p in self._pokemones:

            gen = p.generation

            if gen not in grupos:
                grupos[gen] = []

            grupos[gen].append(p)

        return grupos

    def top_n(self, n: int, stat: str) -> list[Pokemon]:
        return [p for p in self._pokemones if getattr(p.stats, stat, 0) >= n]

    def tipos_mas_comunes(self, n: int = 5) -> list[tuple[str, int]]:
        dicc = {}
        
        for p in self._pokemones:
            if p.type1 not in dicc:
                dicc[p.type1] = 1
            else:
                dicc[p.type1] += 1
                
            if p.type2 == " ":
                continue
                
            if p.type2 not in dicc:
                dicc[p.type2] = 1
            else:
                dicc[p.type2] += 1
        
        lista = []
        for t in dicc:
            lista.append((t, dicc[t]))
            
        return sorted(lista, key=lambda x: x[1], reverse=True)[:n]
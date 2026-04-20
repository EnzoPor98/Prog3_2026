from abc import ABC, abstractmethod
from ejercicio2.pokemon import Pokemon

class PokedexAbstract(ABC):

    def __init__(self) -> None:
        self._pokemon_list : list[Pokemon] = []

    def __len__(self) -> int:
        return len(self._pokemon_list)

    @abstractmethod
    def cargar_csv(self, file_path: str) -> None:
        """Carga en el contenedor los elementos procesados del archivo CSV cuya ruta se especifica en file_path

        Args:
            file_path (str): Ruta del archivo CSV a cargar.
        """
        pass

    @abstractmethod
    def __contains__(self, pokemon: Pokemon) -> bool:
        """Indica si el parámetro pokemon existe en el contenedor.

        Args:
            pokemon (Pokemon): objeto a buscar.

        Returns:
            bool: True si el pokemon existe en el contenedor, False en caso contrario.
        """
        pass

    @abstractmethod
    def filtrar_por_tipo(self, tipo: str) -> list[Pokemon]:
        """Retorna los Pokémon que tengan ese tipo como Type 1 o Type 2.
        Returns:
        
            list[Pokemon]: Lista de Pokémon que coinciden con el tipo.
        """
        pass

    @abstractmethod
    def filtrar_por_generacion(self, gen: int) -> list[Pokemon]:
        """Retorna los Pokémon de una generación específica.
        Returns:
            list[Pokemon]: Lista de Pokémon de la generación indicada.
        """
        pass

    @abstractmethod
    def buscar_por_nombre(self, nombre: str) -> Pokemon | None:
        """Búsqueda parcial, sin distinguir mayúsculas/minúsculas. 
            Retorna el primero que coincida, o None si no hay resultados.

        Args:
            nombre (str): Nombre o parte del nombre del Pokémon a buscar.
        Returns:
            Optional[Pokemon]: El Pokémon encontrado o None.
        """
        pass

    @abstractmethod
    def filtrar(self, tipo=None, generacion=None, legendario=None, hp_min=None, ataque_min=None) -> list[Pokemon]:
        """Un único método que acepta múltiples criterios opcionales y los combina. 
        Deben cumplirse todos al mismo tiempo.
        Si un parámetro es None, ese criterio se ignora.

        Args:
            tipo (str, optional): Tipo de Pokémon a filtrar. Defaults to None.
            generacion (int, optional): Generación a filtrar. Defaults to None.
            legendario (bool, optional): Si True, solo incluye legendarios. Defaults to None.
            hp_min (int, optional): HP mínimo para filtrar. Defaults to None.
            ataque_min (int, optional): Ataque mínimo para filtrar. Defaults to None.
            
        Returns:
            list[Pokemon]: Lista de Pokémon que coinciden con los criterios.
        """
        pass

    @abstractmethod
    def agrupar_por_tipo(self) -> dict[str, list[Pokemon]]:
        """Agrupa los Pokémon por su Type 1 y el valor es la lista de Pokémon de ese tipo.
        Returns:
            dict[str, list[Pokemon]]: Diccionario con el tipo como clave y la lista de Pokémon como valor.
        """
        pass

    @abstractmethod
    def agrupar_por_generacion(self) -> dict[int, list[Pokemon]]:
        """Agrupa los Pokémon por su generación y el valor es la lista de Pokémon de esa generación.
        
        Returns: 
            dict[int, list[Pokemon]]: Diccionario con la generación como clave y la lista de Pokémon como valor.
        """
        
        pass

    @abstractmethod
    def top_n(self, n: int, stat: str) -> list[Pokemon]:
        """Retorna los N Pokémon con mayor valor en la stat indicada (puede ser 'hp', 'attack', 'defense', 'speed', etc.).
        Args:
            n (int): Cantidad de Pokémon a retornar.

        Returns:
            list[Pokemon]: Lista de los N Pokémon con mayor valor en la stat indicada.
        """
        pass

    @abstractmethod
    def tipos_mas_comunes(self, n: int = 5) -> list[tuple[str, int]]:
        """Retorna una lista de tuplas (tipo, cantidad) con los N tipos más frecuentes, ordenados de mayor a menor.
        Args:
            n (int, optional): Cantidad de tipos a retornar. Defaults to 5.
        Returns:
            list[tuple[str, int]]: Lista de tuplas con el tipo y su cantidad de apariciones.
        """
        pass

from stats import Stats
class Pokemon:
    POKEMON_ID = 0
    
    def __init__(self, id : int, name : str, form : str, type1 : str, type2 : str, stats : Stats, generation : int) -> None:
        Pokemon.POKEMON_ID += 1
        self._id = Pokemon.POKEMON_ID
        self.name = name
        self.form = form
        self.type1 = type1
        self.type2 = type2
        self.stats = stats
        self._generation = generation

    def __eq__(self, other) -> bool:
        if isinstance(other, Pokemon) and self.id == other.id:
            return True
        return False

    def __repr__(self) -> str:
        return f"Pokemon(id={self._id}, name='{self.name}', form='{self.form}', type1='{self.type1}', type2='{self.type2}', stats={self.stats}, generation={self._generation})"
    
    def __str__(self) -> str:
        return f"Pokemon(id={self._id}, name='{self.name}', form='{self.form}', type1='{self.type1}', type2='{self.type2}', stats={self.stats}, generation={self._generation})"
    
    # GETTERS
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def generation(self) -> int:
        return self._generation
    
    # SETTERS
    @generation.setter
    def generation(self, generation: int) -> None:
        if not isinstance(generation, int) or generation < 0:
            raise ValueError("Generation debe ser un entero mayor a 0.")
        self._generation = generation
class CalzadoColor:
    def __init__(self, primario: str, secundario: str) -> None:
        self.primario: str
        self.secundario: str | None # NO HACE OPCIONAL AL PARAMETRO.

    def __eq__(self, other: object) -> bool:
        return isinstance(other, CalzadoColor) and self.primario == other.primario and self.secundario == other.secundario
    
    def __str__(self, ) -> str:
        return (f"CalzadoColor(Primario: {self.primario}, Secundario: {self.secundario})")
    
    def __repr__(self):
        return f"CalzadoColor(Primario= {self.primario}, Secundario= {self.secundario})"
    
        

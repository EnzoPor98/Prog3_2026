class CalzadoTalle:
    def __init__(self, descripcion: str, medida_en_cm: float) -> None:
        self.descripcion = descripcion
        self.medida_en_cm = medida_en_cm

    def __eq__(self, other: object) -> bool:
        return isinstance(other, CalzadoTalle) and self.medida_en_cm == other.medida_en_cm
    
    def __str__(self) -> str:
        return f"CalzadoTalle(Descripcion: {self.descripcion}, Medida: {self.medida_en_cm} cm)"
    
    def __repr__(self) -> str:
        return f"CalzadoTalle(Descripcion: {self.descripcion}, Medida: {self.medida_en_cm} cm)"

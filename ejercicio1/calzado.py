from calzado_tipo import CalzadoTipo
from calzado_color import CalzadoColor
from calzado_talle import CalzadoTalle

class Calzado:
    def __init__(self):
        self._sku: int 
        self.nombre : str 
        self.descripcion : str 
        self.tipo : CalzadoTipo 
        self.talle : CalzadoTalle
        self.color: CalzadoColor
        self._cantidad : int  # Cantidad de Existencias de este producto
        self._precio : float
        
    #GETTERS
    @property
    def sku(self) -> int:
        return self._sku
    
    @property
    def cantidad(self) -> int:
        return self._cantidad
    
    @property
    def precio(self) -> float:
        return self._precio
    
    #SETTERS
    @sku.setter
    def sku(self, sku: int) -> None:
        self._sku = sku

    @cantidad.setter
    def cantidad(self, cantidad: int) -> None:
        self._cantidad = cantidad

    @precio.setter
    def precio(self, precio: float) -> None:
        self._precio = precio
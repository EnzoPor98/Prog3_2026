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
        if sku < 0:
            raise ValueError("Sku no puede ser un valor negativo")
        self._sku = sku

    @cantidad.setter
    def cantidad(self, cantidad: int) -> None:
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser un valor negativo")
        self._cantidad = cantidad

    @precio.setter
    def precio(self, precio: float) -> None:
        if precio < 0:
            raise ValueError("El precio no puede ser un valor negativo")
        self._precio = precio
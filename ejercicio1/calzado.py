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
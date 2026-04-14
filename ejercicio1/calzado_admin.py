from calzado_admin_abstract import CalzadoAdminAbstract
from ejercicio1.calzado import Calzado
from ejercicio1.calzado_tipo import CalzadoTipo


class CalzadoAdmin(CalzadoAdminAbstract):
    def __init__(self, lista: list[Calzado] = None):
        super().__init__(lista)

    def agregar(self, calzado: Calzado) -> None:
        if calzado in self._lista:
            raise ValueError("El calzado ya existe en la lista.")

        super().agregar(calzado)
        
    def __repr__(self) -> str:
        return f"CalzadoAdmin(Lista: {self._lista})"
        
    def __str__(self) -> str:
        return f"CalzadoAdmin(Lista: {self._lista})"
        
    def filtrar_por_tipo(self, tipo: CalzadoTipo) -> list[Calzado]:
        pass
    
    def filtrar_precio_entre(self, desde: float = 0, hasta: float = 0) -> list[Calzado]:
        pass
    
    def cantidad_productos(self):
        pass
    
    def cantidad_productos(self) -> int:
        pass
    
    def total_productos(self) -> float:
        pass

    # GETTERS
    @property
    def lista(self) -> list[Calzado]:
        return self._lista

    # SETTERS
    @lista.setter
    def lista(self, lista: list[Calzado]) -> None:
        self._lista = lista

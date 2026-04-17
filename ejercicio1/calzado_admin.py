from typing import Optional

from calzado_admin_abstract import CalzadoAdminAbstract
from ejercicio1.calzado import Calzado
from ejercicio1.calzado_tipo import CalzadoTipo


class CalzadoAdmin(CalzadoAdminAbstract):
    def __init__(self):
        super().__init__()

    def __repr__(self) -> str:
        return f"CalzadoAdmin(Lista: {self._lista})"

    def __str__(self) -> str:
        return f"CalzadoAdmin(Lista: {self._lista})"

    def agregar_calzado(self, calzado: Calzado) -> None:
        if calzado in self._lista:
            raise ValueError("El calzado ya existe en la lista.")

        super().agregar(calzado)

    def eliminar_calzado(self, sku: int) -> None:
        pass

    def modificar_calzado(self, calzado: Calzado) -> None:
        pass

    def buscar_calzado(self, sku: int) -> Optional[Calzado]:
        pass

    def filtrar_por_tipo(self, tipo: CalzadoTipo) -> list[Calzado]:
        pass

    def filtrar_precio_entre(self, desde: float = 0, hasta: float = 0) -> list[Calzado]:
        pass

    def cantidad_productos(self) -> int:
        res = 0
        for calzado in self._lista:
            res += calzado._cantidad
        return res

    def total_productos(self) -> float:
        res = 0
        for calzado in self._lista:
            res += calzado.total()
        return res

    # GETTERS
    @property
    def lista(self) -> list[Calzado]:
        return self._lista

    # SETTERS
    @lista.setter
    def lista(self, lista: list[Calzado]) -> None:
        self._lista = lista

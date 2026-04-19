from typing import Optional
from calzado_admin_abstract import CalzadoAdminAbstract
from calzado import Calzado
from calzado_tipo import CalzadoTipo


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

        self._lista.append(calzado)

    def eliminar_calzado(self, sku: int) -> None:
        for calzado in self._lista:
            if calzado._sku == sku:
                self._lista.remove(calzado)
                break

    def modificar_calzado(self, calzado: Calzado) -> None:
        for i, x in enumerate(self._lista):
            if x._sku == calzado._sku:
                self._lista[i] = calzado
                break            

    def buscar_calzado(self, sku: int) -> Optional[Calzado]:
        for calzado in self._lista:
            if calzado._sku == sku:
                return calzado
        return None

    def filtrar_por_tipo(self, tipo: CalzadoTipo) -> list[Calzado]:
        return [calzado for calzado in self._lista if calzado.tipo == tipo]

    def filtrar_precio_entre(self, desde: float = 0, hasta: float = 0) -> list[Calzado]:
        if desde == 0 or hasta == 0:
            raise ValueError("Los argumentos no pueden valer cero.")

        if desde > hasta:
            raise ValueError("El valor de DESDE no puede ser mayor al valor de HASTA.")

        return [calzado for calzado in self._lista if (calzado._precio >= desde and calzado._precio <= hasta)]

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

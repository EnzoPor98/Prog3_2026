from calzado_tipo import CalzadoTipo
from calzado_color import CalzadoColor
from calzado_talle import CalzadoTalle


class Calzado:
    def __init__(self, sku: int, nombre: str, descripcion: str, tipo: CalzadoTipo, talle: CalzadoTalle, color: CalzadoColor, cantidad: int, precio: float):
        if sku < 0:
            raise ValueError("Sku no puede ser un valor negativo")
        self._sku = sku
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo = tipo
        self.talle = talle
        self.color = color
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser un valor negativo")
        self._cantidad = cantidad
        if precio < 0:
            raise ValueError("El precio no puede ser un valor negativo")
        self._precio = precio

    def total(self) -> float:
        return self._cantidad * self._precio

    def __eq__(self, other) -> bool:
        if not isinstance(other, Calzado):
            return False
        return self._sku == other._sku

    def __str__(self) -> str:
        return f"{self.nombre} - {self.tipo} - Talle: {self.talle} - Color: {self.color}"

    def __repr__(self) -> str:
        return f"Calzado(sku={self._sku}, nombre='{self.nombre}', descripcion='{self.descripcion}', tipo={repr(self.tipo)}, talle={repr(self.talle)}, color={repr(self.color)}, cantidad={self._cantidad}, precio={self._precio})"

    # GETTERS
    @property
    def sku(self) -> int:
        return self._sku

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @property
    def precio(self) -> float:
        return self._precio

    # SETTERS
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
class Stats:
    def __init__(self, hp: int, attack: int, defense: int, sp_atk: int, sp_def: int, speed: int) -> None:
        self._hp = hp
        self._attack = attack
        self._defense = defense
        self._sp_atk = sp_atk
        self._sp_def = sp_def
        self._speed = speed
    
    def total_stats(self) -> int:
        return self._hp + self._attack + self._defense + self._sp_atk + self._sp_def + self._speed

    # GETTERS
    @property
    def hp(self) -> int:
        return self._hp

    @property
    def attack(self) -> int:
        return self._attack

    @property
    def defense(self) -> int:
        return self._defense

    @property
    def sp_atk(self) -> int:
        return self._sp_atk

    @property
    def sp_def(self) -> int:
        return self._sp_def

    @property
    def speed(self) -> int:
        return self._speed

    # SETTERS
    @hp.setter
    def hp(self, hp: int) -> None:
        if not isinstance(hp, int) or hp < 0:
            raise ValueError("HP debe ser un entero mayor a 0.")
        self._hp = hp

    @attack.setter
    def attack(self, attack: int) -> None:
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack debe ser un entero mayor a 0.")
        self._attack = attack

    @defense.setter
    def defense(self, defense: int) -> None:
        if not isinstance(defense, int) or defense < 0:
            raise ValueError("Defense debe ser un entero mayor a 0.")
        self._defense = defense

    @sp_atk.setter
    def sp_atk(self, sp_atk: int) -> None:
        if not isinstance(sp_atk, int) or sp_atk < 0:
            raise ValueError("Sp. Atk debe ser un entero mayor a 0.")
        self._sp_atk = sp_atk

    @sp_def.setter
    def sp_def(self, sp_def: int) -> None:
        if not isinstance(sp_def, int) or sp_def < 0:
            raise ValueError("Sp. Def debe ser un entero mayor a 0.")
        self._sp_def = sp_def

    @speed.setter
    def speed(self, speed: int) -> None:
        if not isinstance(speed, int) or speed < 0:
            raise ValueError("Speed debe ser un entero mayor a 0.")
        self._speed = speed

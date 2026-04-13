from stats import Stats
class Pokemon:
    def __init__(self):
        self.id : int
        self.name : str
        self.form : str
        self.type1 : str
        self.type2 : str
        self.stats : Stats
        self.generation : int
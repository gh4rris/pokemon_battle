class Player():
    def __init__(self, name, party):
        self.name = name
        self.party = party
        self.out = None
        self.battle = None
        self.health_bar = None
        self.turn = False


class Opponent():
    def __init__(self, name, party):
        self.name = name
        self.party = party
        self.out = None
        self.battle = None
        self.health_bar = None
        self.turn = False
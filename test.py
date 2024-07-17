import unittest
from layout import Window, TextActionFrame
from battle import Battle
from trainers import Player, Opponent
from pokemon import Pokemon

class TestBattle(unittest.TestCase):
    def __init__(self):
        self.player = Player("test player", [])
        self.opponent = Opponent("test opponent", [])
        self.window = Window("window", (100, 100), self.player, self.opponent)
        self.text_action_frame = TextActionFrame(self.window)
        self.battle = Battle(self.text_action_frame, self.window, self.player, self.opponent)
        self.move_1 = Pokemon("test player move", 50, 100, 20)
        self.move_2 = Pokemon("test opponent move", 60, 100, 15)
        self.pokemon_1 = Pokemon("test player pokemon", 2.8, 2.5, 62, [self.move_1], self.player)
        self.pokemon_2 = Pokemon("test opponent pokemon", 2.7, 2.6, 63, [self.move_2], self.opponent)
        self.player.party.append(self.pokemon_1)
        self.opponent.party.append(self.pokemon_2)      

    def test_progress_text(self):
        self.battle.next_text = [("This is the first set of text", "S-Next"), ("This is the final set of text", "End")]
        self.battle.progress_text()
        self.assertEqual(len(self.battle_next_text), 2)


if __name__ == "__main__":
    unittest.main()
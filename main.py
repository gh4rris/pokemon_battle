from layout import Window
from pokemon import Pokemon
from trainers import Player, Opponent
from moves import Moves

def main():
    # Trainers
    player = Player("Red", [])
    opponent = Opponent("Blue", [])


    # Moves
    razor_leaf = Moves("Razor Leaf", 55, 95, 25)
    vine_whip = Moves("Vine Whip", 35, 100, 10)
    mega_drain = Moves("Mega Drain", 40, 100, 15)
    solarbeam = Moves("Solarbeam", 120, 100, 10)

    thunder_shock = Moves("Thunder Shock", 40, 100, 30)
    swift = Moves("Swift", 60, 100, 20)
    body_slam = Moves("Body Slam", 85, 100, 15)
    thunder = Moves("Thunder", 120, 70, 10)

    slash = Moves("Slash", 70, 100, 20)
    fire_spin = Moves("Fire Spin", 35, 85, 15)
    rage = Moves("Rage", 20, 100, 20)
    fire_blast = Moves("Fire Blast", 120, 85, 5)

    hydro_pump = Moves("Hydro Pump", 120, 80, 5)
    hyper_beam = Moves("Hyper Beam", 150, 90, 5)
    bite = Moves("Bite", 60, 100, 25)
    tackle = Moves("Tackle", 35, 95, 35)
    

        # Pokemon
    # Player Party
    venasaur = Pokemon("Venasauar", 3.17, 2.12, 65, [razor_leaf, vine_whip, mega_drain, solarbeam], player)
    raichu = Pokemon("Raichu", 2.77, 2.52, 62, [thunder_shock, swift, body_slam, thunder], player)
    player_party = [venasaur, raichu]
    for member in player_party:
        player.party.append(member)

    # Opponent Party
    charizard = Pokemon("Charizard", 3.13, 2.52, 65, [slash, fire_spin, rage, fire_blast], opponent)
    gyarados = Pokemon("Gyarados", 3.47, 2.14, 63, [hydro_pump, hyper_beam, bite, tackle], opponent)
    opponent_party = [charizard, gyarados]
    for member in opponent_party:
        opponent.party.append(member)
    

    main_window = Window("Pokemon Battle", (750, 450), player, opponent)

main()
from layout import Window
from pokemon import Pokemon
from trainers import Trainer, Opponent
from moves import Moves

def main():
    # Moves
    fire_blast = Moves("Fire Blast", 120, 85, 5)
    razor_leaf = Moves("Razor Leaf", 55, 95, 25)
    solarbeam = Moves("Solarbeam", 120, 100, 10)
    mega_drain = Moves("Mega Drain", 40, 100, 15)
    vine_whip = Moves("Vine Whip", 35, 100, 10)


    # Pokemon
    # Trainer Party
    venasaur = Pokemon("Venasaur", 3.17, 65, [razor_leaf, vine_whip, mega_drain, solarbeam])

    # Opponent Party
    charizard = Pokemon("Charizard", 3.13, 65, [fire_blast])


    # Trainers
    trainer = Trainer("Red", [venasaur])
    opponent = Opponent("Blue", [charizard])

    main_window = Window("Pokemon Battle", (750, 450), trainer, opponent)

main()
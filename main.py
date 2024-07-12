from layout import Window
from pokemon import Pokemon
from trainers import Trainer, Opponent
from moves import Moves

def main():
    # Moves
    fire_blast = Moves("Fire Blast", 120, 85, 5)
    razor_leaf = Moves("Razor Leaf", 55, 95, 25)

    # Pokemon
    # Trainer Party
    venasaur = Pokemon("Venasaur", 200, [razor_leaf])

    # Opponent Party
    charizard = Pokemon("Charizard", 210, [fire_blast])


    # Trainers
    trainer = Trainer("Red", [venasaur])
    opponent = Opponent("Blue", [charizard])

    main_window = Window("Pokemon Battle", (750, 450), trainer, opponent)

main()
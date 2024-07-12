from layout import Window
from pokemon import Pokemon
from trainers import Trainer, Opponent

def main():

    # Pokemon
    # Trainer Party
    venasaur = Pokemon("Venasaur", 200)

    # Opponent Party
    charizard = Pokemon("Charizard", 210)


    # Trainers
    trainer = Trainer("Red", [venasaur])
    opponent = Opponent("Blue", [charizard])

    main_window = Window("Pokemon Battle", (750, 450), trainer, opponent)

main()
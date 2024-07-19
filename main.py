from layout import Window
from pokemon import Pokemon
from trainers import Player, Opponent
from moves import Moves

def main():
    # Trainers
    player = Player("Red", [])
    opponent = Opponent("Blue", [])


    # Moves
    # Player
    thunder_shock = Moves("Thunder Shock", 40, 100, 30)
    swift = Moves("Swift", 60, 100, 20)
    body_slam = Moves("Body Slam", 85, 100, 15)
    thunder = Moves("Thunder", 120, 70, 10)
    
    scratch = Moves("Scratch", 40, 100, 35)
    karate_chop = Moves("Karate Chop", 50, 100, 25)
    thrash = Moves("Thrash", 90, 100, 20)
    skull_bash = Moves("Skull Bash", 100, 100, 15)

    water_gun = Moves("Water Gun", 40, 100, 25)
    ice_beam = Moves("Ice Beam", 95, 100, 10)
    hydro_pump = Moves("Hydro Pump", 120, 80, 5)
    bubble_beam = Moves("Bubble Beam", 65, 100, 20)

    lick = Moves("Lick", 20, 100, 30)
    dream_eater = Moves("Dream Eater", 100, 100, 15)
    psychic = Moves("Psychic", 90, 100, 10)
    strength = Moves("Strength", 80, 100, 15)


    headbutt = Moves("Headbutt", 70, 100, 15)
    # body slam
    hyper_beam = Moves("Hyper Beam", 150, 90, 5)
    mega_kick = Moves("Mega Kick", 120, 75, 5)

    razor_leaf = Moves("Razor Leaf", 55, 95, 25)
    vine_whip = Moves("Vine Whip", 35, 100, 10)
    mega_drain = Moves("Mega Drain", 40, 100, 15)
    solarbeam = Moves("Solarbeam", 120, 100, 10)

    
    # Opponent
    wing_attack = Moves("Wing Attack", 60, 100, 35)
    sky_attack = Moves("Sky Attack", 140, 90, 5)
    gust = Moves("Gust", 40, 100, 35)
    fly = Moves("Fly", 70, 95, 15)

    psybeam = Moves("Psybeam", 65, 100, 20)
    # psychic
    confusion = Moves("Confusion", 50, 100, 25)
    mega_punch = Moves("Mega Punch", 80, 85, 20)

    horn_attack = Moves("Horn Attack", 65, 100, 25)
    stomp = Moves("Stomp", 65, 100, 20)
    earthquake = Moves("Earthquake", 100, 100, 10)
    rock_slide = Moves("Rock Slide", 75, 90, 10)
    
    # hydro pump
    # hyper beam
    bite = Moves("Bite", 60, 100, 25)
    tackle = Moves("Tackle", 35, 95, 35)

    # stomp
    # solar beam
    rage = Moves("Rage", 20, 100, 20)
    egg_bomb = Moves("Egg Bomb", 100, 75, 10)

    slash = Moves("Slash", 70, 100, 20)
    fire_spin = Moves("Fire Spin", 35, 85, 15)
    # rage
    fire_blast = Moves("Fire Blast", 120, 85, 5)
    

    # Pokemon
    # Player Party
    raichu = Pokemon("Raichu", 2.77, 2.52, 62, [thunder_shock, swift, body_slam, thunder], player)
    primeape = Pokemon("Primeape", 2.87, 2.42, 59, [scratch, karate_chop, thrash, skull_bash], player)
    lapras = Pokemon("Lapras", 4.17, 1.72, 57, [water_gun, ice_beam, hydro_pump, bubble_beam], player)
    gengar = Pokemon("Gengar", 2.77, 2.72, 60, [lick, dream_eater, psychic, strength], player)
    snorlax = Pokemon("Snorlax", 4.77, 1.12, 58, [headbutt, body_slam, hyper_beam, mega_kick], player)
    venasaur = Pokemon("Venasauar", 3.17, 2.12, 64, [razor_leaf, vine_whip, mega_drain, solarbeam], player)
    player_party = [raichu, primeape, lapras, gengar, snorlax, venasaur]
    for member in player_party:
        player.party.append(member)

    # Opponent Party
    pidgeot = Pokemon("Pidgeot", 3.23, 2.34, 61, [wing_attack, sky_attack, gust, fly], opponent)
    alakazam = Pokemon("Alakazam", 2.67, 2.92, 59, [psybeam, psychic, confusion, mega_punch], opponent)
    rydon = Pokemon("Rydon", 3.67, 1.32, 61, [horn_attack, stomp, earthquake, rock_slide], opponent)
    gyarados = Pokemon("Gyarados", 3.47, 2.14, 63, [hydro_pump, hyper_beam, bite, tackle], opponent)
    exeggutor = Pokemon("Exeggutor", 3.47, 1.62, 61, [stomp, solarbeam, rage, egg_bomb], opponent)
    charizard = Pokemon("Charizard", 3.13, 2.52, 65, [slash, fire_spin, rage, fire_blast], opponent)
    opponent_party = [pidgeot, alakazam, rydon, gyarados, exeggutor, charizard]
    for member in opponent_party:
        opponent.party.append(member)
    

    main_window = Window("Pokemon Battle", (900, 525), player, opponent)

main()
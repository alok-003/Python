import random

regions_E = ("Braavos","Pentos","Myr","Tyrosh","Lys","Volantis","Lorath","Norvos","Qohor")
regions_W = ("North","Vale","Riverlands","Iron Islands","Westerlands","Reach","Stormlands","Dorne","Crownlands")

hintsE = (
    "A city of canals and Titan watchers, famous for secretive bankers and masked swordsmen.",
    "A coastal city where wealthy magisters rule but bend easily to stronger neighbors.",
    "Known for its master lens-makers and intricate glasswork.",
    "A city where brightly dyed beards and mercenary captains abound.",
    "Islands of pleasure and beauty, where courtesans hold as much sway as princes.",
    "The oldest and grandest Free City, marked by its Long Bridge and fiery devotion to the Red God.",
    "Remote and reclusive, with labyrinths from forgotten times.",
    "Stern bearded priests rule here, where bells ring louder than kings.",
    "A city of dark forests and smiths who alone still know how to reforge Valyrian steel.")

hintsW = ("Harsh, cold, and loyal, where direwolves roam and Winter always comes.",
    "A mountain stronghold guarded by the impregnable Eyrie.",
    "A fertile land of rivers, yet often a battlefield for greater powers.",
    "Stormy, sea-swept isles where the Drowned God reigns.",
    "Golden hills and mines that make their lions roar with wealth.",
    "The green and bountiful breadbasket of the realm.",
    "A rugged coast battered by endless tempests.",
    "Hot sands, spicy wines, and people who bow to no one.",
    "The royal heart of the realm, home to the Iron Throne.")

print("Hello!\nWelcome to Guess the G.O.T Region game!")

in1 = int(input("Enter 1 to enter the game: "))

if in1 == 1:
    ConSec = int(input("Select The Continent:\n Westeros (1) or Essos (2): "))

    if ConSec == 1:
        # Pick random index for Westeros
        idx = random.randrange(len(regions_W))
        answer = regions_W[idx]
        hint = hintsW[idx]
        print("HINT:", hint)

        while True:
            guess = input("Answer: ")
            if guess == answer:
                print("Correct Answer!")
                break
            else:
                print("Try again...")

    elif ConSec == 2:
        # Pick random index for Essos
        idx = random.randrange(len(regions_E))
        answer = regions_E[idx]
        hint = hintsE[idx]
        print("HINT:", hint)

        while True:
            guess = input("Answer: ")
            if guess == answer:
                print("Correct Answer!")
                break
            else:
                print("Try again...")

    else:
        print("Invalid Choice!")

else:
    print("Goodbye\nThank You!")

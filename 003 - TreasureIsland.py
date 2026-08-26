import time

def narrar(texto, velocidade=0.02):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidade)
    print()

# Entendendo a função:
"""
    Exibe um texto no terminal caractere por caractere,
    criando um efeito de digitação.

    Parâmetros:
        texto (str): Texto que será exibido.
        velocidade (float): Tempo, em segundos, entre cada caractere.
                            O valor padrão é 0.03.

    Funcionamento:
        - Percorre cada caractere do texto com um loop.
        - Imprime cada caractere sem quebrar a linha.
        - Usa time.sleep() para criar uma pequena pausa entre eles.
        - Ao finalizar, quebra a linha com print().
    """

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Beltrão]
*******************************************************************************
''')
narrar("🏝️ Welcome to Treasure Island...")
time.sleep(1)

narrar("After a long journey, you finally arrive at the mysterious island.")
narrar("The wind is strong, and the sound of the ocean echoes behind you...")

time.sleep(1)

narrar("\nIn front of you, the path splits into two directions.")

print("\n⬅️  [LEFT]  A dark path surrounded by trees.")
print("➡️  [RIGHT] A narrow path that follows the coast.")


while True:
    choice = input("\nWhich way do you want to go? Left or Right?\n> ").upper()

    if choice in ("LEFT", "RIGHT"):
        break

    print()
    print("Trying to steal, huh?\n"
        "You have to choose a path, you cannot run away!")

if choice == "LEFT":
    print("\n" + "=" * 50)
    narrar("🌊 THE MYSTERIOUS LAKE")
    print("=" * 50)

    narrar("\nAfter walking through the dark forest...")
    narrar("You finally arrive at a huge lake.")
    narrar("The water is strangely quiet...")

    print("\nWhat do you want to do?")
    print("[1] 🚤 Wait for the boat")
    print("[2] 🏊 Swim across")

    choice = input("\n👉 Your choice: ")
    if choice == "1":
        narrar("\n🚤 You decide to wait for the boat...")
        time.sleep(1)

        narrar("After a few minutes, a small boat appears through the fog.")
        narrar("You climb aboard and safely cross the lake.")

        time.sleep(1)

        narrar("\n🏝️ After the journey, you arrive at another mysterious island...")
        narrar("You survived! But your adventure is not over yet...")
        narrar("\n🌴 You step onto the mysterious island...")
        time.sleep(1)

        narrar("A thick fog covers the ground, and everything is strangely quiet.")
        narrar("As you walk deeper into the island, you notice something huge in the distance...")

        time.sleep(1)

        narrar("\n🏰 A MAGIC CASTLE!")
        narrar("Its towers rise above the trees, glowing under the moonlight.")
        narrar("You slowly approach the castle and push open its enormous gates...")

        time.sleep(1)

        narrar("\nInside, you find a dark hall illuminated by floating candles.")
        narrar("At the end of the hall, there are THREE mysterious doors.")

        time.sleep(1)

        print("\n🚪 Choose a door:")
        print("🔵 [BLUE]  A cold blue light shines beneath it.")
        print("🔴 [RED]   You can feel heat coming from behind it.")
        print("🟢 [GREEN] Strange sounds echo from the other side.")

        door = input("\n👉 Which door do you choose? BLUE, RED or GREEN?\n> ").upper()

        if door == "BLUE":
            narrar("\n🔵 You slowly open the BLUE door...")
            time.sleep(1)

            narrar("A powerful blue light fills the entire room.")
            narrar("You feel a strange magical energy surrounding you...")

            time.sleep(1)

            narrar("\n✨ A mysterious voice echoes through the castle:")
            narrar('"You have chosen wisely..."')
            narrar('"From this moment, the treasure belongs to you!"')

            time.sleep(1)

            print("\n👑 YOU ARE THE WINNER!")
            print("💰 You found the legendary treasure of Treasure Island!")
            print("✨ The magic of the castle recognizes you as its new owner.")

        elif door == "RED":
            narrar("\n🔴 You slowly open the RED door...")
            time.sleep(1)

            narrar("Suddenly, the room becomes incredibly hot.")
            narrar("Flames surround the chamber and there is no way back.")

            time.sleep(1)

            print("\n🔥 GAME OVER")
            print("The red door was a deadly trap.")

        elif door == "GREEN":
            narrar("\n🟢 You slowly open the GREEN door...")
            time.sleep(1)

            narrar("The room is completely dark...")
            narrar("Then you hear something moving around you.")

            time.sleep(1)

            narrar("🐍 The room is filled with dangerous snakes!")

            time.sleep(1)

            print("\n🐍 GAME OVER")
            print("The green door was a trap.")
        else:
            print("You have to choose a door do not try to run away!")



    elif choice == "2":
        narrar("\n🏊 You jump into the water and start swimming...")
        time.sleep(1)

        narrar("Suddenly, you notice something moving beneath the water...")
        time.sleep(1)

        narrar("🐊 A huge alligator appears!")
        narrar("You couldn't escape.")

        print("\n💀 GAME OVER")

    else:
        print("\n❌ Invalid option. Choose 1 or 2.")





    
elif choice == "RIGHT":
    narrar("\n➡️ You decide to take the path on the right...")
    time.sleep(1)

    narrar("The trail becomes narrower as you walk deeper into the island.")
    narrar("The wind suddenly stops...")
    narrar("Everything becomes completely silent.")

    time.sleep(1)

    narrar("\nYou hear a strange noise behind the bushes...")
    time.sleep(1)

    narrar("Before you can turn back, the ground beneath you collapses!")

    time.sleep(1)

    narrar("\nYou fall into an ancient trap hidden on the island.")

    print("\n💀 GAME OVER")
    print("You chose the wrong path.")
else:
    print("Trying to steal, huh? Game over.")



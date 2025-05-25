# escape_room_game.py
# COMP9001 Final Project - Escape Room Puzzle Game
# Author: Vicky z

#  Introduction function 
def intro(name):
    print(f"\nWelcome, {name}. You find yourself locked in a mysterious room.")
    print("Your goal is to find clues and escape!")
    print("Type 'help' at any time to see the list of available commands.\n")

#  Help command to list available actions 
def help_menu():
    print("\nAvailable commands:")
    print(" - look around")
    print(" - inspect [object] (e.g. inspect table)")
    print(" - use [item] (e.g. use key)")
    print(" - inventory")
    print(" - status")
    print(" - quit\n")

#  Main game logic loop 
def game_loop(name):
    inventory = []
    tries_left = 3
    states = {
        "door_unlocked": False,
        "painting_moved": False,
        "key_found": False,
        "safe_unlocked": False,
        "code_paper_found": False,
        "teddy_hint_given": False,
        "wrong_key_used": False,
    }

    print(f"{name}, your escape begins now...\n")

    while True:
        command = input("> ").strip().lower()

        if command == "help":
            help_menu()

        elif command == "look around":
            print("\nYou see a door, a table, a painting, a lamp, a mirror, and a teddy bear sitting in the corner.")

        elif command.startswith("inspect"):
            obj = command.replace("inspect ", "")
            if obj == "door":
                print("🚪 The door has a digital keypad. It requires a 4-digit code.")
            elif obj == "table":
                print("🗄️ There's an old wooden table. It has a drawer.")
            elif obj == "drawer":
                if not states["key_found"]:
                    print("📦 You open the drawer and find two small keys: one silver, one black. You take both.")
                    inventory.append("silver key")
                    inventory.append("black key")
                    states["key_found"] = True
                else:
                    print("The drawer is empty.")
            elif obj == "painting":
                if not states["painting_moved"]:
                    print("🖼️ You move the painting aside and discover a locked safe behind it.")
                    states["painting_moved"] = True
                else:
                    print("The safe is still there, waiting to be opened.")
            elif obj == "safe":
                if "silver key" in inventory and not states["safe_unlocked"]:
                    print("🔓 You use the silver key to unlock the safe. Inside is a note: 'Code = 3927'")
                    states["safe_unlocked"] = True
                    states["code_paper_found"] = True
                elif "black key" in inventory and not states["safe_unlocked"]:
                    print("❌ You try the black key... it snaps inside the lock!")
                    print("The safe is now jammed. You can't open it anymore. Game Over.")
                    states["wrong_key_used"] = True
                elif states["safe_unlocked"]:
                    print("The safe is already open. The note says: 'Code = 3927'")
                else:
                    print("The safe is locked. You probably need a key.")
            elif obj == "lamp":
                print("💡 The lamp is flickering. Nothing special here.")
            elif obj == "mirror":
                print("🪞 In the mirror, the painting's reflection looks warped... odd.")
            elif obj == "teddy":
                if not states["teddy_hint_given"]:
                    print("🧸 You hug the teddy bear. It's soft and comforting.")
                    print("You see something stitched on its paw: 'Black is cursed.'")
                    states["teddy_hint_given"] = True
                else:
                    print("🧸 The teddy sits quietly. Still soft.")
            else:
                print("You can't inspect that object.")

        elif command.startswith("use"):
            obj = command.replace("use ", "")
            if obj == "door":
                if states["door_unlocked"]:
                    print(f"🎉 You open the door and escape the room. Well done, {name}!")
                    break
                elif tries_left <= 0 or states["wrong_key_used"]:
                    print("🚨 The door won't open. You're out of options. Game Over.")
                    break
                else:
                    code = input("Enter the 4-digit code: ")
                    if code == "3927":
                        print("✅ Correct code! The door is now unlocked.")
                        states["door_unlocked"] = True
                    else:
                        tries_left -= 1
                        print(f"❌ Incorrect code. Attempts left: {tries_left}")
            elif obj == "silver key":
                if "silver key" in inventory:
                    if not states["safe_unlocked"]:
                        print("🔓 You unlock the safe with the silver key. Inside is a note with the code: 3927.")
                        states["safe_unlocked"] = True
                        states["code_paper_found"] = True
                    else:
                        print("The safe is already open.")
                else:
                    print("You don’t have the silver key.")
            elif obj == "black key":
                if "black key" in inventory:
                    print("❌ The black key snaps as you try to use it... something feels wrong.")
                    states["wrong_key_used"] = True
                else:
                    print("You don’t have the black key.")
            else:
                print("You can't use that item.")

        elif command == "inventory":
            if inventory:
                print("🎒 Your backpack contains: " + ", ".join(inventory))
            else:
                print("Your backpack is empty.")

        elif command == "status":
            print("\n🔎 Current progress:")
            for key, value in states.items():
                check = "✅" if value else "❌"
                print(f" - {key.replace('_', ' ').capitalize()}: {check}")

        elif command == "quit":
            print("You chose to quit the game. Goodbye!")
            break

        else:
            print("⚠️ Invalid command. Type 'help' to see what you can do.")

#  Game entry point 
if __name__ == "__main__":
    player_name = input("Enter your name: ")
    intro(player_name)
    game_loop(player_name)

import time
import builtins

original_print = builtins.print
original_input = builtins.input

def slow_print(*args, sep=' ', end='\n', delay=0.01, **kwargs):
    text = sep.join(map(str, args))
    for char in text:
        original_print(char, end='', flush=True)
        time.sleep(delay)
    original_print(end=end, flush=True)


def slow_input(prompt='', delay=0.01):
    for char in prompt:
        original_print(char, end='', flush=True)
        time.sleep(delay)
    return original_input()


builtins.print = slow_print
builtins.input = slow_input

class Game:
    def __init__(self):
        self.rooms = {
            "living_room": {
                "description": "A cozy living room with a fireplace and a sofa.",
                "objects": [
                    {"name": "family portrait", "type": "descriptive", "description": "A portrait of your family, smiling together."},
                    {"name": "newspaper", "type": "descriptive", "description": "An old newspaper with headlines about the new year."},
                    {"name": "key", "type": "usable", "description": "A small golden key that might unlock something."},
                ],
            },
            "kitchen": {
                "description": "A small kitchen with a fridge and a dining table.",
                "objects": [
                    {"name": "knife", "type": "usable", "description": "A sharp kitchen knife."},
                    {"name": "recipe book", "type": "descriptive", "description": "A book filled with old family recipes."},
                    {"name": "apple", "type": "descriptive", "description": "A fresh, red apple."},
                ],
            },
            "master bedroom": {
                "description":"this is grandma and grandpa's bedroom.",
                "objects": [
                    {'name': "grandma's dairy",'type':'descriptive'},
                    {'name':"grandpa's portrait",'type':"descriptive"},
                    {'name':""},

                ] 
            },
            "dads bedroom ":{
                "description":"this is dad's bed room .",
                "objects":[
                    {"name": "watch", "type": "usable", "description": "Dad's old wristwatch."},
                    {"name": "book", "type": "descriptive", "description": "A book about engineering."},
                    {"name": "glasses", "type": "usable", "description": "A pair of reading glasses."},
                ]
            },
            "basement": {
                "description": "A dark and cold basement with a musty smell.",
                "objects": [
                    {"name": "old chest", "type": "descriptive", "description": "A locked chest covered in dust."},
                    {"name": "lamp", "type": "usable", "description": "An old oil lamp with a cracked glass."},
                    {"name": "tools", "type": "descriptive", "description": "A set of rusty tools hanging on the wall."},
                 ],
            },
            "bathroom": {
                "description": "A clean bathroom with a mirror and a sink.",
                "objects": [
                    {"name": "toothbrush", "type": "usable", "description": "A blue toothbrush."},
                    {"name": "towel", "type": "descriptive", "description": "A soft white towel."},
                    {"name": "soap", "type": "usable", "description": "A bar of lavender-scented soap."},
                 ],
             },
            "aunt's bedroom": {
                "description": "This is aunt's bedroom.",
                "objects": [
                    {"name": "jewelry box", "type": "descriptive", "description": "A small box filled with necklaces and rings."},
                    {"name": "perfume", "type": "usable", "description": "A bottle of aunt's favorite perfume."},
                    {"name": "photo album", "type": "descriptive", "description": "An album full of family photos."},
                 ],
             },
            # add more item
            # more room
        }
        self.inventory = []
        self.current_room = "living_room"

    def describe_room(self):
        room = self.rooms[self.current_room]
        print(f"\n{room['description']}")
        inspecting=str(input("do you want to inspect the room? ")).lower
        if inspecting == "yes":
                if room["objects"]:
                    print("You see the following objects: ", ", ".join(obj["name"] for obj in room["objects"]))
                else:
                    print("There are no objects here.")
        elif inspecting == "no":
            print("then we are going to the next room")
            
    def interact_with_item(self, item_name):
        room = self.rooms[self.current_room]
        item = next((obj for obj in room["objects"] if obj["name"].lower() == item_name.lower()), None)
        if item:
            print(f"\nYou selected the {item['name']}.")
            print(f"Description: {item['description']}")
            if item["type"] == "usable":
                action = input(f"What would you like to do with the {item['name']}? (use/store): ").lower()
                if action == "use":
                    print(f"You used the {item['name']}!")
                    #function for the item here
                elif action == "store":
                    print(f"The {item['name']} has been stored in your inventory.")
                    self.inventory.append(item)
                    room["objects"].remove(item)
                else:
                    print("Invalid choice. The item is stored by default.")
                    self.inventory.append(item)
                    room["objects"].remove(item)
            else:
                print(f"The {item['name']} is a descriptive item and has been stored in your inventory.")
                self.inventory.append(item)
                room["objects"].remove(item)
        else:
            print("That item is not in this room.")

    def interact(self):
        room = self.rooms[self.current_room]
        while room["objects"]:
            item_name = input("Type the name of the item you want to interact with (or type 'leave' to stop): ").lower()
            if item_name == "leave":
                print("You decided to stop interacting.")
                break
            self.interact_with_item(item_name)

    def move_room(self, new_room):
        if new_room in self.rooms:
            self.current_room = new_room
            self.describe_room()
        else:
            print("You can't go there.")

    def play(self):
        while True:
            print("Hello and welcome to Christmas Mystery.")
            print("\nPress 'F' for instructions.")
            start = input("Press 'S' to start the game, or 'Q' to quit: ").lower()

            if start == 's':
                self.back_story()
                break
            elif start == 'f':
                self.show_instructions()
            elif start == 'q':
                print("Goodbye!")
                return
            else:
                print("Invalid input. Please try again.")

        while True:
            self.describe_room()
            self.interact()
            new_room = input("Where would you like to go next? (type room name or 'quit' to exit): ").lower()
            if new_room == "quit":
                print("Thanks for playing Goodbye!")
                break
            self.move_room(new_room)

    def back_story(self):
        text ='''\nIt's New Year, and you are at your grandmother's house.
You wake up early in the morning and realize a thief was in the house and stole all of the presents.
Grandmother and the grandkids are really sad.
Now it's your job to find the gifts and make your grandmother happy again.'''
        
        for char in text:
            print(char , end='',flush=True)
            time.sleep(0.03)


    def show_instructions(self):
        print('''
        - By using the map, you can go to different places.
        - Press 'M' to open the map.
        - You can press 'I' to open your inventory at any time.
        - By entering each place, you will get some information and access to interactions.
        ''')

# Start the game
game = Game()
game.play()

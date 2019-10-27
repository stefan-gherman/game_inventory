# game inventory functions file

def display_inventory(inventory):
    for item, value in inventory.items():
        print("{}:{}".format(item, value))

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1     

#tests
INV = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}        
display_inventory(INV)
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print("\n")
add_to_inventory(INV, dragon_loot)
display_inventory(INV)


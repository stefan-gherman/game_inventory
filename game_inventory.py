# game inventory functions file

def display_inventory(inventory):

    for item, value in inventory.items():
        print("{}:{}".format(item, value))



#tests
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}        
display_inventory(inv)

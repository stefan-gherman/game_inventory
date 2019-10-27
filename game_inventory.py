# game inventory functions file

def display_inventory(inventory):   # Step 1
    for item, value in inventory.items():
        print("{}:{}".format(item, value))


def add_to_inventory(inventory, added_items): # Step 2
    for item in added_items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1     


def check_longest(lst):                   # A function that sorts the list of tuples by the lenght of the first element in the tuple
    sort_lenght = sorted(lst, key = lambda x: len(x[0]), reverse = True)    
    return len(sort_lenght[0][0])



def print_table(inventory, order = ""):    #Step 3
    if order == "count,desc":
        displayable_dict = sorted(inventory.items(), key = lambda item: item[1], reverse = True)
    elif order == "count,asc":
        displayable_dict = sorted(inventory.items(), key = lambda item: item[1])
    else:
        displayable_dict = list(inventory.items())

    padding = check_longest(displayable_dict)
    displayable_dict = dict(displayable_dict)
    
    
    
    print("-----------------" + '\n')
    print("item name | count" + '\n')
    print("-----------------" + '\n')
    for item, val in displayable_dict.items():
        print(str(item).rjust(padding) + " | "  + str(val).rjust(4) + '\n')
    print("-----------------")    
    

#tests
INV = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}        
#display_inventory(INV)
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#print("\n")
add_to_inventory(INV, dragon_loot)
display_inventory(INV)

print_table(INV)
print('\n')

print_table (INV, "count,desc")

print('\n')

print_table (INV, "count,asc")


#a = sorted(INV.items())
#print(type(a), a, a[1])
  
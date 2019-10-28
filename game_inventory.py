# game inventory functions file


def display_inventory(inventory):   # Step 1
    for item, value in inventory.items():
        print("{}: {}".format(item, value))


def add_to_inventory(inventory, added_items):  # Step 2
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
    
    
    #print(padding)
    print("-----------------" )
    print("item name | count" )
    print("-----------------" )
    for item, val in displayable_dict.items():
        print(str(item).rjust(padding) + " | "  + str(val).rjust(padding))
    print("-----------------")    


def string_separator(string):  # A function used to turn csv file input into a list usable by the add inventory function
    new_string = string.replace(",", ".").replace("\n","").replace("    ","")
    return new_string.split('.')



def import_inventory(inventory, filename = "import_inventory.csv"): #Step 4

    try:
        with open(filename) as csv_inv:
            mod_items = csv_inv.read()
        mod_items = string_separator(mod_items)
        add_to_inventory(inventory, mod_items)
        
    except FileNotFoundError:
        print("File '{}' not found!".format(filename))            


def calculate_items(inventory):
    total_items = 0
    for item in inventory.keys():
        total_items += inventory[item]
    return total_items    


def export_inventory(inventory, filename="export_inventory.csv"): #Step 5
    sort_inv = sorted(inventory.items(), key = lambda item:item[1], reverse = True)
    sort_inv = dict(sort_inv)
    string_items = []

    items_write = calculate_items(sort_inv)

    while items_write > 0:
        for item in sort_inv.keys():
            if sort_inv[item] != 0:
                string_items.append(item)
                sort_inv[item] -= 1
                items_write -= 1
    
    string_items = ",".join(string_items)
    #print(string_items)            


    try:
        with open(filename, 'w') as export_inv:
            export_inv.write(string_items)
    except PermissionError:
        print("You don't have permission creating file '{}'!".format(filename))    
        
            


# tests
INV = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}        
# display_inventory(INV)
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# print("\n")
add_to_inventory(INV, dragon_loot)
# display_inventory(INV)

print_table(INV)
# print('\n')

# print_table (INV, "count,desc")

# print('\n')

print_table (INV, "count,asc")


# a = sorted(INV.items())
# print(type(a), a, a[1])



# import_inventory(INV)
print_table (INV, "count,desc")

# export_inventory({"horse":2, "food":3, "something_else":1},"test_file.csv")

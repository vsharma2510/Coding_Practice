def displayInventory(inv):
    number_of_items = 0
    print('Inventory:')
    for k,v in inv.items():
        print(str(v)+ ' ' +k)
        number_of_items = number_of_items+v
    print('Total number of items: ' + str(number_of_items))

def addToInventory(inventory, addedItems):
    for i, val in enumerate(addedItems):
        if(val in inventory.keys()):
            inventory[val] = inventory[val] + 1
        if(val not in inventory.keys()):
            inventory[val] = 1

inventory = {'rope': 1,'torch': 6,'gold coin':42,'dagger': 1,'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
displayInventory(inventory)
addToInventory(inventory, dragonLoot)
displayInventory(inventory)

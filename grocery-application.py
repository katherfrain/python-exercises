class GroceryStore:
    def __init__(self):
        self.stores = []
        self.itemlist = []

    def add_store(self):
        answer = input('What store would you like to add to the list? Please enter "q" to exit this menu. ')
        while answer != 'q':
            self.stores.append(answer)
            self.stores.append(self.itemlist)
            print(self.stores)
            answer = input('Would you like to add another store? If so, please enter the name. If not, hit "q" to quit. ')
        # for store in self.stores:
        #     store.append(self.itemlist)

class ShoppingList:
    def __init__(self, stores):
        self.stores = stores
        # self.storelist = input("Where would you like to draw these stores from? ")

    def add_item(self):
        print(len(self.stores.stores))

        answer = input('Would you like to add an item to your shoppping list? ')

        while answer == 'yes':
          
            storename = input("What store would you like to create a shopping list for? ")
            offset_index = 0
          
            for store in self.stores.stores:
                offset_index = offset_index + 1
                print(store)

                if store == storename:   
        
                    add_item = input(f"What item would you like to purchase from {storename}? ")
                    self.stores.stores[offset_index] += add_item

                    print(self.stores.stores)
                    answer = input('Would you like to add another item? ')
        print(self.stores.stores)

        # if self.storelist.stores.contains(storename):

        #         answer = input(f"Would you like to add an item to the {storename} list? If so, please print the name of the item. If not, please hit 'q'. ")
        #         while answer != 'q':
        #             self.storelist.stores = f'{storename}: ' + answer
        #             item_list = input(f'Would you like to add another item? If so, please enter the item\'s name. If not, please press "q". ')





myListofStores = GroceryStore()
myListofStores.add_store()
myListofItems = ShoppingList(myListofStores)
myListofItems.add_item()
myListofItems.add_item()

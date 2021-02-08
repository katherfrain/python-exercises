class GroceryStore:
    def __init__(self):
        self.stores = []

    def add_store(self):
        answer = input('What store would you like to add to the list? Please enter "q" to exit this menu. ')
        while answer != 'q':
            self.stores.append(input('What store would you like to add to the list? '))
            print(self.stores)

WalMart = GroceryStore()
WalMart.add_store()

stores = []

class Store: 
  def __init__(self, name, address): 
    self.name = name 
    self.address = address 
    self.items = [] 
    
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


def makeagrocerylist():

    choice = ""
    while choice != 'q': 
        print("Enter 1 to add a store: ")
        print("Enter 2 to add item to a store: ")
        print("Enter q to quit: ")
        choice = input('Please enter a choice: ') 

        if choice == "1":
            store_name = input("Enter store name: ")
            store_address = input("Enter store address: ")
    
            store = Store(store_name, store_address)
            stores.append(store)  

        elif choice == "2":
            index = 1 
            for store in stores: 
                print(f'{index} ------ {store.name} is at {store.address}')
                index = index + 1

            try:
                add_index = int(input('Which store would you like to add to? ')) -1

            except ValueError:
                add_index = int(input('Please indicate a number, not a store name. ')) - 1
       
            print(stores[add_index].name)
            add_item = input('What item would you like to add to this list? ')
            price_item = float(input('How much does this item cost? '))
            quantity_item = float(input('And how many/much of that will you be getting? '))


            new_item = Item(add_item, price_item, quantity_item)

            stores[add_index].items.append(new_item)
            for item in stores[add_index].items:
                print(f'We have added {item.quantity} copies of {item.name} at {item.price} to your list')

        else:
            break

makeagrocerylist()
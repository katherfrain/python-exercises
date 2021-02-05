def ask_first_name():
    return input('Please input your first name: ')
    
def ask_last_name():
    return input('Please input your last name: ')

def ask_street():
    return input('Please enter your address. First, the street address:\n')

def ask_state():
    return input('Please enter your state: ')

def ask_zipcode():
    return input('Please enter your ZIP code: ')

def ask_address_from_user():
    street = ask_street()
    state = ask_state()
    zipcode = ask_zipcode()
    return {'street': street, 'state':state, 'zipcode':zipcode}

class Address: 

    def __init__(self = '', street = '', state = '', zipcode = ''):
        self.street = street
        self.state = state
        self.zipcode = zipcode

class User:
    def __init__(self, first_name = '', last_name = '', address_list = []):
        self.first_name = ask_first_name()
        self.last_name = ask_last_name()
        self.address_list = address_list

    def add_address(self, address = '', address_list = []):
        self.address = address
        self.address_list = address_list

        new_address = Address(
            street=ask_street(),
            state=ask_state(),
            zipcode=ask_zipcode()
        )  
        address_list.append(new_address)

        exit_to_menu = input('If you wish to exit this menu, enter "No new address."\n')
        
        if exit_to_menu != 'No new address':
            new_address = Address(
                street=ask_street(),
                state=ask_state(),
                zipcode=ask_zipcode()
            )
            address_list.append(new_address)
            exit_to_menu = input('If you wish to exit this menu, enter "No new address."\n')

    def display_addresses(self, address_list = []):
        self.adress_list = address_list
        print(f'{self.first_name} {self.last_name} reports living at these addresses: {address_list}')


user = User()
user.add_address()
user.display_addresses()


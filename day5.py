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

class User:
    def __init__(self):
        self.first_name = ask_first_name()
        self.last_name = ask_last_name()
        self.address_list = []

    def add_address(self, new_address):
        self.address_list.append(new_address)

    def display_addresses(self, address_list = []):
        self.adress_list = address_list
        print(f'{self.first_name} {self.last_name} reports living at these addresses: {address_list}')

class Address: 
    
    def __init__(self):
        self.street = ask_street()
        self.state = ask_state()
        self.zipcode = ask_zipcode()



user = User()
user.add_address(Address())
user.display_addresses()


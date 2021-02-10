favorite_dishes = input('My dude, list for me your favorite foods: ')


with open('dude.txt','a') as new_file:
    while favorite_dishes != 'q':
        new_file.write



while favorite_dishes != 'q':
    with open('fave-dishes.txt', 'a') as file_object:
        file_object.write(favorite_dishes + '\n')
        favorite_dishes = input('Tell me another dish you like, or press q to quit. ')

with open('fave_dishes.txt', 'r') as file_object:
    content = file_object.read()
    print(content)
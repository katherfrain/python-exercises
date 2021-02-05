# friends = ['Jack', 'Noonan', 'Heather', 'Tim']

# #for dudes in range 0 to [however many friends I have]
# for dudes in range(len(friends)-1, -1, -1):
#     if friends[dudes] == 'Jack':
#         print('JACK')
#     else:
#         print(friends[dudes])

def palindrome(): 
    wordinput = input('Check if the inputted word is a palindrome: ')
    originalword = []
    palindromechecker = []

    #create a 'forwards' list of the word 
    for letter in range(0, len(wordinput)):
        #append pushes the letter at wordinput's current index into a list
        originalword.append(wordinput[letter])
        print(originalword)

    #forwards loop produces: [C, A, T]
    #backwards loop produces: [T, A, C] ==
    #comparison loop fines that this is NOT A VALID PALINDROME, you can see that the first letter of both words are not the same

    #[R,A,C,E,C,A,R]
    #[R,A,C,E,C,A,R]


    #create a 'backwards' list of the word
    for letter in range(len(wordinput)-1, -1, -1):
        palindromechecker.append(wordinput[letter])
        print(palindromechecker)

    #checks if the 'forwards' word is the EXACT SAME as the 'backwards' word
    #if the forwards word and the backwards word are NOT the same, return false
    #otherwise, if the forwards word and the backwards word ARE the same, we know it is a palindrome & can return true
 
    for letter in range(0, len(wordinput)):
        if originalword[letter] != palindromechecker[letter]:
            return False
            #return gives values to the computer - not you! If you want to see a value, it must be printed!
        return True

print(palindrome())


3 * (3 - 1) * (3-2) 
3 * 2 * 1 

def while_asker():
    answer = input('Do you wanna be my friend??? Press N if no. ')
    while answer != 'N':
        answer = input('Are you sure? ')
while_asker()
    
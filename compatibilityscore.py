alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 5
newMessage = ' '
score = 0

message = input('Enter the names of two people: ')

for character in message:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    print(newPosition)
    score += newPosition


print('Your compatibility score is: ' + str(score))



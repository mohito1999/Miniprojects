catNames = []
while True: #loop to record name of each cat. If nothing is entered then the for loop is printed which prints out all the cats
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):') #the + 1 part is to label the correct number for each cat
    name = input()
    if name == '':
        break

    catNames = catNames + [name] # list concatenation - adding each new cat to the list
print('The cat names are:')
for name in catNames:
    print(' ' + name)

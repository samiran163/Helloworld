import random
list = [2, 18, 8, 4]
print ("Prior Shuffling - 0", list)
random.shuffle(list)
print ("After Shuffling - 1", list)
random.shuffle(list)
print ("After Shuffling - 2", list)

#splitting

string = "Hi My name is samiran"

print(string.split(","))

#string to list

#list('I am staying in bangalore')
#print(list)


keyword = 'aeioubcdfg'
print (keyword [:3] + keyword [3:])
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice_cream')
print("My favorite foods are:") 
print(my_foods)
print("\nMy friend's favorite foods are:") 
print(friend_foods)

print("The first three items in the list are: ")
print(my_foods[0:3])
print("The first three items from the middle of the list are: ")
middle = int(len(my_foods)/2)
print(my_foods[middle:3 + middle])
last = len(my_foods)

print("The first three items from the middle of the list are: ")
print(my_foods[last - 3: last])

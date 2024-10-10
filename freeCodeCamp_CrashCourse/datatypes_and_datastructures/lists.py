'''

Lists - builtin data structure

To define a list, we use square brackets [] with the elements separated by a comma.

'''

my_list = [1, "Emily", 3.4]
nested_list = [[1, 2, 3], [4, 5, 6]]

# We can access the nested lists using their corresponding index

print(my_list[0])


'''
Nested lists could be used to represent, for example, the structure of a 
simple 2D game board where each number could represent a different element or tile:

# Sample Board where: 
# 0 = Empty tile
# 1 = Coin
# 2 = Enemy
# 3 = Goal
board = [[0, 0, 1],
         [0, 2, 0],
         [1, 0, 3]]

'''

# Common function/attr

print(len(my_list))  # gives len

# Update value in the list

letters = ["a", "b", "c", "d"]
letters[0] = 'z'
print(f"letters -  {letters}")


# Add value in the list

letters.append(2)
print(f"letters -  {letters}")


# Remove value in the list

letters.remove(2)  # you have to specify value (not index) & this removes only first occurence
print(f"letters -  {letters}")


# Accessing by index & slicing -> like strings

print(letters[1:3])
print(letters[::-1]) 


# List methods

print('------ List Methods -------')

freecodecampmy_list = [1, 2, 3, 3, 4]

freecodecampmy_list.append(5)
print(freecodecampmy_list)


freecodecampmy_list.extend([6, 7, 8])
print(freecodecampmy_list)


freecodecampmy_list.insert(2, 15) # first arg is index, second is value
print(freecodecampmy_list)


freecodecampmy_list.remove(2)
print(freecodecampmy_list)


print(freecodecampmy_list.pop())


print(freecodecampmy_list.index(6))


print(freecodecampmy_list.count(2))


freecodecampmy_list.sort()
print(freecodecampmy_list)


freecodecampmy_list.reverse()
print(freecodecampmy_list)


freecodecampmy_list.clear()
print(freecodecampmy_list)

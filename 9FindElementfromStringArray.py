#python program to find an element from the string array

# assign list
l = [1, 2.0, 'have', 'a', 'welcome', 'day']

# assign string
s = 'welcome'

# check if string is present in the list
if s in l:
    print(f'{s} is present in the list')
else:
    print(f'{s} is not present in the list')



print("------------------------------------")

#Method 2

l1 = ['A', 'B', 'c', 'D', 'e', 'A', 'C']

# string in the list
if 'A' in l1:
    print('A is present in the list')

# string not in the list
if 'F' not in l1:
    print('F is not present in the list')


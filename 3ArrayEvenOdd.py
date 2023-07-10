num_list = [10,20,22,1,23,54,13,7,15]
print("List : ",num_list)
even_list = []
odd_list = []
for i in range(len(num_list)):
  if(num_list[i]%2 == 0):
    even_list.append(num_list[i])
  else:
    odd_list.append(num_list[i])
print("Even Numbers List : ", even_list)
print("Odd Numbers List : ", odd_list)


print("----------------------------------------")
#Method2

num_list=[]
n = int(input("Enter the Starting of the range : "))
k = int(input("Enter the Ending of the range : "))
for i in range(n,k):
  num_list.append(i)
print("Original Number List:", num_list)
even_list = []
odd_list = []
for i in range(len(num_list)):
  if(num_list[i]%2 == 0):
    even_list.append(num_list[i])
  else:
    odd_list.append(num_list[i])
print("Even Numbers List:", even_list)
print("Odd Numbers List:", odd_list)
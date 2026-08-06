n=int(input("Enter the number of elements in the list: "))
my_list=[]
for i in range(n):
    element=input("Enter element {}: ".format(i+1))
    my_list.append(element) 

print("The list you entered is:", my_list)
m=max(my_list)
print("The maximum element in the list is:", m)
n=min(my_list)
print("The minimum element in the list is:", n)
my_list.sort()
print("The sorted list is:", my_list)
my_list.sort(reverse=True)
print("The list sorted in descending order is:", my_list)

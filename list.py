list1=[12,4,35,19,78,2]
list2=[1.8,2,4,7,12]

sum = 0
multi = 1 

for x in list1:
	sum= sum + x
	multi=multi*x

print("Sum of all numbers in list1 is: ",sum)
print("Multiplication  of all numbers in list1 is: ",multi)

print("Largest number in list1: ",min(list1))
print("Smallest number in list1: ",max(list1))

list1.reverse() 
print("Reversed list1 is: ",list1)

print("Comomn numbers in list1 and list2 are: ")
for i in list1:
	for j in list2:
		if(i==j):
			print(j)

print("Even numbers in list1 are:")
for i in list1:
	if(i%2==0):
		print(i)


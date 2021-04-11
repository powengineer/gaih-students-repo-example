#swap the first half with the second half
n = [100, 65, 78, "Hello", 6.7, -84, 78, "Bye"] #define a dummy list
t = len(n) #determine the length of the list
n1 = n[:int(t/2)] #take the first half
n2 = n[int(t/2):] #take the second half
#exchange the two halves
temp = n1
n1 = n2
n2 = temp
#stich them to each other and reform the list
n = n1 + n2
#print all
print(n)



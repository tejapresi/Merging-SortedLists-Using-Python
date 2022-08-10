"""Merging sorted lists"""


#sorted list named Lis1
Lis1 = [-22,-1,2,4,5,7]
#sorted list named Lis2
Lis2 = [1,2,3,6,11,12,13]


#empty list named sortedList in which we store the merged sorted lists
sortedList = []

#sentinal value (When to stop comparing the lists)
sentinal = 0

#append the sentinal values in both Lis1 and Lis2
Lis1.append(sentinal)
Lis2.append(sentinal)


#length variable to store the sum of two lists length
length = len(Lis1)+len(Lis2)

#assign 0 to index1
index1 = 0
#assign 0 to index2
index2 = 0


#iterating while loop
while (index1+index2)<=length:

	#if the any of the list reaches sentinal value
	if Lis1[index1]==sentinal or Lis2[index2] == sentinal:
		
		#exit from the loop
		break

	#if the Lis1[index1] value <= Lis2[index2]
	elif Lis1[index1]<=Lis2[index2]:
		
		#append the Lis1[index1] to sortedList
		sortedList.append(Lis1[index1])
		#incrementing index1 value
		index1+=1

	#else (Lis2[index2] > Lis1[index1])
	else:

		#append the Lis2[index2] to sortedList
		sortedList.append(Lis2[index2])
		#incrementing index2 value
		index2+=1
	
# if Lis1 values all aren't in sortedList then add the remaining values are appended
if index1<len(Lis1):

	sortedList += Lis1[index1:len(Lis1)-1]

#if Lis2 values all aren't in sortedList then add the remaining values are appended
if index2<len(Lis2):
	sortedList += Lis2[index2:len(Lis2)-1]

#printing sortedList
print(sortedList)
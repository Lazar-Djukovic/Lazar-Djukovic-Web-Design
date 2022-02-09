#A program is to be written which merges the following two sorted lists list1 and list2 into a single sorted list called mergeList and prints out all three lists.
#original lists
list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
#variables and the new list
MergeList = []
index1 = 0
index2 = 0
i = 0
j = 0

while index1 < len(list1) and index2 < len(list2):
 if list1[index1] < list2[index2]:
  MergeList.append(list1[index1])
  index1 = index1 + 1
 else:
  MergeList.append(list2[index2])
  index2 =index2 + 1
    #endif
#endwhile

for i in range(index1, len(list1)):
	MergeList.append(list1[i])

for j in range(index2, len(list2)):
    MergeList.append(list2[j])

print(list1)
print(list2)
print(MergeList)